"""Explicit references for reviewed dead code false positives."""

from pyrig.rig.configs.base.config_file import ConfigFile

from pyrig_badge.rig.configs.docs.badge import BadgeConfigFile

_CONFIG_FILE_OVERRIDES = (
    ConfigFile._configs,  # noqa: SLF001
    ConfigFile._dump,  # noqa: SLF001
    ConfigFile._load,  # noqa: SLF001
    ConfigFile.extension,
    ConfigFile.stem,
)
_CONFIG_FILES = (BadgeConfigFile,)
