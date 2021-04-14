from enum import Enum


class ExportFormat(str, Enum):
    DOCKER = "docker"
    PEX = "pex"
    ZIP = "zip"
