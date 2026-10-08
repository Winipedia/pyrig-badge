"""Configuration management for the project's README.md file."""

from pyrig.rig.configs.readme import ReadmeConfigFile as BaseReadmeConfigFile

from pyrig_badge.rig.configs.base.badges import BadgesConfigFile


class ReadmeConfigFile(BadgesConfigFile, BaseReadmeConfigFile):
    """Generate the project README with the configured logo and badges."""
