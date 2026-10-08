"""Explicit references for reviewed dead code false positives."""

from pyrig.rig.configs.base.config_file import ConfigFile
from pyrig.rig.configs.base.string_ import StringConfigFile

from pyrig_badge.rig.configs.docs.badge import BadgeConfigFile

_CONFIG_FILE_OVERRIDES = (
    ConfigFile._configs,  # noqa: SLF001
    ConfigFile.extension,
    ConfigFile.stem,
    StringConfigFile.content,
)
_CONFIG_FILES = (BadgeConfigFile,)
