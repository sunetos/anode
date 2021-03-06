#!/usr/bin/env python

__author__ = 'Adam R. Smith'
__license__ = 'Apache 2.0'

from anode.util.config import Config
from anode.core.object import AnodeObjectRegistry

# Note: do we really want to do the res folder like this again?
conf_paths = ['res/config/anode.yml', 'res/config/anode.local.yml']
CONF = Config(conf_paths).data

obj_registry = AnodeObjectRegistry()
obj_registry.register_yaml_dir('obj', ['ion.yml'], ['services'])

# Make a default factory for AnodeObjects
AnodeObject = obj_registry.new

svc_registry = AnodeObjectRegistry()
svc_registry.register_yaml_dir('obj/services')
