""" Script for Dynamic Evaluation App
"""


import os
import subprocess
import sys

import BaseScriptObject as ScriptObject
import NemAll_Python_AllplanSettings as AllplanSettings

from BuildingElement import BuildingElement
from CreateElementResult import CreateElementResult
from ScriptObjectInteractors.MultiElementSelectInteractor import MultiElementSelectInteractorResult

from . import AllplanEventHooks
from .gui_classes.PathFunctions import PathFunctions


def check_allplan_version(build_ele:    BuildingElement,
                          version:      str) ->bool:
    """Check the current Allplan version

    Args:
        build_ele: the building element.
        version:   the current Allplan version

    Returns:
        True/False if version is supported by this script
    """

    # Delete unused arguments
    del (version, build_ele)


    # Support all versions
    return True

def create_script_object(build_ele         : BuildingElement,
                         script_object_data: ScriptObject.BaseScriptObjectData) -> ScriptObject.BaseScriptObject:
    """ Creation of the script object

    Args:
        build_ele:          building element with the parameter properties
        script_object_data: script object data

    Returns:
        created script object
    """
    dynamic_evaluation = DynamicEvalApp(build_ele, script_object_data)

    return dynamic_evaluation

class DynamicEvalApp (ScriptObject.BaseScriptObject):

    """ Definition of class DynamicEvalApp with which it is
        possible to start an external GUI window for the
        dynamic evaluation of all date currently visible in
        the open drawing files in Allplan
    """

    def __init__(self
                 , build_ele:           BuildingElement
                 , script_object_data:  ScriptObject.BaseScriptObjectData):

        """ Class for the starting of the dynamic evaluation
            REMARK: currently not needed as ScriptObject but implemented
            to maybe later also allow evaluation of selected elements

        Args:
            build_ele: the building element
            script_object_data: tool package of the script object
        """

        super().__init__(script_object_data)
        self.build_ele = build_ele
        self.ctrl_prop_util = script_object_data.control_props_util
        self.doc = self.document

        self.selection_mode = ""
        self.calc_objects = MultiElementSelectInteractorResult()
        self.script_object_interactor = None


    def modify_element_property(self
                                , name:     str
                                , value:    str)   ->bool:

        """ modify the element properties

        Args:
            name: name of the modified value
            value: modified value
        Returns:
            update the property palette

        """

        del (name, value)
        return True


    def on_control_event(self
                         , event_id: int) -> bool:

        """ Handles on control event

        Args:
            event_id: event id of the clicked button control

        Returns:
            True if palette refresh is necessary, False otherwise
        """

        build_ele = self.build_ele

        local_str_table, _ = build_ele.get_string_tables()
        start_eval_message = local_str_table.get_string("2001", "Start the Dynamic Evaluation App")


        if event_id == 1000:
            self.create_path_file()

            dyn_eval_path = os.path.join(AllplanSettings.AllplanPaths.GetStdPath(),
                                        "PythonPartsScripts", "allplan_gmbh", "DynamicEvaluation", "gui_classes", "GUIWindow.py")
            #dyn_eval_path = r"C:\Daten\Git\standalone-interface\gui_classes\GuiWindow.py"

            print(f"{dyn_eval_path} is the path to the GUIWindow.py file")

            python = f"{AllplanSettings.AllplanPaths.GetPrgPath()}\\Python\\python.exe"

            startupinfo              = subprocess.STARTUPINFO()
            startupinfo.dwFlags     |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow  = subprocess.SW_HIDE

            subprocess.Popen(f"{python} \"{dyn_eval_path}\" {sys.path}",    # pylint: disable=consider-using-with
                                           creationflags=subprocess.CREATE_NO_WINDOW)

            print("GUI started.")

        else:
            print("unknown event id ", event_id)

        del start_eval_message

        return True


    def start_next_input(self):

        """ stops the script object interactor and
            executes the script

        """

        self.script_object_interactor = None


    def create_path_file(self) -> bool:

        """ method to save the selected folder path
            of the log file for the dynamic evaluation in a text file
            to access it in the event hooks for the logging process

        Returns:
            text file with the path for the log file in the Users folder
        """

        logfile_path = self.build_ele.eval_file_path.value

        PathFunctions.save_start_file(logfile_path)
        AllplanEventHooks.read_all_visible_objects(self.doc)

        return True


    def execute(self) -> CreateElementResult:

        """Function for the element creation

        Returns:
            created element result
        """

        return CreateElementResult()
