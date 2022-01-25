#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2022, Justin Béra (@just1not2) <me@just1not2.org>
# GNU General Public License v3.0+ (see LICENCE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: pm2_facts
short_description: Return PM2 information as fact data
description:
  - Return PM2 information as fact data for PM2 process management.
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
extends_documentation_fragment:
  - action_common_attributes
attributes:
  check_mode:
    support: full
  diff_mode:
    support: none
  facts:
    support: full
  platform:
    platforms: posix
notes: []
author:
  - Justin Béra (@just1not2)
'''


EXAMPLES = r'''
- name: Populate PM2 facts
  just1not2.pm2.pm2_facts:

- name: Print PM2 facts
  ansible.builtin.debug:
    var: ansible_facts.pm2
'''


RETURN = r'''
ansible_facts:
  description:
    - Facts to add to ansible_facts about PM2.
  returned: success
  type: dict
  contains:
    pm2:
      description:
        - Information about PM2.
      returned: success
      type: dict
      contains:
        executable:
          description:
            - The explicit executable or pathname for the pm2 executable.
          returned: success
          type: str
          sample: /usr/local/bin/pm2
        processes:
          description:
            - The list of PM2 processes.
          returned: success
          type: list
          elements: dict
          contains:
            cwd:
              description:
                - The path to the directory from which the script runs.
              returned: success
              type: str
              sample: /home/user
              version_added: "1.2.0"
            file:
              description:
                - The path to the process script file.
              returned: success
              type: str
              sample: /path/to/script.py
            id:
              description:
                - The PM2 id of the process.
              returned: success
              type: int
              sample: 0
            interpreter:
              description:
                - The path to the process script interpreter.
              returned: success
              type: str
              sample: /usr/bin/python3
            mode:
              description:
                - The PM2 mode of the process.
              returned: success
              type: str
              sample: fork_mode
            monitor:
              description:
                - The monitoring information about the process.
              returned: success
              type: dict
              contains:
                cpu:
                  description:
                    - The CPU percentage used by the process.
                  returned: success
                  type: float
                  sample: 20.7
                memory:
                  description:
                    - The memory used by the process (in Bytes).
                  returned: success
                  type: int
                  sample: 6500352
                restarts:
                  description:
                    - The number of times the process has been restarted.
                  returned: success
                  type: int
                  sample: 5
            name:
              description:
                - The name of the process.
              returned: success
              type: str
              sample: example
            namespace:
              description:
                - The namespace of the process.
              returned: success
              type: str
              sample: default
            pid:
              description:
                - The process ID (PID).
              returned: success
              type: int
              sample: 26741
            status:
              description:
                - The status of the process.
              returned: success
              type: str
              sample: online
        version:
          description:
            - The version of the PM2 executable used.
          returned: success
          type: str
          sample: "5.1.2"
'''


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.just1not2.pm2.plugins.module_utils.pm2 import Pm2Env


def main():

    module = AnsibleModule(
        argument_spec=dict(
            allow_update=dict(type="bool", default=True),
            executable=dict(type="path")
        ),
        supports_check_mode=True
    )

    env = Pm2Env(module)
    ansible_facts = dict(pm2=env.to_dict())

    result = dict(
        ansible_facts=ansible_facts,
        changed=False
    )
    module.exit_json(**result)

    return


if __name__ == "__main__":
    main()
