.. _just1not2.pm2.pm2_process:


*************************
just1not2.pm2.pm2_process
*************************

**Manage PM2 processes**


*New in version 1.0:* of just1not2.pm2

.. contents::
   :local:
   :depth: 1



Synopsis
--------

- Control PM2 process state.



Requirements
------------

The below requirements are needed on the host that executes this module.

- pm2



Parameters
----------

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th>Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
        <tr>
            <td>
                <b>allow_update</b>
                <div style="font-size: small">
                    <span style="color: purple">boolean</span>
                </div>
                <div style="font-size: small">
                    <span style="color: green; font-style: italic"></span>
                </div>
            </td>
            <td>
                <ul style="margin: 0; padding: 0">
                    <b>Choices:</b>
                    <li>no</li>
                    <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                </ul>
            </td>
            <td>
                <div>Boolean that indicates if PM2 should be updated in case in-memory PM2 is out-of-date.</div>
                <div>If this option is set to no, the module will return an error with out-of-date in-memory PM2.</div>
            </td>
        </tr>
        <tr>
            <td>
                <b>chdir</b>
                <div style="font-size: small">
                    <span style="color: purple">path</span>
                </div>
                <div style="font-size: small">
                    <span style="color: green; font-style: italic">added in 1.2</span>
                </div>
            </td>
            <td>
            </td>
            <td>
                <div>The working directory of the script.</div>
            </td>
        </tr>
        <tr>
            <td>
                <b>executable</b>
                <div style="font-size: small">
                    <span style="color: purple">path</span>
                </div>
                <div style="font-size: small">
                    <span style="color: green; font-style: italic"></span>
                </div>
            </td>
            <td>
            </td>
            <td>
                <div>The explicit executable or pathname for the pm2 executable.</div>
            </td>
        </tr>
        <tr>
            <td>
                <b>file</b>
                <div style="font-size: small">
                    <span style="color: purple">path</span>
                </div>
                <div style="font-size: small">
                    <span style="color: green; font-style: italic"></span>
                </div>
            </td>
            <td>
            </td>
            <td>
                <div>The path to the process script file.</div>
            </td>
        </tr>
        <tr>
            <td>
                <b>name</b>
                <div style="font-size: small">
                    <span style="color: purple">string</span>/<span style="color: red">required</span>
                </div>
                <div style="font-size: small">
                    <span style="color: green; font-style: italic"></span>
                </div>
            </td>
            <td>
            </td>
            <td>
                <div>The name of the process.</div>
                <div>If this option is set to *, the module will match all processes.</div>
            </td>
        </tr>
        <tr>
            <td>
                <b>state</b>
                <div style="font-size: small">
                    <span style="color: purple">string</span>
                </div>
                <div style="font-size: small">
                    <span style="color: green; font-style: italic"></span>
                </div>
            </td>
            <td>
                <ul style="margin: 0; padding: 0">
                    <b>Choices:</b>
                    <li>deleted</li>
                    <li>reloaded</li>
                    <li>restarted</li>
                    <li><div style="color: blue"><b>started</b>&nbsp;&larr;</div></li>
                    <li>stopped</li>
                </ul>
            </td>
            <td>
                <div>The state of the process.</div>
            </td>
        </tr>
    </table>



Attributes
----------

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th>Attribute</th>
            <th>Support</th>
            <th width="100%">Description</th>
        </tr>
        <tr>
            <td>
                <b>check_mode</b>
            </td>
            <td>
                <b>
                    <span style="color: green">full</span>
                    <span style="color: red"></span>
                </b>
            </td>
            <td>
                Can run in check_mode and return changed status prediction withought modifying target.
            </td>
        </tr>
        <tr>
            <td>
                <b>diff_mode</b>
            </td>
            <td>
                <b>
                    <span style="color: green">full</span>
                    <span style="color: red"></span>
                </b>
            </td>
            <td>
                Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode.
            </td>
        </tr>
        <tr>
            <td>
                <b>platform</b>
            </td>
            <td>
                <b>
                    <span style="color: green">posix</span>
                    <span style="color: red"></span>
                </b>
            </td>
            <td>
                Target OS/families that can be operated against.
            </td>
        </tr>
    </table>



Examples
--------

.. code-block:: yaml+jinja

    - name: Make sure PM2 example process is running
      just1not2.pm2.pm2_process:
        name: example
        file: /path/to/script.py

    - name: Stop PM2 example process, if running
      just1not2.pm2.pm2_process:
        name: example
        state: stopped

    - name: Restart all PM2 processes
      just1not2.pm2.pm2_process:
        name: "*"
        state: restarted



Return Values
-------------

This module has no return value.



Status
------

Authors
~~~~~~~

- Justin Béra (@just1not2)
