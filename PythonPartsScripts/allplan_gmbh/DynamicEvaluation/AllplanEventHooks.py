""" implementation of the hooks for the Allplan events to log elements modifications
"""

import datetime
import os

from getpass import getuser
from pathlib import Path
from typing import Any

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter

from NemAll_Python_BaseElements import AttributeService, ElementsSelectService, eAttibuteReadState

from . import PathFunctions

""" Constants for logging"""

""" implementation of the hooks for the Allplan events to log elements modifications
"""

def execute_event(event_id: int,
                  *args   : Any):
    """Executes the event with the given ID and arguments.
    Args:
        event_id: Event ID of the clicked button control.
        *args: Arguments for the event.
    """
    match event_id:
        case AllplanSettings.PythonEventHooks.ePostAllplanStart:
            # Clear temp log on Allplan start and update path for logging
            read_all_visible_objects(args[0])
        case AllplanSettings.PythonEventHooks.ePreAllplanClose:
            # Flush temp log to final log before saving drawing files
            read_all_visible_objects(args[0])
        case AllplanSettings.PythonEventHooks.ePostDrawingFilesLoad:
            # Flush temp log to final log before loading drawing files
            read_all_visible_objects(args[0])
        case AllplanSettings.PythonEventHooks.ePreDrawingFilesSave:
            # Flush temp log to final log before saving drawing files
            read_all_visible_objects(args[0])
        case AllplanSettings.PythonEventHooks.ePostProjectLoad:
            # Update path for logging
            read_all_visible_objects(args[0])
        case AllplanSettings.PythonEventHooks.ePreProjectClose:
            # Flush temp log to final log before saving drawing files
            read_all_visible_objects(args[0])
        case AllplanSettings.PythonEventHooks.ePostDocumentUpdate:
            # Write modified and deleted elements to temporary log
            read_all_visible_objects(args[0])
        case AllplanSettings.PythonEventHooks.eMoveElementToDifferentDF:
            # Write modified and deleted elements to temporary log
            read_all_visible_objects(args[0])
        case _:
            pass

def read_all_visible_objects(_doc: AllplanEleAdapter.DocumentAdapter):

    leftout_attrib_number_list = [5, 6, 7, 10, 12, 45, 50, 94, 110, 111, 113,114, 115, 118
                           , 141, 161, 162, 163, 164, 165, 166, 171, 180, 190
                           , 191, 334, 335, 345, 346, 347, 349, 538, 539, 600
                           , 683, 1317, 1318, 1319]
    leftout_attrib_name_list = [AttributeService.GetAttributeName(_doc, attrib_number)
                                for attrib_number in leftout_attrib_number_list]
    leftout_object_list = [22, 23, 24, 25, 27, 28, 35, 36, 41, 42, 43, 44, 45, 51, 67, 68, 71, 72, 89, 95, 97, 98
                           , 102, 112, 150, 254, 970, 973, 985, 1022, 1094, 1095, 1096, 1097]

    all_elems = ElementsSelectService.SelectAllElements(_doc)
    elem_attrib_list = []
    for elem in all_elems:

        attrib_dict = {attrib_id:attrib_value for attrib_id, attrib_value
                       in elem.GetAttributes(eAttibuteReadState.ReadAll)}

        object_id = attrib_dict.get(12)
        if object_id in leftout_object_list:
            continue


        elem_attrib_dict = {(AttributeService.GetAttributeName(_doc, attrib_name)
                            ,attrib_value) for attrib_name, attrib_value
                            in elem.GetAttributes(eAttibuteReadState.ReadAll)
                            if attrib_name not in leftout_attrib_number_list}
        if elem_attrib_dict:

            elem_attrib_list.append(elem_attrib_dict)

    file_name = PathFunctions.read_start_file()
    with open(file_name, "w", encoding="utf-8") as log_file:
        for elem_attrib_dict in elem_attrib_list:
            log_file.write(str(elem_attrib_dict) + "\n")
