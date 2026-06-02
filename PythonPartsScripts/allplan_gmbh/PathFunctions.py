""" Common functions to exchange path locations
"""


from __future__ import annotations

from pathlib import Path

#----------------- GENERAL FUNCTIONS
#----------------- function to build the folder

def create_folder() -> Path:
    """Create a folder in the user directory

    Returns:
        Path: The path to the created folder
    """
    user_dir = Path.home()
    folder_path = user_dir / "DynamicEvaluation"
    folder_path.mkdir(parents=True, exist_ok=True)
    return folder_path

#----------------- function to build and save the eval_start file

def save_start_file(logfile_path:   str) -> Path:
    """Create a start file for the evaluation

    Args:
        logfile_path: The path where the logfile
        of the evaluation should be saved

    Returns:
        Path: The path to the created start file
    """
    eval_start_file = create_folder() / "start_eval.txt"
    eval_start_file.write_text(logfile_path, encoding="utf-8")
    return eval_start_file

#----------------- function to read the eval_start file

def read_start_file() -> Path:
    """Read the eval_start file to find out the location
        of the logfile for the evaluation

    Returns:
        Path: The path to the logfile for the evaluation
    Raises:
        FileNotFoundError: if the start file is not found
    """
    eval_start_file = create_folder() / "start_eval.txt"
    if not eval_start_file.exists():
        raise FileNotFoundError(f"Start file not found at {eval_start_file}.")

    logfile_path = eval_start_file.read_text(encoding="utf-8").strip()

    return logfile_path
