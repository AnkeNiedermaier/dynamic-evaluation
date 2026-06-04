""" Script for Diagram Window
"""

import csv
import math
import os
import subprocess
import sys
import textwrap
import tkinter as tk

from tkinter import filedialog

import BaseScriptObject as ScriptObject
import matplotlib
import matplotlib.pyplot as MatPlt
import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_BaseElements as AllplanBaseElements
import NemAll_Python_BasisElements as AllplanBasisElements
import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_IFW_ElementAdapter as AllplanElementAdapter
import NemAll_Python_Utility as AllplanUtil
import numpy
import openpyxl
import PathFunctions

from BuildingElement import BuildingElement
from ControlPropertiesUtil import ControlPropertiesUtil
from CreateElementResult import CreateElementResult
from DocumentManager import DocumentManager
from matplotlib import ticker
from ScriptObjectInteractors.MultiElementSelectInteractor import MultiElementSelectInteractor, MultiElementSelectInteractorResult
from StringTableService import StringTableService


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
    diagram_creator = DiagramCreator(build_ele, script_object_data)

    return diagram_creator

class DiagramCreator (ScriptObject.BaseScriptObject):

    """ Class to deal with the SOM Attribute requirements in Allplan

        Args:
            build_ele: the building element
            script_object_data: tool package of the script object
    """

    def __init__(self
                 , build_ele:           BuildingElement
                 , script_object_data:  ScriptObject.BaseScriptObjectData):
        super().__init__(script_object_data)
        self.build_ele = build_ele
        self.ctrl_prop_util = script_object_data.control_props_util
        self.doc = self.document

        self.selection_mode = ""
        self.calc_objects = MultiElementSelectInteractorResult()

        self.excel_file_path = ""
        self.name_list_y = []
        self.value_list_x = []
        self.name_value_dict = {}
        self.selection_mode = ""



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
        attrib_assign_message = local_str_table.get_string("2001", "Show the Diagram!")


        if event_id == 1000:
            #self.create_diagram()
            #self.create_value_dict()
            #self.show_diagram()
            self.create_path_file()
            eval_script = r"C:\Daten\Git\standalone-interface\gui_classes\GuiWindow.py"

            # Use Python 3.13 with PySide6
            python_exe = r"C:\Users\aniedermaier\AppData\Local\Programs\Python\Python313\pythonw.exe"

            subprocess.Popen(
                [python_exe, eval_script],
                cwd=os.path.dirname(eval_script),
            )
            print("GUI started.")




        else:
            print("unknown event id ", event_id)

        return True




    def start_next_input(self):

        self.script_object_interactor = None


    def create_path_file(self):
        logfile_path = self.build_ele.eval_file_path.value

        PathFunctions.save_start_file(logfile_path)


    def execute(self) -> CreateElementResult:

        """Function for the element creation

        Returns:
            created element result
        """

        return CreateElementResult()

