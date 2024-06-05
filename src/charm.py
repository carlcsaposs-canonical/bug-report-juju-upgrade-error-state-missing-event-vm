#!/usr/bin/env python3
# Copyright 2024 Ubuntu
# See LICENSE file for licensing details.
#
# Learn more at: https://juju.is/docs/sdk

"""Charm the service.

Refer to the following tutorial that will help you
develop a new k8s charm using the Operator Framework:

https://juju.is/docs/sdk/create-a-minimal-kubernetes-charm
"""

import logging

import ops

logger = logging.getLogger(__name__)


class FooCharm(ops.CharmBase):
    """Charm the service."""

    def __init__(self, *args):
        super().__init__(*args)
        self.framework.observe(self.on.install, self._on_event)
        self.framework.observe(self.on.config_changed, self._on_event)
        self.framework.observe(self.on.leader_elected, self._on_event)
        self.framework.observe(self.on.leader_settings_changed, self._on_event)
        self.framework.observe(self.on.start, self._on_event)
        self.framework.observe(self.on.update_status, self._on_event)
        self.framework.observe(self.on.upgrade_charm, self._on_event)
        self.framework.observe(self.on.stop, self._on_event)
        self.framework.observe(self.on.remove, self._on_event)

    def _on_event(self, event: ops.EventBase):
        logger.info(f"Event: {type(event)}")

if __name__ == "__main__":  # pragma: nocover
    ops.main(FooCharm)  # type: ignore
