"""data models that can be connected to QTableViews"""

import ast
import random

from collections import defaultdict
from pathlib import Path
from typing import Literal

import openpyxl
import openpyxl.styles as excel_styles
import openpyxl.utils as excel_utils
import PySide6.QtGui as PyGui

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt


def aggregat_param_file(param_lines:        list[dict]
                        , key_attrib:       str
                        , quantity_attrib:  str) -> tuple[list[list], list[str]]:

    volume_attrib_set = {"Volume", "VOB_Volume", "Net volume", "Gross volume"
                         "Volumen", "VOB_Volumen", "Nettovolumen", "Bruttovolumen"}
    area_attrib_set = {"Area", "Floor_surface", "Base_area"
                    , "Vertical_Surface", "VOB_Area", "Ceiling_Surface"
                    , "Net floor surface", "Surface"
                    , "Fläche", "Bodenfläche", "Grundfläche"
                    , "Seitenfläche", "VOB_Fläche", "Deckenfläche"
                    , "Bodenfläche netto", "Oberfläche"}
    length_attrib_set = {"Length", "Height", "VOB_Length", "Absolute_length"
                            , "Absolute_height", "Clear_height"
                            , "Länge", "Höhe", "VOB_Länge", "Länge_absolut"
                            , "Höhe_absolut", "Lichte_Höhe"}
    piece_attrib_set = {"Factor", "Faktor", "Piece", "Anzahl", "Count"}

    if quantity_attrib in ["Volume", "Volumen"]:
        quantity_set = volume_attrib_set
    elif quantity_attrib in ["Area", "Fläche"]:
        quantity_set = area_attrib_set
    elif quantity_attrib in ["Length", "Länge"]:
        quantity_set = length_attrib_set
    elif quantity_attrib in ["Piece", "Stück", "Anzahl"]:
        quantity_set = piece_attrib_set
    else:
        quantity_set = {quantity_attrib}

    key_value_dict = defaultdict(float)
    for single_line in param_lines:
        if key_attrib not in single_line.keys():
            continue

        quantity_key = quantity_set.intersection(single_line.keys())
        if not quantity_key:
            continue

        dict_key = single_line[key_attrib]
        if dict_key in ("", "<undefined>"):
            dict_key = "not specified"
        quantity_value = single_line[next(iter(quantity_key))]


        if not isinstance(quantity_value, (int, float)) or isinstance(quantity_value, bool):
            continue

        key_value_dict[dict_key] += quantity_value

    sorted_line_list = sorted(key_value_dict.items(), key = lambda table_line: table_line[0])
    color_list = [get_random_color() for line in range(len(sorted_line_list))]
    table_lines = [[sorted_line[0], sorted_line[1], color] for sorted_line
                   , color in zip(sorted_line_list, color_list)]
    table_headers = [key_attrib, quantity_attrib, "Color"]

    return (table_lines, table_headers)


def aggregat_sorted_file(param_lines:        list[dict]
                        , key_attrib:       str
                        , quantity_attrib:  str
                        , sorting_attrib:   str = None) -> tuple[list[list], list[str]]:

    volume_attrib_set = {"Volume", "VOB_Volume", "Net volume", "Gross volume"
                         "Volumen", "VOB_Volumen", "Nettovolumen", "Bruttovolumen"}
    area_attrib_set = {"Area", "Floor_surface", "Base_area"
                    , "Vertical_Surface", "VOB_Area", "Ceiling_Surface"
                    , "Net floor surface", "Surface"
                    , "Fläche", "Bodenfläche", "Grundfläche"
                    , "Seitenfläche", "VOB_Fläche", "Deckenfläche"
                    , "Bodenfläche netto", "Oberfläche"}
    length_attrib_set = {"Length", "Height", "VOB_Length", "Absolute_length"
                            , "Absolute_height", "Clear_height"
                            , "Länge", "Höhe", "VOB_Länge", "Länge_absolut"
                            , "Höhe_absolut", "Lichte_Höhe"}
    piece_attrib_set = {"Factor", "Faktor", "Piece", "Anzahl", "Count"}

    if quantity_attrib in ["Volume", "Volumen"]:
        quantity_set = volume_attrib_set
    elif quantity_attrib in ["Area", "Fläche"]:
        quantity_set = area_attrib_set
    elif quantity_attrib in ["Length", "Länge"]:
        quantity_set = length_attrib_set
    elif quantity_attrib in ["Piece", "Stück", "Anzahl"]:
        quantity_set = piece_attrib_set
    else:
        quantity_set = {quantity_attrib}

    key_value_dict = defaultdict(float)
    sorting_quantity_dict = defaultdict(lambda: defaultdict(float))
    for single_line in param_lines:
        if key_attrib not in single_line.keys():
            continue

        quantity_key = quantity_set.intersection(single_line.keys())
        if not quantity_key:
            continue

        dict_key = single_line[key_attrib]
        if dict_key in ("", "<undefined>"):
            dict_key = "not specified"
        quantity_value = single_line[next(iter(quantity_key))]

        if not isinstance(quantity_value, (int, float)) or isinstance(quantity_value, bool):
            continue

        if sorting_attrib:
            if sorting_attrib not in single_line.keys() or single_line[sorting_attrib] in ("", "<undefined>"):
                sorting_value = "unknown"
            else:
                sorting_value = single_line[sorting_attrib]
            sorting_quantity_dict[dict_key][sorting_value] += quantity_value
            

        key_value_dict[dict_key] += quantity_value

    sorted_line_list = sorted(key_value_dict.items(), key = lambda table_line: table_line[0])

    table_lines = []
    sorting_value_color_dict = {}
    current_dict_key = ""
    for dict_key_name, total_key_quantity in sorted_line_list:
        detailed_sorting_dict = dict(sorting_quantity_dict[dict_key_name])
        
        for sorting_value_name, sorting_value_quantity in sorted(detailed_sorting_dict.items()
                                                                 , key = lambda item: str(item[0])):
            if sorting_value_name not in sorting_value_color_dict.keys():
                sorting_value_color_dict[sorting_value_name] = get_random_color()
                
            sorting_value_color = sorting_value_color_dict[sorting_value_name]
            if dict_key_name != current_dict_key:
                table_lines.append([dict_key_name, total_key_quantity, sorting_value_name
                                    , sorting_value_quantity, sorting_value_color])
            else:
                table_lines.append(["", "", sorting_value_name, sorting_value_quantity, sorting_value_color])
            current_dict_key = dict_key_name
        


    
    if sorting_attrib:
        table_headers = [key_attrib, quantity_attrib, sorting_attrib
                         , f"{quantity_attrib} ({sorting_attrib})", "Color"]
    else:
        table_headers = [key_attrib, quantity_attrib, "Color"]


    return (table_lines, table_headers)


