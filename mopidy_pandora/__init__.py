from __future__ import unicode_literals

import logging
import os

from mopidy import config, ext


__version__ = '0.1.3'

logger = logging.getLogger(__name__)


class Extension(ext.Extension):

    dist_name = 'Mopidy-Pandora'
    ext_name = 'pandora'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(Extension, self).get_config_schema()
        schema['api_host'] = config.String(optional=True)
        schema['partner_encryption_key'] = config.String()
        schema['partner_decryption_key'] = config.String()
        schema['partner_username'] = config.String()
        schema['partner_password'] = config.String()
        schema['partner_device'] = config.String()
        schema['username'] = config.String()
        schema['password'] = config.Secret()
        schema['preferred_audio_quality'] = config.String(optional=True, choices=['lowQuality', 'mediumQuality',
                                                                                  'highQuality'])
        schema['sort_order'] = config.String(optional=True, choices=['date', 'A-Z', 'a-z'])
        return schema

    def setup(self, registry):
        from .actor import PandoraBackend
        registry.add('backend', PandoraBackend)
