""" Common functions to exchange path locations
"""


from __future__ import annotations

from pathlib import Path

#----------------- GENERAL FUNCTIONS
#----------------- function to build the folder

#----------------- function to get the DynamicEvaluation folder path

def get_folder_path() -> Path:
    """Get the path to the DynamicEvaluation folder

    Returns:
        Path: The path to the DynamicEvaluation folder
    """
    return Path.home() / "DynamicEvaluation"

def create_folder() -> Path:
    """Create a folder in the user directory

    Returns:
        Path: The path to the created folder
    """
    folder_path = get_folder_path()
    folder_path.mkdir(parents=True, exist_ok=True)
    return folder_path

#----------------- function to build and save the eval_start file

def save_start_file(logfile_path:   str | Path) -> Path:
    """Create a start file for the evaluation

    Args:
        logfile_path: The path where the logfile
        of the evaluation should be saved

    Returns:
        Path: The path to the created start file
    """
    eval_start_file = create_folder() / "start_eval.txt"
    eval_start_file.write_text(str(logfile_path), encoding="utf-8")
    return eval_start_file

#----------------- function to check existence of eval_start file

def check_for_file() -> bool:
    """Check if the eval_start file exists

    Returns:
        bool: True if the eval_start file exists, False otherwise
    """
    eval_start_file = get_folder_path() / "start_eval.txt"
    return eval_start_file.is_file()

#----------------- function to read the eval_start file

def read_start_file() -> Path:
    """Read the eval_start file to find out the location
        of the logfile for the evaluation

    Returns:
        Path: The path to the logfile for the evaluation
    Raises:
        FileNotFoundError: if the start file is not found
    """
    eval_start_file = get_folder_path() / "start_eval.txt"
    if not eval_start_file.is_file():
        raise FileNotFoundError(f"Start file not found at {eval_start_file}.")

    logfile_path = eval_start_file.read_text(encoding="utf-8").strip()
    logfile_path = Path(logfile_path)

    return logfile_path

#----------------- function to delete the eval folder and its content

def delete_folder() -> bool:
    """Delete the DynamicEvaluation folder and its content

    Returns:
        bool: True if the folder was deleted, False otherwise
    """
    folder_path = get_folder_path()
    eval_start_file = folder_path / "start_eval.txt"

    if eval_start_file.is_file():
        eval_start_file.unlink()

    if folder_path.exists() and folder_path.is_dir():
        try:
            folder_path.rmdir()
            return True
        except OSError:
            # The folder is not empty, so we cannot delete it
            return False

    return False

