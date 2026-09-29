import logging
from pathlib import Path


logger = logging.getLogger(__name__)


def inspect_file(filepath_str):

    filepath = Path(filepath_str) # TODO 1

    if not filepath.is_file():
        logger.error(f"File not found") 
        raise FileNotFoundError("File is not found") #TODO 2

    return {"name": filepath.name, "extension":filepath.suffix}


    """Return basic information about an existing file."""
    # TODO 1: Create a Path object. (Check)

    # TODO 2: If the path is not a file:
    #         Log an ERROR message.
    #         Raise FileNotFoundError (e.g. file not found).

    # TODO 3: Return a dictionary containing:
    #         name and extension.
    


def inspect_extension(file_info):

    if file_info["extension"] != ".txt":
        logger.error(f"Unsupported file: {file_info['extension']}")
        raise ValueError("Unsupported file") #TODO 4

    return file_info #TODO 5


    """Confirm that the file uses a supported text extension."""
    supported_extension = ".txt"

    # TODO 4: If file_info["extension"] does not equal
    #         supported_extension:
    #         Log an ERROR message (e.g. unsupported format).
    #         Raise ValueError.

    # TODO 5: Return file_info.
    