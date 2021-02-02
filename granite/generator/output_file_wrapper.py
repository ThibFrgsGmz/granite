# Standard includes
# OS module provides functions for interacting with the operating system
import os
from pathlib import Path


DEFAULT_FILE_LOCATION = "default_file"


class OutputFileWrapper():
    """
    ...
    """

    def __init__(self, filename=None, format = None ):
        """
        Initialize the object instance
        """

        if not filename:
            print("No file location given. Using default '{}'."" Overwriting existing file.".format(DEFAULT_FILE_LOCATION) )
            self.filename = Path(DEFAULT_FILE_LOCATION).resolve()
            self.default_filename_on_use = True
        elif isinstance(filename, Path):
            self.filename = filename
            self.default_filename_on_use = False
        else:
            self.filename = Path(filename).resolve()
            self.default_filename_on_use = False

        if self.filename.is_dir():
            self.filename.mkdir(exist_ok=True)

            print("Given path is directory without filename, using default filename.")
            # self.filename.joinpath(DEFAULT_FILE_LOCATION, ".h")
            self.filename = os.path.join(self.filename, DEFAULT_FILE_LOCATION + format)

        self.document = open(f"{self.filename}", "w+")

    def __del__(self):
        self.document.close()