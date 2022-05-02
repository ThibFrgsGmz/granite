# Standard includes
# OS module provides functions for interacting with the operating system
import os
from pathlib import Path


DEFAULT_FILE_LOCATION = "default_file"


class OutputFileWrapper():
    """
    Class to gather the operations common to the output files of the application.
    """

    def __init__(self, filename = None, format = None ):
        """Initialize the object instance

        Parameters
        ----------
        filename:
            Name of the file
        format:
            Format of the file
        """

        if not filename:
            print(
                f"No file location given. Using default '{DEFAULT_FILE_LOCATION}'. Overwriting existing file."
            )

            self.filename = Path(DEFAULT_FILE_LOCATION).resolve()
            self.default_filename_on_use = True
        else:
            self.filename = Path(filename + format).resolve()
            self.default_filename_on_use = False

        self.document = open(f"{self.filename}", "w+")
        

    def __del__(self):
        self.document.close()