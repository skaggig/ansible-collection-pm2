# PM2 Ansible Collection

The Parallel Multithreaded Machine (PM2) Ansible collection includes Ansible modules to help the management of PM2 processes.

This collection has been tested against following PM2 versions: **>=4.2.0**.


## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.10.0**.

Plugins and modules within a collection may be tested with only specific Ansible versions.
A collection may contain metadata that identifies these versions.
PEP440 is the schema used to describe the versions of Ansible.


## Included content

### Modules
Name | Description
--- | ---
[just1not2.pm2.pm2_facts](./docs/pm2_facts_module.rst)|Return PM2 information as fact data
[just1not2.pm2.pm2_process](./docs/pm2_process_module.rst)|Manage PM2 processes


## Installing this collection

You can install the PM2 collection with the Ansible Galaxy CLI:

    ansible-galaxy collection install just1not2.pm2

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: just1not2.pm2
```


## Using this collection

You can either call modules by their Fully Qualified Collection Namespace (FQCN), such as `just1not2.pm2.pm2_facts`, or you can call modules by their short name if you list the `just1not2.pm2` collection in the playbook's collections keyword:

```yaml
---
  - name: Populate PM2 facts
    just1not2.pm2.pm2_facts:

  - name: Print the list of PM2 processes
    debug:
      var: ansible_facts.pm2.processes

  - name: Make sure PM2 example process is running
    just1not2.pm2.pm2_process:
      name: example
      file: /path/to/script.py
      state: started
```


## See Also

* [PM2 official documentation](https://doc.pm2.io)
* [Ansible Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details


## Contributing to this collection

This collection started as personal project, but I welcome community contributions to this collection. If you find problems, please open an issue or create a PR against the [PM2 collection repository](https://github.com/just1not2/ansible-collection-pm2).

You can also reach me by email at `me@just1not2.org`.


## Licensing

GNU General Public License v3.0 or later.

See [LICENSE](./LICENCE) to see the full text.


## Author Information

This collection was created in 2022 by Justin Béra.
