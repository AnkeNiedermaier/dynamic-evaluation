"""classes for different methods as connections to widgets"""

import os

from typing import Literal

import PySide6.QtWidgets as PyWidget


#----------------- sample methods for widget connections
#----------------- method to show a trace message
def press_message():
    print("You clicked the button!!")
    
#----------------- method for a pop-up window
    
def show_message():
    curr_user = os.environ.get("USERNAME")
    message_box = PyWidget.QMessageBox(PyWidget.QMessageBox.Icon.Information
                                       , "Greeting", f"Hello again {curr_user}!"
                                       , PyWidget.QMessageBox.StandardButton.Cancel)
    message_box.setObjectName("pop_up")
    message_box.setWindowTitle("Greetings")
    message_box.resize(400, 300)
    message_box.exec()
    
def menu_action_dialog(parent_app = None
                     , action_kind: Literal["open_new"
                                          , "save_table", "save_diagram"] = "open_new") -> str | None:
    file_dialog = PyWidget.QFileDialog()
    if action_kind == "open_new":
        file_dialog.setFileMode(PyWidget.QFileDialog.FileMode.ExistingFile)
        file_dialog.setWindowTitle("Open evaluation file")       
        file_dialog.setNameFilter("Text files (*.txt)")
    else:
        file_dialog.setAcceptMode(PyWidget.QFileDialog.AcceptMode.AcceptSave)
        if action_kind == "save_table":
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
