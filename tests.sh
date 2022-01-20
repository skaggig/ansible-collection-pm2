#!/bin/bash

# Copyright: (c) 2022, Justin Béra (@just1not2) <me@just1not2.org>
# GNU General Public License v3.0+ (see LICENCE or https://www.gnu.org/licenses/gpl-3.0.txt)


# Installs pip requirements
pip install -r ./tests/requirements.txt

# Runs Ansible sanity tests
ansible-test sanity
