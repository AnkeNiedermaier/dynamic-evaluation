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

# from . import PathFunctions


def execute_event(event_id: int,
                  *args   : Any):
    """Executes the event with the given ID and arguments.
    Args:
        event_id: Event ID of the clicked button control.
        *args: Arguments for the event.
    """
    match event_id:
        case AllplanSettings.PythonEventHooks.ePostAllplanStart:
            # if all drawing files are loaded after start of Allplan
            read_all_visible_objects(args[0])
        case AllplanSettings.PythonEventHooks.ePreAllplanClose:
            # the last state of the drawing files before closing Allplan
            read_all_visible_objects(args[0])
        case AllplanSettings.PythonEventHooks.ePostDrawingFilesLoad:
            # the current state of drawing files when the BWS dialog is opended
            read_all_visible_objects(args[0])
        case AllplanSettings.PythonEventHooks.ePreDrawingFilesSave:
            # the last state of the drawing files before saving drawing files
            read_all_visible_objects(args[0])
        case AllplanSettings.PythonEventHooks.ePostProjectLoad:
            # the current state of drawing files when the project selection dialog is opened
            read_all_visible_objects(args[0])
        case AllplanSettings.PythonEventHooks.ePreProjectClose:
            # the last state of the drawing files before closing the project
            read_all_visible_objects(args[0])
        case AllplanSettings.PythonEventHooks.ePostDocumentUpdate:
            # the current state of the drawing files after a document update or save
            read_all_visible_objects(args[0])
        case AllplanSettings.PythonEventHooks.eMoveElementToDifferentDF:
            # the current state of the drawing files after moving an element to a different drawing file
            read_all_visible_objects(args[0])
        case _:
            pass

