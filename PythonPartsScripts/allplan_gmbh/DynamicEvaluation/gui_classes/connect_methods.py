"""classes for different methods as connections to widgets"""

import os

from typing import Literal

import PySide6.QtWidgets as PyWidget


#----------------- sample functions for widget connections
#----------------- function to show a trace message
def press_message():
    """ function to show a trace message
    """
    print("You clicked the button!!")

#----------------- function for a pop-up window

def show_message():

    """ function to show a message box with a greeting to the current user
    """
    curr_user = os.environ.get("USERNAME")
    message_box = PyWidget.QMessageBox(PyWidget.QMessageBox.Icon.Information
                                       , "Greeting", f"Hello again {curr_user}!"
                                       , PyWidget.QMessageBox.StandardButton.Cancel)
    message_box.setObjectName("pop_up")
    message_box.setWindowTitle("Greetings")
    message_box.resize(400, 300)
    message_box.exec()

#----------------- function to open a dialog window

def menu_action_dialog(parent_app: PyWidget.QWidget | None = None
                     , action_kind: Literal["open_snapshot"
                                            , "save_snapshot"
                                            , "save_table"
                                            , "save_diagram"] = "open_snapshot") -> str | None:
    """ function to open a dialog window

    Args:
        parent_app: the parent application window
        action_kind: the menu item used

    Returns:
        either the selected file path or None for other action kinds
    """


    file_dialog = PyWidget.QFileDialog()
    if action_kind == "open_snapshot":
        file_dialog.setFileMode(PyWidget.QFileDialog.FileMode.ExistingFile)
        file_dialog.setWindowTitle("Open snapshot file")
        file_dialog.setNameFilter("Text files (*.txt)")
    else:
        file_dialog.setAcceptMode(PyWidget.QFileDialog.AcceptMode.AcceptSave)
        if action_kind == "save_snapshot":
            file_dialog.setWindowTitle("Save snapshot file")
            file_dialog.setNameFilter("Text files (*.txt)")
            file_dialog.setDefaultSuffix("txt")

        elif action_kind == "save_table":
            file_dialog.setWindowTitle("Export table as Excel file")
            file_dialog.setNameFilter("Excel files (*.xlsx)")
        else:
            file_dialog.setWindowTitle("Export diagram as image")
            file_dialog.setNameFilter("PNG files (*.png);;JPEG files (*.jpg);;All files (*.*)")
    if file_dialog.exec():
        selected_file_list = file_dialog.selectedFiles()
        if selected_file_list:
            print(f"You selected the file: {selected_file_list[0]}")
            return selected_file_list[0]
    return None