def convert_to_numeric(param_value: str):
    try:
        return int(param_value)
    except ValueError:
        try:
            return float(param_value)
        except ValueError:
            return param_value
        
def get_random_color() -> tuple[int, int, int]:
    red_part = random.randint(0, 255)
    green_part = random.randint(0, 255)
    blue_part = random.randint(0, 255)
    rgb_color = (red_part, green_part, blue_part)
    return rgb_color


def read_param_file(file_path: str | Path) -> list[dict]:
    table_line_list = []
    with open(file_path, "r", encoding = "utf-8") as param_file:
        param_lines = param_file.readlines()
    for line_content in param_lines:
        line_content = line_content.strip()
        if not line_content:
            continue
        attrib_pair_set = ast.literal_eval(line_content)
        attrib_pair_dict = dict(attrib_pair_set)
        table_line_list.append(attrib_pair_dict)

    return table_line_list

def create_table_style (cell_color:   str
                        , border_color: str
                        , border_style: str
                        , font_size:    int
                        , font_weight:  bool = False
                        , style_name:   Literal["header", "body", "footer"] = "body") -> excel_styles.NamedStyle:
        
    table_style = excel_styles.NamedStyle(name = style_name)
    table_style.font = excel_styles.Font(size = font_size, bold = font_weight)
    if style_name == "header":
        table_style.fill = excel_styles.PatternFill(fill_type = "solid", start_color = cell_color)
        
        table_style.border = excel_styles.Border(
            left = excel_styles.Side(border_style = border_style, color = border_color),
            right = excel_styles.Side(border_style = border_style, color = border_color),
            top = excel_styles.Side(border_style = border_style, color = border_color),
            bottom = excel_styles.Side(border_style = border_style, color = border_color)
        )
    else:
        table_style.border = excel_styles.Border(
            left = excel_styles.Side(border_style = border_style, color = border_color),
            right = excel_styles.Side(border_style = border_style, color = border_color)
        )
        
    table_style.alignment = excel_styles.Alignment(horizontal = "center", vertical = "center"
                                                   , shrink_to_fit = False)

    return table_style


class MainTableModel(QAbstractTableModel):

    def __init__(self
                 , row_content: list
                 , header_naming: list):
        super().__init__()
        self.row_content = row_content
        self.header_naming = header_naming

    def rowCount(self
                    , model_parent: QModelIndex = QModelIndex()) -> int:
        return len(self.row_content)

    def columnCount (self
                     , model_parent: QModelIndex = QModelIndex()) -> int:
        return len(self.row_content[0] if self.row_content else [])

    def data (self
                   , cell_index: QModelIndex
                   , model_role: int = Qt.DisplayRole):
        curr_row = cell_index.row()
        curr_column = cell_index.column()

        value =  self.row_content[curr_row][curr_column]
        
        if model_role == Qt.DisplayRole:
            if isinstance(value, tuple) and len(value) == 3:
                return None
            if isinstance(value, (str, int, float, bool)):
                return value
            return str(value)
        if model_role == Qt.BackgroundRole:
            if isinstance(value, tuple) and len(value) == 3:
                cell_color = PyGui.QColor(value[0], value[1], value[2])
                return cell_color
        return None

    def headerData(self
                   , count_index: int
                   , row_or_cell: Qt.Orientation
                   , model_role: int = Qt.DisplayRole):
        if model_role != Qt.DisplayRole:
            return None
        if row_or_cell == Qt.Horizontal:
            return self.header_naming[count_index]
        return None
   