def read_all_visible_objects(_doc: AllplanEleAdapter.DocumentAdapter):

    """ Reads all visible elementsin the current loaded drawing files
        filters them by the layer status and their type to eliminate
        usless objects and wirtes their attributes as dict with attribute
        and value to a log file that is the basis for dynamic evaluation
    Args:
        _doc: Document adapter for the current loaded drawing files
    """

    leftout_attrib_number_list = [5, 6, 7, 10, 12, 45, 50, 94, 110, 111, 113,114, 115, 118
                           , 141, 161, 162, 163, 164, 165, 166, 171, 180, 190
                           , 191, 334, 335, 345, 346, 347, 349, 538, 539, 600
                           , 683, 1317, 1318, 1319]
    leftout_attrib_name_list = [AttributeService.GetAttributeName(_doc, attrib_number)
                                for attrib_number in leftout_attrib_number_list]
    relevant_object_list = ["Volume3D_TypeUUID", "Cylinder3D_TypeUUID", "Sphere3D_TypeUUID"
                            , "BRep3D_Volume_TypeUUID", "BRep3D_Surface_TypeUUID", "BRep3D_Wire_TypeUUID"
                            , "SmartSymbol_TypeUUID", "OutdoorFacilitiesObject_TypeUUID", "DeliverySymbol_TypeUUID"
                            , "FixtureDefinition_TypeUUID", "DynamicGroupFixture_TypeUUID"
                            , "LandscapingPathFloorSurface_TypeUUID", "LandscapingPathBaseboard_TypeUUID"
                            , "LandscapingPlantsFloorSurface_TypeUUID", "LandscapingPlantsBaseboard_TypeUUID"
                            , "UrbanPlanningPlotFloorSurface_TypeUUID", "UrbanPlanningBuilding_TypeUUID"
                            , "UrbanPlanningDrawingFloorSurface_TypeUUID", "WallTier_TypeUUID", "CircularWallTier_TypeUUID"
                            , "ElementWallTier_TypeUUID", "PolygonWallTier_TypeUUID"
                            , "Upstand_TypeUUID", "LineUpstand_TypeUUID", "CircularUpstand_TypeUUID"
                            , "ElementUpstand_TypeUUID", "PolygonUpstand_TypeUUID", "LineUpstandTier_TypeUUID"
                            , "CircularUpstandTier_TypeUUID", "ElementUpstandTier_TypeUUID"
                            , "Slab_TypeUUID", "Column_TypeUUID", "Beam_TypeUUID", "InstallationComponent_TypeUUID"
                            , "PolyInstallationComponent_TypeUUID", "Chimney_TypeUUID", "BuildingSolid_TypeUUID"
                            , "DemolitionSolid_TypeUUID", "UserDefinedSolid_TypeUUID"
                            , "StripFoundation_TypeUUID", "IndividualFoundation_TypeUUID", "Any3DFoundation_TypeUUID"
                            , "SlabFoundationTier_TypeUUID"
                            , "Stairs_TypeUUID", "StairsStraightFlight_TypeUUID", "StairsHalfTurn_TypeUUID"
                            , "StairsWinder_TypeUUID", "StairsDoubleQuarterTurn_TypeUUID", "StairsTripleQuarterTurn_TypeUUID"
                            , "StairsSpiral_TypeUUID", "StairsUType_TypeUUID", "StairsQuarterLanding_TypeUUID"
                            , "StairsDoubleQuarterLanding_TypeUUID", "StairModeler_TypeUUID"
                            , "Room_TypeUUID", "RoomGroup_TypeUUID", "ArchitectureFloorSurface_TypeUUID"
                            , "ArchitectureVerticalSurface_TypeUUID", "ArchitectureCeilingSurface_TypeUUID"
                            , "ArchitectureBaseboard_TypeUUID", "FloorSurface_TypeUUID", "VerticalSurface_TypeUUID"
                            , "CeilingSurface_TypeUUID", "Baseboard_TypeUUID", "Storey_TypeUUID", "StoreyGroup_TypeUUID"
                            , "Rafter_TypeUUID", "RafterPlaced_TypeUUID", "RafterPurlin_TypeUUID"
                            , "HipRafter_TypeUUID", "Header_TypeUUID", "Purlin_TypeUUID", "CollarBeam_TypeUUID"
                            , "CollarTie_TypeUUID", "Post_TypeUUID", "ValleyRafter_TypeUUID", "JoistPlaced_TypeUUID"
                            , "Timber_TypeUUID", "RoofCovering_TypeUUID", "Skylight_TypeUUID"
                            , "BarsLinearPlacement_TypeUUID", "BarsLinearMultiPlacement_TypeUUID"
                            , "BarsAreaPlacement_TypeUUID", "BarsSpiralPlacement_TypeUUID", "BarsCircularPlacement_TypeUUID"
                            , "BarsRotationalSolidPlacement_TypeUUID", "BarsRotationalPlacement_TypeUUID"
                            , "BarsTangentionalPlacement_TypeUUID", "BarsEndBendingPlacement_TypeUUID"
                            , "MeshPlacement_TypeUUID", "MeshAreaPlacement_TypeUUID", "ReinforcementGroup_TypeUUID"
                            , "ReinforcementFFUnit_TypeUUID", "ReinforcementStampPoint_TypeUUID"
                            , "ReinforcementStructuralStarterBars_TypeUUID", "ReinforcementExtrudeRebarAlongPath_TypeUUID"
                            , "ReinforcementSweepBarsAlongPath_TypeUUID", "ReinforcementPlaceBarsAlongSurface_TypeUUID"
                            , "ParapetSmartSymbol_TypeUUID", "SubFacade_TypeUUID"
                            , "SlabOpeningSmartSymbol_TypeUUID"
                            , "SlabRecessSmartSymbol_TypeUUID", "SkylightSmartSymbol_TypeUUID"
                            , "SubRail_TypeUUID"
                            , "SubCeilingSystem_TypeUUID", "CeilingSystemSmartSymbol_TypeUUID"
                            , "PointFixture_TypeUUID", "LineFixture_TypeUUID", "PlaneFixture_TypeUUID"
                            , "GeneralGroupFixture_TypeUUID", "CadastralPointFixture_TypeUUID"
                            , "CadastralLineFixture_TypeUUID", "CadastralPlaneFixture_TypeUUID", "CadastralGeneralGroupFixture_TypeUUID"
                            , "SmartPart_TypeUUID"
                            , "DoorOpeningSmartPart_TypeUUID", "WindowOpeningSmartPart_TypeUUID", "SillSmartPart_TypeUUID"
                            , "SolarScreenSmartPart_TypeUUID", "EquipmentSmartPart_TypeUUID", "LightdomeSmartPart_TypeUUID"
                            , "RoofWindowSmartPart_TypeUUID", "PointBuiltInElementSmartPart_TypeUUID"
                            , "ReinforcementRobotSmartPart_TypeUUID", "PythonPart_TypeUUID"
                            , "PipeWork_TypeUUID", "PipeBundle_TypeUUID"
                            , "OpeningPart_TypeUUID", "OpeningPartWindow_TypeUUID", "OpeningPartDoor_TypeUUID"
                            , "SkeletonGrid_TypeUUID", "SkeletonColumn_TypeUUID", "SkeletonBeam_TypeUUID"
                            , "SkeletonBrace_TypeUUID", "SkeletonPurlin_TypeUUID", "SkeletonPortalFrame_TypeUUID"
                            , "SkeletonSolidElementSystem_TypeUUID"]

    if not check_for_file():
        return

    all_elems = ElementsSelectService.SelectAllElements(_doc)
    elem_attrib_list = []
    for single_elem in all_elems:

        if single_elem.IsInActiveLayer() is False:
            continue

        object_type = single_elem.GetElementAdapterType().GetTypeName()
        if object_type not in relevant_object_list:
            continue


        elem_attrib_dict = {(AttributeService.GetAttributeName(_doc, attrib_name)
                            ,attrib_value) for attrib_name, attrib_value
                            in single_elem.GetAttributes(eAttibuteReadState.ReadAll)
                            if attrib_name not in leftout_attrib_number_list}
        if elem_attrib_dict:

            elem_attrib_list.append(elem_attrib_dict)



    file_name = read_start_file()
    with open(file_name, "w", encoding="utf-8") as log_file:
        for elem_attrib_dict in elem_attrib_list:
            log_file.write(str(elem_attrib_dict) + "\n")


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
