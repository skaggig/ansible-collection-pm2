#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2022, Justin Béra (@just1not2) <me@just1not2.org>
# GNU General Public License v3.0+ (see LICENCE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: pm2_process
short_description: Manage PM2 processes
description:
  - Control PM2 process state.
version_added: "1.0.0"
requirements:
  - pm2
options:
  allow_update:
    description:
      - Boolean that indicates if PM2 should be updated in case in-memory PM2 is out-of-date.
      - If this option is set to no, the module will return an error with out-of-date in-memory PM2.
    type: bool
    default: yes
  executable:
    description:
      - The explicit executable or pathname for the pm2 executable.
    type: path
  file:
    description:
      - The path to the process script file.
    type: path
  name:
    description:
      - The name of the process.
      - If this option is set to *, the module will match all processes.
    type: str
    required: true
  state:
    description:
      - The state of the process.
    type: str
    choices:
      - deleted
      - reloaded
      - restarted
      - started
      - stopped
    default: started
extends_documentation_fragment:
  - action_common_attributes
attributes:
  check_mode:
    support: full
  diff_mode:
    support: full
  platform:
    platforms: posix
notes: []
author:
  - Justin Béra (@just1not2)
'''


EXAMPLES = r'''
- name: Make sure PM2 example process is running
  just1not2.pm2.pm2_process:
    name: example
    file: /path/to/script.py

- name: Stop PM2 example process, if running
  just1not2.pm2.pm2_process:
    name: example
    state: stopped
'''


RETURN = r'''
'''


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.just1not2.pm2.plugins.module_utils.pm2 import Pm2Env


def main():

    module = AnsibleModule(
        argument_spec=dict(
            allow_update=dict(type="bool", default=True),
            executable=dict(type="path"),
            file=dict(type="path"),
            name=dict(type="str", required=True),
            state=dict(type="str", choices=["deleted", "reloaded", "restarted", "started", "stopped"], default="started")
        ),
        supports_check_mode=True
    )

    env = Pm2Env(module)
    processes = env.get_matching_processes(module.params["name"])
    diff = dict(
        before="",
        after=""
    )
    changed = False

    # If there is no matching process, creates one if state is "reloaded", "restarted" or "started"
    if not len(processes):
        if module.params["state"] in ["reloaded", "restarted", "started"]:

            # Fails if the file option is not defined
            if not module.params["file"]:
                module.fail_json(msg="Cannot create '%s' pm2 process: 'file' option not provided" % module.params["name"])

            # Otherwise, creates the process with the provided options
            else:
                env.create_process(module.params["name"], module.params["file"])
                diff["after"] += "'%s' state: started\n" % module.params["name"]
                changed = True

    else:
        # Initializes the list of processes that will be affected
        diff_processes = processes

        if module.params["state"] == "started":
            # Only keeps the matching processes that do not follow the provided options
            diff_processes = [process for process in processes if (
                process.status != "online" or
                (module.params["file"] and module.params["file"] != process.file)
            )]
        elif module.params["state"] == "stopped":
            # Only keeps the matching processes that are not already stopped
            diff_processes = [process for process in processes if process.status != "stopped"]

        for process in diff_processes:
            if module.params["state"] in ["restarted", "started"]:
                # Restarts the process and checks if it had to be deleted
                delete_and_restart = process.restart(module.params["file"])
                diff["before"] += "'%s' state: %s\n" % (process.name, process.status)
                diff["after"] += "'%s' state: %s\n" % (process.name, "deleted and restarted" if delete_and_restart else "restarted")

            elif module.params["state"] == "reloaded":
                # Reloads the process and checks if it had to be deleted
                delete_and_restart = process.reload(module.params["file"])
                diff["before"] += "'%s' state: %s\n" % (process.name, process.status)
                diff["after"] += "'%s' state: %s\n" % (process.name, "deleted and restarted" if delete_and_restart else "reloaded")

            elif module.params["state"] == "stopped":
                process.stop()
                diff["before"] += "'%s' state: %s\n" % (process.name, process.status)
                diff["after"] += "'%s' state: stopped\n" % process.name

            elif module.params["state"] == "deleted":
                process.delete()
                diff["before"] += "'%s' state: %s\n" % (process.name, process.status)
                diff["after"] += "'%s' state: deleted\n" % process.name

            changed = True

    result = dict(
        changed=changed
    )
    if module._diff:
        result["diff"] = diff
    module.exit_json(**result)

    return


if __name__ == "__main__":
    main()
