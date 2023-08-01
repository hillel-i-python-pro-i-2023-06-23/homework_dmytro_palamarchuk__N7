"""Config for homework module"""

import pathlib
from typing import Final

ROOT_DIR: Final[pathlib.Path] = pathlib.Path(__file__).parents[1]
FILES_INPUT_DIR: Final[pathlib.Path] = ROOT_DIR.joinpath("files_input")
FILES_OUTPUT_DIR: Final[pathlib.Path] = ROOT_DIR.joinpath("files_output")

# LOGGER
LOGS_DIR: Final[pathlib.Path] = ROOT_DIR.joinpath("logs")
LOGS_FILE_APP = "app.logs"
