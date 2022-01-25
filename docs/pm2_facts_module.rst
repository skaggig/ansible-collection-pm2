.. _just1not2.pm2.pm2_facts:


***********************
just1not2.pm2.pm2_facts
***********************

**Return PM2 information as fact data**


*New in version 1.0:* of just1not2.pm2

.. contents::
   :local:
   :depth: 1



Synopsis
--------

- Return PM2 information as fact data for PM2 process management.



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
                    <span style="color: green"></span>
                    <span style="color: red">none</span>
                </b>
            </td>
            <td>
                Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode.
            </td>
        </tr>
        <tr>
            <td>
                <b>facts</b>
            </td>
            <td>
                <b>
                    <span style="color: green">full</span>
                    <span style="color: red"></span>
                </b>
            </td>
            <td>
                Action returns an ansible_facts dictionary that will update existing host facts.
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

    - name: Populate PM2 facts
      just1not2.pm2.pm2_facts:

    - name: Print PM2 facts
      ansible.builtin.debug:
        var: ansible_facts.pm2



Return Values
-------------

Facts returned by this module are added/updated in the hostvars host facts and can be referenced by name just like any other host fact. They do not need to be registered in order to use them.

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="4">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
        <tr>
            <td colspan="4">
                <b>pm2</b>
                <div style="font-size: small">
                    <span style="color: purple">dictionary</span>
                </div>
                <div style="font-size: small">
                    <span style="color: green; font-style: italic"></span>
                </div>
            </td>
            <td>success</td>
            <td>
                <div>Information about PM2.</div>
                <br/>
                <div style="font-size: smaller"><b></b></div>
                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;"></div>
            </td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;</td>
            <td colspan="3">
                <b>executable</b>
                <div style="font-size: small">
                    <span style="color: purple">string</span>
                </div>
                <div style="font-size: small">
                    <span style="color: green; font-style: italic"></span>
                </div>
            </td>
            <td>success</td>
            <td>
                <div>The explicit executable or pathname for the PM2 executable.</div>
                <div style="font-size: smaller"><b>Sample:</b></div>
                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">"/usr/local/bin/pm2"</div>
            </td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;</td>
            <td colspan="3">
                <b>processes</b>
                <div style="font-size: small">
                    <span style="color: purple">list</span>/<span style="color: purple">elements=dictionary</span>
                <div style="font-size: small">
                    <span style="color: green; font-style: italic"></span>
                </div>
                </div>
            </td>
            <td>success</td>
            <td>
                <div>The list of PM2 processes.</div>
            </td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;</td>
            <td>&nbsp;&nbsp;</td>
            <td colspan="2">
                <b>cwd</b>
                <div style="font-size: small">
                    <span style="color: purple">string</span>
                </div>
                <div style="font-size: small">
                    <span style="color: green; font-style: italic">added in 1.2</span>
                </div>
            </td>
            <td>success</td>
            <td>
                <div>The path to the directory from which the script runs.</div>
                <div style="font-size: smaller"><b>Sample:</b></div>
                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">"/home/user"</div>
            </td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;</td>
            <td>&nbsp;&nbsp;</td>
            <td colspan="2">
                <b>file</b>
                <div style="font-size: small">
                    <span style="color: purple">string</span>
                </div>
                <div style="font-size: small">
                    <span style="color: green; font-style: italic"></span>
                </div>
            </td>
            <td>success</td>
            <td>
                <div>The path to the process script file.</div>
                <div style="font-size: smaller"><b>Sample:</b></div>
                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">"/path/to/script.py"</div>
            </td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;</td>
            <td>&nbsp;&nbsp;</td>
            <td colspan="2">
                <b>id</b>
                <div style="font-size: small">
                    <span style="color: purple">integer</span>
                </div>
                <div style="font-size: small">
                    <span style="color: green; font-style: italic"></span>
                </div>
            </td>
            <td>success</td>
            <td>
                <div>The PM2 id of the process.</div>
                <div style="font-size: smaller"><b>Sample:</b></div>
                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">0</div>
            </td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;</td>
            <td>&nbsp;&nbsp;</td>
            <td colspan="2">
                <b>interpreter</b>
                <div style="font-size: small">
                    <span style="color: purple">string</span>
                </div>
                <div style="font-size: small">
                    <span style="color: green; font-style: italic"></span>
                </div>
            </td>
            <td>success</td>
            <td>
                <div>The path to the process script interpreter.</div>
                <div style="font-size: smaller"><b>Sample:</b></div>
                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">"/usr/bin/python3"</div>
            </td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;</td>
            <td>&nbsp;&nbsp;</td>
            <td colspan="2">
                <b>mode</b>
                <div style="font-size: small">
                    <span style="color: purple">string</span>
                </div>
                <div style="font-size: small">
                    <span style="color: green; font-style: italic"></span>
                </div>
            </td>
            <td>success</td>
            <td>
                <div>The PM2 mode of the process.</div>
                <div style="font-size: smaller"><b>Sample:</b></div>
                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">"fork_mode"</div>
            </td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;</td>
            <td>&nbsp;&nbsp;</td>
            <td colspan="2">
                <b>monitor</b>
                <div style="font-size: small">
                    <span style="color: purple">dictionary</span>
                </div>
                <div style="font-size: small">
                    <span style="color: green; font-style: italic"></span>
                </div>
            </td>
            <td>success</td>
            <td>
                <div>The monitoring information about the process.</div>
            </td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;</td>
            <td>&nbsp;&nbsp;</td>
            <td>&nbsp;&nbsp;</td>
            <td colspan="1">
                <b>cpu</b>
                <div style="font-size: small">
                    <span style="color: purple">float</span>
                </div>
                <div style="font-size: small">
                    <span style="color: green; font-style: italic"></span>
                </div>
            </td>
            <td>success</td>
            <td>
                <div>The CPU percentage used by the process.</div>
                <div style="font-size: smaller"><b>Sample:</b></div>
                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">20.7</div>
            </td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;</td>
            <td>&nbsp;&nbsp;</td>
            <td>&nbsp;&nbsp;</td>
            <td colspan="1">
                <b>memory</b>
                <div style="font-size: small">
                    <span style="color: purple">integer</span>
                </div>
                <div style="font-size: small">
                    <span style="color: green; font-style: italic"></span>
                </div>
            </td>
            <td>success</td>
            <td>
                <div>The memory used by the process (in Bytes).</div>
                <div style="font-size: smaller"><b>Sample:</b></div>
                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">6500352</div>
            </td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;</td>
            <td>&nbsp;&nbsp;</td>
            <td>&nbsp;&nbsp;</td>
            <td colspan="1">
                <b>restarts</b>
                <div style="font-size: small">
                    <span style="color: purple">integer</span>
                </div>
                <div style="font-size: small">
                    <span style="color: green; font-style: italic"></span>
                </div>
            </td>
            <td>success</td>
            <td>
                <div>The number of times the process has been restarted.</div>
                <div style="font-size: smaller"><b>Sample:</b></div>
                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">5</div>
            </td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;</td>
            <td>&nbsp;&nbsp;</td>
            <td colspan="2">
                <b>name</b>
                <div style="font-size: small">
                    <span style="color: purple">string</span>
                </div>
                <div style="font-size: small">
                    <span style="color: green; font-style: italic"></span>
                </div>
            </td>
            <td>success</td>
            <td>
                <div>The name of the process.</div>
                <div style="font-size: smaller"><b>Sample:</b></div>
                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">"example"</div>
            </td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;</td>
            <td>&nbsp;&nbsp;</td>
            <td colspan="2">
                <b>namespace</b>
                <div style="font-size: small">
                    <span style="color: purple">string</span>
                </div>
                <div style="font-size: small">
                    <span style="color: green; font-style: italic"></span>
                </div>
            </td>
            <td>success</td>
            <td>
                <div>The namespace of the process.</div>
                <div style="font-size: smaller"><b>Sample:</b></div>
                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">"default"</div>
            </td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;</td>
            <td>&nbsp;&nbsp;</td>
            <td colspan="2">
                <b>pid</b>
                <div style="font-size: small">
                    <span style="color: purple">integer</span>
                </div>
                <div style="font-size: small">
                    <span style="color: green; font-style: italic"></span>
                </div>
            </td>
            <td>success</td>
            <td>
                <div>The process ID (PID).</div>
                <div style="font-size: smaller"><b>Sample:</b></div>
                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">26741</div>
            </td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;</td>
            <td>&nbsp;&nbsp;</td>
            <td colspan="2">
                <b>status</b>
                <div style="font-size: small">
                    <span style="color: purple">string</span>
                </div>
                <div style="font-size: small">
                    <span style="color: green; font-style: italic"></span>
                </div>
            </td>
            <td>success</td>
            <td>
                <div>The status of the process.</div>
                <div style="font-size: smaller"><b>Sample:</b></div>
                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">"online"</div>
            </td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;</td>
            <td colspan="3">
                <b>version</b>
                <div style="font-size: small">
                    <span style="color: purple">string</span>
                </div>
                <div style="font-size: small">
                    <span style="color: green; font-style: italic"></span>
                </div>
            </td>
            <td>success</td>
            <td>
                <div>The version of the PM2 executable used.</div>
                <div style="font-size: smaller"><b>Sample:</b></div>
                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">"5.1.2"</div>
            </td>
        </tr>
    </table>



Status
------

Authors
~~~~~~~

- Justin Béra (@just1not2)
