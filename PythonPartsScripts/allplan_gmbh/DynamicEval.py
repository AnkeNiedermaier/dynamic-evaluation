""" Script for Diagram Window
"""

import csv
import math
import os
import subprocess
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
            self.create_diagram()
            #self.create_value_dict()
            #self.show_diagram()
            print("Return value = " ,  attrib_assign_message)

        if event_id == 2000:
            self.selection_mode = "eval_objects"
            self.script_object_interactor = MultiElementSelectInteractor(interactor_result = self.calc_objects
                                                                         , prompt_msg= "Objekte wählen")
            self.script_object_interactor.start_input(self.coord_input)


        else:
            print("unknown event id ", event_id)

        return True

    def create_value_dict(self):

        build_ele = self.build_ele
        doc = self.document

        name_value_dict = {}


    #----------------- Extract palette parameter values

        key_id = build_ele.key_attrib.value
        amount_id = build_ele.amount_attrib.value

    #----------------- select relevant objects


        rel_objects = self.calc_objects.sel_elements

        for single_object in rel_objects:

            object_attrib_list = AllplanBaseElements.ElementsAttributeService.GetAttributes(single_object)

            object_attrib_dict = {attrib_name : attrib_value for attrib_name
                                  , attrib_value in object_attrib_list}

            if key_id in object_attrib_dict.keys() and amount_id in object_attrib_dict.keys():
                key_value = object_attrib_dict.get(key_id)
                amount_value = object_attrib_dict.get(amount_id)
                if key_value in ["", None, 0]:
                    key_value = "varied"
                if amount_value in ["", None, 0]:
                    amount_value = 0.00


                if key_value in name_value_dict.keys():
                    current_amount = name_value_dict.get(key_value)
                    new_amount = current_amount + amount_value
                else:
                    new_amount = amount_value
                name_value_dict[key_value] = new_amount

        name_list_y = name_value_dict.keys()
        value_list_x = name_value_dict.values()
        name_value_list = name_value_dict.items()

        self.name_value_dict = name_value_dict
        self.name_list_y = name_list_y
        self.value_list_x = value_list_x

        return True

    def start_next_input(self):

        self.script_object_interactor = None

    def show_diagram(self):

        build_ele = self.build_ele
        doc = self.document

    #----------------- Extract palette parameter values

        key_id = build_ele.key_attrib.value
        amount_id = build_ele.amount_attrib.value

        key_string = AllplanBaseElements.AttributeService.GetAttributeName(doc, key_id)
        amount_string = AllplanBaseElements.AttributeService.GetAttributeName(doc, amount_id)

        value_items = self.value_list_x
        name_items = self.name_list_y
        title_name = f"{amount_string} per {key_string}"

        canvas_compl, ind_diagram = MatPlt.subplots(nrows = 2, ncols = 1)

        canvas_compl.suptitle("Whole diagram")

        ind_diagram[0].pie(value_items, labels = name_items, shadow = False, labeldistance = 0.4)

        ind_diagram[0].set_title(label = title_name, loc = "center", fontsize = 10)

        ind_diagram[0].legend(title = key_string, loc = "upper left", fontsize = 9, bbox_to_anchor=(1, 0, 0.5, 1))

        ind_diagram[1].pie(value_items, labels = name_items, shadow = False, labeldistance = 0.4)
        ind_diagram[1].legend(title = key_string, loc = "upper left", fontsize = 9, bbox_to_anchor=(1, 0, 0.5, 1))
        ind_diagram[1].set_title(label = title_name, loc = "center", fontsize = 10)

        MatPlt.show()


    def create_diagram(self):
        materials = ["concrete as a long word", "wood", "C25/30", "steel"]
        material_lable = [textwrap.fill(single_lable, 12) for single_lable in materials]
        object_types = ["beam", "wall", "column", "slab", "box"]
        indiv_object_dict = {123:("concrete as a long word", "beam", 5.80, 6, 4.09)
                            , 345:("concrete as a long word", "slab", 2.80, 3, 1.09)
                            , 678:("steel", "box", 34.80, 12, 2.09)
                            , 901:("concrete as a long word", "slab", 31.80, 3, 1.09)
                            , 446:("C25/30", "wall", 4.80, 12, 2.09)
                            , 348:("steel", "slab", 2.80, 3, 1.09)
                            , 670:("wood", "box", 34.80, 12, 2.09)
                            , 900:("concrete as a long word", "wall", 31.80, 3, 1.09)
                            , 444:("C25/30", "column", 4.80, 12, 2.09)}
        material_object_dict = {}
        for single_obj in object_types:
            material_object_dict[single_obj] = {mat_name: 0.00 for mat_name in materials}

        for item_values in indiv_object_dict.values():
            type_key = item_values[1]
            mat_dict = material_object_dict.get(type_key)
            mat_value = item_values[0]
            object_ecco_value = mat_dict.get(mat_value)
            ecco_value = item_values[2]
            mat_dict[mat_value] = object_ecco_value + ecco_value
            material_object_dict[type_key] = mat_dict

        material_per_object = {}
        for object_typename in material_object_dict.keys():
            object_material_list = []
            object_materials = material_object_dict.get(object_typename)
            for material_name_string in object_materials.keys():
                material_value = object_materials.get(material_name_string)
                object_material_list.append(material_value)
            material_per_object[object_typename] = object_material_list


        # material_label = numpy.arange(len(materials))
        # col_width = 0.25
        # col_place = 0

        # for oject_name, material_gwp in material_per_object.items():
        #     col_offset = col_width * col_place
        #     MatPlt.bar(material_label + col_offset, material_gwp, col_width, label = oject_name)

        #     col_place += 1

        # MatPlt.xticks(material_label + col_width, materials)

        canvas_compl, ind_diagram = MatPlt.subplots(nrows = 2, ncols = 1, figsize = (12, 6))
        col_width = 0.80
        start_offset = numpy.zeros(len(materials))

        for oject_name, material_gwp in material_per_object.items():
            bar_lable = []
            for object_gwp in material_gwp:
                if object_gwp == 0.00:
                    object_lable = ""
                else:
                    object_lable = f"{object_gwp:.3f} CO²"
                bar_lable.append(object_lable)

            obj_bar = ind_diagram[0].bar(x = material_lable, height = material_gwp, width = col_width, bottom = start_offset, label = oject_name)
            start_offset += material_gwp

            ind_diagram[0].bar_label(obj_bar, labels = bar_lable, label_type = "center", fontsize = 9)
        ind_diagram[0].yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.3f}"))
        ind_diagram[0].legend(title = "Objects", loc = "upper left", fontsize = 9, bbox_to_anchor=(1, 0, 0.5, 1))
        ind_diagram[0].spines["top"].set_visible(False)
        ind_diagram[0].spines["right"].set_visible(False)
        ind_diagram[0].set_ylabel("CO²")
        ind_diagram[0].grid(axis = "y")



        MatPlt.show()



    def execute(self) -> CreateElementResult:

        """Function for the element creation

        Returns:
            created element result
        """

        return CreateElementResult()

