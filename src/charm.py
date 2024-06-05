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

if __name__ == "__main__":  # pragma: nocover
    ops.main(FooCharm)  # type: ignore
