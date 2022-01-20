# -*- coding: utf-8 -*-

# Copyright: (c) 2022, Justin Béra (@just1not2) <me@just1not2.org>
# GNU General Public License v3.0+ (see LICENCE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


from json import dump, loads
from os import remove
from tempfile import NamedTemporaryFile


class Pm2Env():

    def __init__(self, module):

        self.module = module

        if module.params["executable"]:
            self.executable = module.params["executable"]
        else:
            self.executable = module.get_bin_path("pm2", True)

        # Gets PM2 version and eventually catches the PM2 starting message
        self.version = self.run("--version").split("\n")[-2]

        # Gathers PM2 process facts
        json = self.run("jlist")

        # Updates in-memory PM2 if it is out-of-date and the module options allow it
        if json.startswith("\n>>>> In-memory PM2 is out-of-date, do:"):
            if module.params["allow_update"]:
                self.run("update")
                json = self.run("jlist")
            else:
                self.module.fail_json(msg="In-memory PM2 is out-of-date and 'allow_update' has been set to 'no'")

        self.processes = []
        for process in loads(json):
            self.processes.append(
                Pm2Process(
                    self,
                    file=process["pm2_env"]["pm_exec_path"],
                    id=process["pm_id"],
                    interpreter=process["pm2_env"]["exec_interpreter"],
                    mode=process["pm2_env"]["exec_mode"],
                    monitor=dict(
                        memory=process["monit"]["memory"],
                        cpu=process["monit"]["cpu"],
                        restarts=process["pm2_env"]["restart_time"]
                    ),
                    name=process["name"],
                    namespace=process["pm2_env"]["namespace"],
                    pid=process["pid"],
                    status=process["pm2_env"]["status"],
                )
            )

    def to_dict(self):
        ''' Returns a dictionary translation of the environment '''

        return dict(
            executable=self.executable,
            processes=[process.to_dict() for process in self.processes],
            version=self.version
        )

    def run(self, command):
        ''' Runs a PM2 based command and return standard output '''

        rc, out, err = self.module.run_command("%s %s" % (self.executable, command))

        if rc != 0:
            self.module.fail_json(msg="Failed to run 'pm2 %s'" % command, rc=rc, err=err)

        return out

    def get_matching_processes(self, name):
        ''' Returns the list of processes whose name matches the name module parameter '''

        # Returns every processes for specified reserved name "*"
        if name == "*":
            return self.processes

        return [process for process in self.processes if process.name == name]

    def create_ecosystem_file(self, process_json):
        ''' Creates a PM2 temporary ecosystem file from a JSON and returns the file path '''

        ecosystem_file = None
        ecosystem_file_path = None

        try:
            # Creates the temporary file
            ecosystem_file = NamedTemporaryFile(mode="w", prefix="pm2", suffix=".json", delete=False)

            # Writes the JSON inside the file
            dump(
                dict(apps=[{key: process_json[key] for key in process_json if process_json[key]}]),
                ecosystem_file
            )
            ecosystem_file_path = ecosystem_file.name

        except Exception as err:
            self.module.fail_json(msg="Cannot create temporary file", err=repr(err))

        finally:
            ecosystem_file.close()

        return ecosystem_file_path

    def delete_ecosystem_file(self, ecosystem_file_path):
        ''' Deletes a temporary file '''

        try:
            remove(ecosystem_file_path)

        except Exception as err:
            self.module.fail_json(msg="Cannot delete temporary ecosystem file '%s'" % ecosystem_file_path, err=repr(err))

    def create_process(self, name, file):
        ''' Create a PM2 process '''

        # Raises an error if the specified name is "*" (reserved)
        if name == "*":
            self.module.fail_json(msg="Cannot create PM2 process with name '*': reserved name")

        elif not self.module.check_mode:
            process_json = dict(
                name=name,
                script=file
            )

            # Create a temporary ecosystem file for the new process
            ecosystem_file_path = self.create_ecosystem_file(process_json)

            self.run("start %s" % ecosystem_file_path)
            self.delete_ecosystem_file(ecosystem_file_path)


class Pm2Process():

    def __init__(self, env, **kwargs):

        self.env = env
        self.module = self.env.module

        for (key, value) in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        ''' Returns a dictionary translation of the process '''

        return dict(
            file=self.file,
            id=self.id,
            interpreter=self.interpreter,
            mode=self.mode,
            monitor=self.monitor,
            name=self.name,
            namespace=self.namespace,
            pid=self.pid,
            status=self.status
        )

    def execute_ecosystem_action(self, action, name, file):
        ''' Executes a PM2 action with an temporary ecosystem file and returns if process was deleted and recreated '''

        # If its script file changes, the process has to be deleted and restarted
        delete_and_restart = file and self.file != file

        if not self.module.check_mode:
            if delete_and_restart:
                self.delete()
                self.env.create_process(name, file)

            else:
                process_json = dict(
                    name=name,
                    script=self.file
                )
                # Create a temporary ecosystem file to update the process
                temporary_file = self.env.create_ecosystem_file(process_json)

                self.env.run("%s %s" % (action, temporary_file))
                self.env.delete_ecosystem_file(temporary_file)

        return delete_and_restart

    def restart(self, file):
        ''' Restarts the process '''

        return self.execute_ecosystem_action("restart", self.name, file)

    def reload(self, file):
        ''' Reloads the process '''

        return self.execute_ecosystem_action("reload", self.name, file)

    def stop(self):
        ''' Stops the process '''

        if not self.module.check_mode:
            self.env.run("stop %s" % self.id)

    def delete(self):
        ''' Deletes the process '''

        if not self.module.check_mode:
            self.env.run("del %s" % self.id)
