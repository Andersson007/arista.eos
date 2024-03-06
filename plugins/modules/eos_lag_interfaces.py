#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for eos_lag_interfaces
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type


DOCUMENTATION = """
module: eos_lag_interfaces
short_description: LAG interfaces resource module
description: This module manages attributes of link aggregation groups on Arista EOS
  devices.
version_added: 1.0.0
author: Nathaniel Case (@Qalthos)
notes:
- Tested against Arista EOS 4.24.6F
- This module works with connection C(network_cli). See the L(EOS Platform Options,../network/user_guide/platform_eos.html).
options:
  config:
    description: A list of link aggregation group configurations.
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - Name of the port-channel interface of the link aggregation group (LAG) e.g.,
          Port-Channel5.
        type: str
        required: true
      members:
        description:
        - Ethernet interfaces that are part of the group.
        type: list
        elements: dict
        suboptions:
          member:
            description:
            - Name of ethernet interface that is a member of the LAG.
            type: str
          mode:
            description:
            - LAG mode for this interface.
            type: str
            choices:
            - 'active'
            - 'on'
            - 'passive'
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the EOS device by
      executing the command B(show running-config | section interfaces).
    - The state I(parsed) reads the configuration from C(running_config) option and
      transforms it into Ansible structured data as per the resource module's argspec
      and the value is then returned in the I(parsed) key within the result.
    type: str
  state:
    description:
    - The state of the configuration after module completion.
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    - rendered
    - gathered
    - parsed
    default: merged

"""

EXAMPLES = """

# Using merged

# Before state:
# -------------
#
# veos#show running-config | section interface
# interface Ethernet1
#   channel-group 5 mode on
# interface Ethernet2

- name: Merge provided LAG attributes with existing device configuration
  arista.eos.eos_lag_interfaces:
    config:
      - name: Port-Channel5
        members:
          - member: Ethernet2
            mode: "on"
    state: merged

# After state:
# ------------
#
# veos#show running-config | section interface
# interface Ethernet1
#   channel-group 5 mode on
# interface Ethernet2
#   channel-group 5 mode on


# Using replaced

# Before state:
# -------------
#
# veos#show running-config | section interface
# interface Ethernet1
#   channel-group 5 mode on
# interface Ethernet2

- name: Replace all device configuration of specified LAGs with provided configuration
  arista.eos.eos_lag_interfaces:
    config:
      - name: Port-Channel5
        members:
          - member: Ethernet2
            mode: "on"
    state: replaced

# After state:
# ------------
#
# veos#show running-config | section interface
# interface Ethernet1
# interface Ethernet2
#   channel-group 5 mode on


# Using overridden

# Before state:
# -------------
#
# veos#show running-config | section interface
# interface Ethernet1
#   channel-group 5 mode on
# interface Ethernet2

- name: Override all device configuration of all LAG attributes with provided configuration
  arista.eos.eos_lag_interfaces:
    config:
      - name: Port-Channel10
        members:
          - member: Ethernet2
            mode: "on"
    state: overridden

# After state:
# ------------
#
# veos#show running-config | section interface
# interface Ethernet1
# interface Ethernet2
#   channel-group 10 mode on


# Using deleted

# Before state:
# -------------
#
# veos#show running-config | section interface
# interface Ethernet1
#   channel-group 5 mode on
# interface Ethernet2
#   channel-group 5 mode on

- name: Delete LAG attributes of the given interfaces.
  arista.eos.eos_lag_interfaces:
    config:
      - name: Port-Channel5
        members:
          - member: Ethernet1
    state: deleted

# After state:
# ------------
#
# veos#show running-config | section interface
# interface Ethernet1
# interface Ethernet2
#   channel-group 5 mode on

# Using parsed:

# parsed.cfg
# interface Ethernet1
#   channel-group 5 mode on
# interface Ethernet2
#   channel-group 5 mode on

- name: Use parsed to convert native configs to structured data
  arista.eos.lag_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Output:
#   parsed:
#     - name: Port-Channel5
#       members:
#         - member: Ethernet2
#           mode: "on"
#         - member: Ethernet1
#           mode: "on"

# using rendered:

- name: Use Rendered to convert the structured data to native config
  arista.eos.eos_lag_interfaces:
    config:
      - name: Port-Channel5
        members:
          - member: Ethernet2
            mode: "on"
          - member: Ethernet1
            mode: "on"
    state: rendered
# -----------
# Output
# -----------
#
# rendered:

# interface Ethernet1
#   channel-group 5 mode on
# interface Ethernet2
#   channel-group 5 mode on


# Using gathered:

# native config:
# interface Ethernet1
#   channel-group 5 mode on
# interface Ethernet2
#   channel-group 5 mode on

- name: Gather lldp_global facts from the device
  arista.eos.lldp_global:
    state: gathered

# Output:
#   gathered:
#     - name: Port-Channel5
#       members:
#         - member: Ethernet2
#           mode: on
#         - member: Ethernet1
#           mode: on
"""

RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule

from ansible_collections.arista.eos.plugins.module_utils.network.eos.argspec.lag_interfaces.lag_interfaces import (
    Lag_interfacesArgs,
)
from ansible_collections.arista.eos.plugins.module_utils.network.eos.config.lag_interfaces.lag_interfaces import (
    Lag_interfaces,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "overridden", ("config",)),
        ("state", "rendered", ("config",)),
        ("state", "parsed", ("running_config",)),
    ]
    mutually_exclusive = [("config", "running_config")]
    module = AnsibleModule(
        argument_spec=Lag_interfacesArgs.argument_spec,
        required_if=required_if,
        supports_check_mode=True,
        mutually_exclusive=mutually_exclusive,
    )

    result = Lag_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
