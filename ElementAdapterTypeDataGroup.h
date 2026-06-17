/// \file    ElementAdapterTypeDataGroup.h
///
/// \brief   Definition of the general element adapter type data
///
/// \author  Horst Hohmann
/// \date    09.02.2016
//-----------------------------------------------------------------------------

#pragma once

#include "NemAll_IFW_ElementAdapter\ElementAdapterModelTypeUUIDs.h"
#include "NemAll_IFW_ElementAdapter\ElementAdapterTypeGroup.h"
#include <set>

    using GroupPair = std::pair<GUID, std::set<ElementAdapterTypeGroup>>;

    using TG = ElementAdapterTypeGroup;


    //----------------- Type-UUID , Type group

    static std::initializer_list<GroupPair> s_GroupTypeData = 
    {
        {GroupPair(NULL_TypeUUID(),            {TG::NO_GROUP})},
        {GroupPair(Undefined_TypeUUID(),       {TG::NO_GROUP})},
        {GroupPair(InternalElement_TypeUUID(), {TG::NO_GROUP})},


        //----------------- 2D elements
        
        {GroupPair(Point2D_TypeUUID(),           {TG::NO_GROUP})},
        {GroupPair(Line2D_TypeUUID(),            {TG::NO_GROUP})},
        {GroupPair(Polyline2D_TypeUUID(),        {TG::NO_GROUP})},
        {GroupPair(TextPointer_TypeUUID(),       {TG::NO_GROUP})},
        {GroupPair(Circle2D_TypeUUID(),          {TG::NO_GROUP})},
        {GroupPair(Ellipse2D_TypeUUID(),         {TG::NO_GROUP})},
        {GroupPair(Spline2D_TypeUUID(),          {TG::NO_GROUP})},
        {GroupPair(Clothoid2D_TypeUUID(),        {TG::NO_GROUP})},
        {GroupPair(Chain2D_TypeUUID(),           {TG::NO_GROUP})},
        {GroupPair(Chain2DStationing_TypeUUID(), {TG::NO_GROUP})},
        {GroupPair(Chain2DText_TypeUUID(),       {TG::TEXT_GROUP})},
        {GroupPair(Chain2DParallel_TypeUUID(),   {TG::NO_GROUP})},
        {GroupPair(RevisionCloud_TypeUUID(),     {TG::NO_GROUP})},
        {GroupPair(PointSymbol2D_TypeUUID(),     {TG::NO_GROUP})},
        {GroupPair(PointSymbol3D_TypeUUID(),     {TG::NO_GROUP})},
        {GroupPair(ElementGroup_TypeUUID(),      {TG::NO_GROUP})},
        {GroupPair(SmartFit2D_TypeUUID(),        {TG::NO_GROUP})},
        {GroupPair(Slope_TypeUUID(),             {TG::NO_GROUP})},
        {GroupPair(ExtendedElement_TypeUUID(),   {TG::NO_GROUP})},
        {GroupPair(FillLine_TypeUUID(),          {TG::NO_GROUP})},
        {GroupPair(Link_TypeUUID(),              {TG::NO_GROUP})},
        {GroupPair(OLEElement_TypeUUID(),        {TG::NO_GROUP})},
        {GroupPair(ElementNumber_TypeUUID(),     {TG::TEXT_GROUP})},
        {GroupPair(ClippingPath_TypeUUID(),      {TG::NO_GROUP})},
        {GroupPair(ClippingPathBody_TypeUUID(),  {TG::NO_GROUP})},
        {GroupPair(ClippingPathText_TypeUUID(),  {TG::NO_GROUP})},
        {GroupPair(ClippingPathRepresentation_TypeUUID(),      {TG::NO_GROUP})},
        {GroupPair(LineSupport_TypeUUID(),       {TG::NO_GROUP})},


        //----------------- Object manager

        {GroupPair(GeneralObject_TypeUUID(), {TG::NO_GROUP})},
        {GroupPair(SurfaceObject_TypeUUID(), {TG::NO_GROUP})},
        {GroupPair(LineObject_TypeUUID(),    {TG::NO_GROUP})},


        //----------------- Thermal insulation calculation

        {GroupPair(EnvelopingSurface_TypeUUID(), {TG::NO_GROUP})},


        //----------------- XRef

        {GroupPair(XRefDocument_TypeUUID(),             {TG::XREF_GROUP})},
        {GroupPair(XRefDocumentClipped_TypeUUID(),      {TG::XREF_GROUP})},
        {GroupPair(XRefDocumentEmbedded_TypeUUID(),     {TG::XREF_GROUP})},
        {GroupPair(XRefFreeDocument_TypeUUID(),         {TG::XREF_GROUP})},
        {GroupPair(XRefFreeDocumentClipped_TypeUUID(),  {TG::XREF_GROUP})},
        {GroupPair(XRefFreeDocumentEmbedded_TypeUUID(), {TG::XREF_GROUP})},


        //----------------- ProxyObject

        {GroupPair(ProxyObject_TypeUUID(), {TG::NO_GROUP})},


        //----------------- Grid

        {GroupPair(CartesianGrid_TypeUUID(),              {TG::NO_GROUP})},
        {GroupPair(PolarGrid_TypeUUID(),                  {TG::NO_GROUP})},
        {GroupPair(CartesianGridWithDimension_TypeUUID(), {TG::NO_GROUP})},


        //----------------- Dimension lines

        {GroupPair(LinearDimension_TypeUUID(),                        {TG::DIMENSION_GROUP})},
        {GroupPair(ElevationDimension_TypeUUID(),                     {TG::DIMENSION_GROUP})},
        {GroupPair(SAAP_ElevationDimension_TypeUUID(),                {TG::DIMENSION_GROUP})},
        {GroupPair(AbsoluteElevationDimension_TypeUUID(),             {TG::DIMENSION_GROUP})},
        {GroupPair(CurveDimension_TypeUUID(),                         {TG::DIMENSION_GROUP})},
        {GroupPair(AngleDimension_TypeUUID(),                         {TG::DIMENSION_GROUP})},
        {GroupPair(RadiusDimension_TypeUUID(),                        {TG::DIMENSION_GROUP})},
        {GroupPair(ArcDimension_TypeUUID(),                           {TG::DIMENSION_GROUP})},
        {GroupPair(SplineDimension_TypeUUID(),                        {TG::DIMENSION_GROUP})},
        {GroupPair(ClothoidDimension_TypeUUID(),                      {TG::DIMENSION_GROUP})},
        {GroupPair(DimensionText_TypeUUID(),                          {TG::DIMENSION_GROUP})},
        {GroupPair(Associative_LinearDimension_TypeUUID(),            {TG::DIMENSION_GROUP})},
        {GroupPair(Associative_ElevationDimension_TypeUUID(),         {TG::DIMENSION_GROUP})},
        {GroupPair(Associative_AbsoluteElevationDimension_TypeUUID(), {TG::DIMENSION_GROUP})},
        {GroupPair(Associative_RadiusDimension_TypeUUID(),            {TG::DIMENSION_GROUP})},
        {GroupPair(Associative_AngleDimension_TypeUUID(),             {TG::DIMENSION_GROUP})},
        {GroupPair(Associative_CurveDimension_TypeUUID(),             {TG::DIMENSION_GROUP})},

        //----------------- Text

        {GroupPair(TextBlock_TypeUUID(),                {TG::TEXT_GROUP})},
        {GroupPair(GeneralVariableText_TypeUUID(),      {TG::TEXT_GROUP})},
        {GroupPair(GeneralVariableTextBlock_TypeUUID(), {TG::TEXT_GROUP})},
        {GroupPair(MaskText_TypeUUID(),                 {TG::TEXT_GROUP})},
        {GroupPair(CellButton_TypeUUID(),               {TG::TEXT_GROUP})},


        //----------------- Filled areas

        {GroupPair(Hatching2D_TypeUUID(),        {TG::NO_GROUP})},
        {GroupPair(Pattern2D_TypeUUID(),         {TG::NO_GROUP})},
        {GroupPair(Filling2D_TypeUUID(),         {TG::NO_GROUP})},
        {GroupPair(GradientFilling2D_TypeUUID(), {TG::NO_GROUP})},
        {GroupPair(Bitmap_TypeUUID(),            {TG::NO_GROUP})},
        {GroupPair(Facestyle_TypeUUID(),         {TG::NO_GROUP})},
        {GroupPair(ScanelementMono_TypeUUID(),   {TG::NO_GROUP})},
        {GroupPair(ScanelementColor_TypeUUID(),  {TG::NO_GROUP})},


        //----------------- Zoom window  ...

        {GroupPair(ZoomWindow_TypeUUID(), {TG::NO_GROUP})},


        //----------------- 3D elements

        {GroupPair(Line3D_TypeUUID(),                 {TG::LINES3D_GROUP})},
        {GroupPair(Polyline3D_TypeUUID(),             {TG::LINES3D_GROUP})},
        {GroupPair(Area3D_TypeUUID(),                 {TG::LINES3D_GROUP,TG::AREAS3D_GROUP})},
        {GroupPair(Volume3D_TypeUUID(),               {TG::LINES3D_GROUP,TG::AREAS3D_GROUP,TG::VOLUMES3D_GROUP})},
        {GroupPair(MultiLine3D_TypeUUID(),            {TG::NO_GROUP})},
        {GroupPair(MultiLine3DGroup_TypeUUID(),       {TG::NO_GROUP})},
        {GroupPair(EngineeringPathElement_TypeUUID(), {TG::NO_GROUP})},
        {GroupPair(Arc3D_TypeUUID(),                  {TG::CURVES3D_GROUP })},
        {GroupPair(Spline3D_TypeUUID(),               {TG::CURVES3D_GROUP })},
        {GroupPair(BRep3D_Volume_TypeUUID(),          {TG::BREPS3D_GROUP,TG::BREPS3D_SURFACE_GROUP,TG::LINES3D_GROUP,TG::CURVES3D_GROUP,TG::AREAS3D_GROUP,TG::VOLUMES3D_GROUP})},
        {GroupPair(BRep3D_Surface_TypeUUID(),         {TG::BREPS3D_GROUP,TG::BREPS3D_SURFACE_GROUP,TG::LINES3D_GROUP,TG::CURVES3D_GROUP,TG::AREAS3D_GROUP })},
        {GroupPair(BRep3D_Wire_TypeUUID(),            {TG::BREPS3D_GROUP,TG::LINES3D_GROUP,TG::CURVES3D_GROUP})},
        {GroupPair(Cylinder3D_TypeUUID(),             {TG::BREPS3D_GROUP,TG::BREPS3D_SURFACE_GROUP,TG::LINES3D_GROUP,TG::CURVES3D_GROUP,TG::AREAS3D_GROUP,TG::VOLUMES3D_GROUP})},
        {GroupPair(Sphere3D_TypeUUID(),               {TG::BREPS3D_GROUP,TG::BREPS3D_SURFACE_GROUP,TG::LINES3D_GROUP,TG::CURVES3D_GROUP,TG::AREAS3D_GROUP,TG::VOLUMES3D_GROUP})},


        //----------------- Smart symbol,  fixture

        {GroupPair(SmartSymbol_TypeUUID(),              {TG::SMART_SYMBOL_GROUP})},
        {GroupPair(SmartSymbolDefinition_TypeUUID(),    {TG::SMART_SYMBOL_GROUP})},
        {GroupPair(SmartSymbolFoil_TypeUUID(),          {TG::SMART_SYMBOL_GROUP})},
        {GroupPair(SmartSymbolElementGroup_TypeUUID(),  {TG::SMART_SYMBOL_GROUP})},
        {GroupPair(PlantSmartSymbol_TypeUUID(),         {TG::SMART_SYMBOL_GROUP})},
        {GroupPair(OutdoorFacilitiesObject_TypeUUID(),  {TG::SMART_SYMBOL_GROUP})},

        {GroupPair(OleSmartSymbolDefinition_TypeUUID(), {TG::SMART_SYMBOL_GROUP})},
        {GroupPair(DeliverySymbol_TypeUUID(),           {TG::NO_GROUP})},

        {GroupPair(ElementGroupNode_TypeUUID(),         {TG::NO_GROUP})},

        {GroupPair(FixtureDefinition_TypeUUID(),        {TG::FIXTURE_GROUP})},
        {GroupPair(DynamicGroupFixture_TypeUUID(),      {TG::FIXTURE_GROUP})},


        //----------------- DTM

        {GroupPair(DTMArea_TypeUUID(),                {TG::NO_GROUP})},
        {GroupPair(DTMProfile_TypeUUID(),             {TG::NO_GROUP})},
        {GroupPair(DTMElevation_TypeUUID(),           {TG::NO_GROUP})},
        {GroupPair(DTMContourLine_TypeUUID(),         {TG::NO_GROUP})},
        {GroupPair(DTMGrid_TypeUUID(),                {TG::NO_GROUP})},
        {GroupPair(DTMPointSymbol_TypeUUID(),         {TG::NO_GROUP})},
        {GroupPair(DTMPointSymbol3D_TypeUUID(),       {TG::NO_GROUP})},
        {GroupPair(DTMLongitudinalSection_TypeUUID(), {TG::NO_GROUP})},
        {GroupPair(DTMCrossSection_TypeUUID(),        {TG::NO_GROUP})},
        {GroupPair(DTMLine_TypeUUID(),                {TG::NO_GROUP})},


        //----------------- Landscaping

        {GroupPair(LandscapingPathFloorSurface_TypeUUID(),   {TG::NO_GROUP})},
        {GroupPair(LandscapingPathBaseboard_TypeUUID(),      {TG::NO_GROUP})},
        {GroupPair(LandscapingPlantsFloorSurface_TypeUUID(), {TG::NO_GROUP})},
        {GroupPair(LandscapingPlantsBaseboard_TypeUUID(),    {TG::NO_GROUP})},


        //----------------- Urban planning

        {GroupPair(UrbanPlanningPlotFloorSurface_TypeUUID(),    {TG::NO_GROUP})},
        {GroupPair(UrbanPlanningBuilding_TypeUUID(),            {TG::NO_GROUP})},
        {GroupPair(UrbanPlanningDrawingFloorSurface_TypeUUID(), {TG::NO_GROUP})},
        {GroupPair(UrbanPlanningDrawingBaseboard_TypeUUID(),    {TG::NO_GROUP})},

        {GroupPair(UrbanPlanningDrawingObject_TypeUUID(),       {TG::NO_GROUP})},
        {GroupPair(UrbanPlanningSpacingArea_TypeUUID(),         {TG::NO_GROUP})},


        //----------------- Planes

        {GroupPair(DefaultPlane_TypeUUID(),       {TG::NO_GROUP})},
        {GroupPair(PlanePairArea_TypeUUID(),      {TG::NO_GROUP})},
        {GroupPair(MaskingPlane_TypeUUID(),       {TG::NO_GROUP})},
        {GroupPair(ReferenceSurface_TypeUUID(),   {TG::NO_GROUP})},


        //----------------- Walls

        {GroupPair(Wall_TypeUUID(),             {TG::AXIS_ELEMENT_GROUP, TG::HYPERELEMENT_GROUP})},
        {GroupPair(CircularWall_TypeUUID(),     {TG::AXIS_ELEMENT_GROUP, TG::HYPERELEMENT_GROUP})},
        {GroupPair(ElementWall_TypeUUID(),      {TG::AXIS_ELEMENT_GROUP, TG::HYPERELEMENT_GROUP})},
        {GroupPair(PolygonWall_TypeUUID(),      {TG::HYPERELEMENT_GROUP})},
        {GroupPair(ProfileWall_TypeUUID(),      {TG::AXIS_ELEMENT_GROUP, TG::HYPERELEMENT_GROUP})},

        {GroupPair(WallTier_TypeUUID(),         {TG::AXIS_ELEMENT_GROUP, TG::HYPERELEMENT_TIER_GROUP})},
        {GroupPair(CircularWallTier_TypeUUID(), {TG::AXIS_ELEMENT_GROUP, TG::HYPERELEMENT_TIER_GROUP})},
        {GroupPair(ElementWallTier_TypeUUID(),  {TG::AXIS_ELEMENT_GROUP, TG::HYPERELEMENT_TIER_GROUP})},
        {GroupPair(PolygonWallTier_TypeUUID(),  {TG::HYPERELEMENT_TIER_GROUP})},
        {GroupPair(ProfileWallTier_TypeUUID(),  {TG::AXIS_ELEMENT_GROUP, TG::HYPERELEMENT_TIER_GROUP})},

        {GroupPair(WallAxis_TypeUUID(),         {TG::NO_GROUP})},
        {GroupPair(WallAxisLine_TypeUUID(),     {TG::NO_GROUP})},
        {GroupPair(WallAxisPolyline_TypeUUID(), {TG::NO_GROUP})},
        {GroupPair(WallAxisArc_TypeUUID(),      {TG::NO_GROUP})},
        {GroupPair(WallAxisSpline_TypeUUID(),   {TG::NO_GROUP})},
        {GroupPair(WallAxisClothoid_TypeUUID(), {TG::NO_GROUP})},
        {GroupPair(WallAxisChain_TypeUUID(),    {TG::NO_GROUP})},


        //----------------- Upstand, ...

        {GroupPair(Upstand_TypeUUID(),             {TG::AXIS_ELEMENT_GROUP})},
        {GroupPair(LineUpstand_TypeUUID(),         {TG::AXIS_ELEMENT_GROUP, TG::HYPERELEMENT_GROUP})},
        {GroupPair(CircularUpstand_TypeUUID(),     {TG::AXIS_ELEMENT_GROUP, TG::HYPERELEMENT_GROUP})},
        {GroupPair(ElementUpstand_TypeUUID(),      {TG::AXIS_ELEMENT_GROUP, TG::HYPERELEMENT_GROUP})},
        {GroupPair(PolygonUpstand_TypeUUID(),      {TG::AXIS_ELEMENT_GROUP})},

        {GroupPair(LineUpstandTier_TypeUUID(),     {TG::AXIS_ELEMENT_GROUP, TG::HYPERELEMENT_TIER_GROUP})},
        {GroupPair(CircularUpstandTier_TypeUUID(), {TG::AXIS_ELEMENT_GROUP, TG::HYPERELEMENT_TIER_GROUP})},
        {GroupPair(ElementUpstandTier_TypeUUID(),  {TG::AXIS_ELEMENT_GROUP, TG::HYPERELEMENT_TIER_GROUP})},


        //----------------- Slab, column

        {GroupPair(MultiSlab_TypeUUID(),                 {TG::NO_GROUP})},
        {GroupPair(Slab_TypeUUID(),                      {TG::NO_GROUP})},
        {GroupPair(Column_TypeUUID(),                    {TG::NO_GROUP})},
        {GroupPair(Beam_TypeUUID(),                      {TG::AXIS_ELEMENT_GROUP})},
        {GroupPair(BeamPolygonalRecess_TypeUUID(),       {TG::NO_GROUP})},
        {GroupPair(InstallationComponent_TypeUUID(),     {TG::AXIS_ELEMENT_GROUP})},
        {GroupPair(PolyInstallationComponent_TypeUUID(), {TG::NO_GROUP})},
        {GroupPair(Chimney_TypeUUID(),                   {TG::NO_GROUP})},
        {GroupPair(WallInfraction_TypeUUID(),            {TG::NO_GROUP})},

        {GroupPair(BeamPolygonalRecessTier_TypeUUID(),   {TG::NO_GROUP})},

        {GroupPair(BuildingSolid_TypeUUID(),             {TG::NO_GROUP})},
        {GroupPair(DemolitionSolid_TypeUUID(),           {TG::NO_GROUP})},
        {GroupPair(UserDefinedSolid_TypeUUID(),          {TG::NO_GROUP})},
        {GroupPair(UserDefinedSolidOpening_TypeUUID(),   {TG::NO_GROUP})},


        //----------------- Openings

        {GroupPair(WindowDoor_TypeUUID(),           {TG::WALL_OPENING_GROUP})},
        {GroupPair(Window_TypeUUID(),               {TG::WALL_OPENING_GROUP})},
        {GroupPair(CornerWindow_TypeUUID(),         {TG::WALL_OPENING_GROUP})},
        {GroupPair(CornerWindowComposite_TypeUUID(),{TG::WALL_OPENING_GROUP})},
        {GroupPair(Door_TypeUUID(),                 {TG::WALL_OPENING_GROUP})},
        {GroupPair(Niche_TypeUUID(),                {TG::WALL_OPENING_GROUP})},
        {GroupPair(PolygonalNiche_TypeUUID(),       {TG::WALL_OPENING_GROUP})},
        {GroupPair(Recess_TypeUUID(),               {TG::WALL_OPENING_GROUP})},
        {GroupPair(PolygonalRecess_TypeUUID(),      {TG::WALL_OPENING_GROUP})},
        {GroupPair(FlushPier_TypeUUID(),            {TG::NO_GROUP})},
        {GroupPair(Joint_TypeUUID(),                {TG::WALL_OPENING_GROUP})},
        {GroupPair(FacingComposite_TypeUUID(),      {TG::WALL_OPENING_GROUP})},
        {GroupPair(RabbetComposite_TypeUUID(),      {TG::WALL_OPENING_GROUP})},
        {GroupPair(SlabRecess_TypeUUID(),           {TG::NO_GROUP})},
        {GroupPair(SlabOpening_TypeUUID(),          {TG::NO_GROUP})},

        {GroupPair(WindowDoorTier_TypeUUID(),      {TG::WALL_OPENING_GROUP,TG::WALL_OPENING_SUB_ELEMENTS_GROUP})},
        {GroupPair(WindowTier_TypeUUID(),          {TG::WALL_OPENING_GROUP,TG::WALL_OPENING_SUB_ELEMENTS_GROUP})},
        {GroupPair(CornerWindowTier_TypeUUID(),    {TG::WALL_OPENING_GROUP,TG::WALL_OPENING_SUB_ELEMENTS_GROUP})},
        {GroupPair(DoorTier_TypeUUID(),            {TG::WALL_OPENING_GROUP,TG::WALL_OPENING_SUB_ELEMENTS_GROUP})},
        {GroupPair(NicheTier_TypeUUID(),           {TG::WALL_OPENING_GROUP,TG::WALL_OPENING_SUB_ELEMENTS_GROUP})},
        {GroupPair(PolygonalNicheTier_TypeUUID(),  {TG::WALL_OPENING_GROUP,TG::WALL_OPENING_SUB_ELEMENTS_GROUP})},
        {GroupPair(RecessTier_TypeUUID(),          {TG::WALL_OPENING_GROUP,TG::WALL_OPENING_SUB_ELEMENTS_GROUP})},
        {GroupPair(PolygonalRecessTier_TypeUUID(), {TG::WALL_OPENING_GROUP,TG::WALL_OPENING_SUB_ELEMENTS_GROUP})},
        {GroupPair(JointTier_TypeUUID(),           {TG::WALL_OPENING_GROUP,TG::WALL_OPENING_SUB_ELEMENTS_GROUP})},
        {GroupPair(FlushPierTier_TypeUUID(),       {TG::WALL_OPENING_SUB_ELEMENTS_GROUP})},
        {GroupPair(Rabbet_TypeUUID(),              {TG::WALL_OPENING_SUB_ELEMENTS_GROUP})},
        {GroupPair(Facing_TypeUUID(),              {TG::WALL_OPENING_SUB_ELEMENTS_GROUP})},
        {GroupPair(Lintel_TypeUUID(),              {TG::WALL_OPENING_SUB_ELEMENTS_GROUP})},
        {GroupPair(RollerBlind_TypeUUID(),         {TG::WALL_OPENING_SUB_ELEMENTS_GROUP})},

        {GroupPair(WindowReveal_TypeUUID(),        {TG::REVEAL_GROUP})},
        {GroupPair(CornerWindowReveal_TypeUUID(),  {TG::REVEAL_GROUP})},
        {GroupPair(DoorReveal_TypeUUID(),          {TG::REVEAL_GROUP})},
        {GroupPair(WindowDoorReveal_TypeUUID(),    {TG::REVEAL_GROUP})},
        {GroupPair(NicheReveal_TypeUUID(),         {TG::REVEAL_GROUP})},
        {GroupPair(RecessReveal_TypeUUID(),        {TG::REVEAL_GROUP})},

        {GroupPair(DoorSwing_TypeUUID(),           {TG::NO_GROUP})},
        {GroupPair(DoorSill_TypeUUID(),            {TG::NO_GROUP})},
        {GroupPair(Sill_TypeUUID(),                {TG::NO_GROUP})},
        {GroupPair(SillBothSides_TypeUUID(),       {TG::NO_GROUP})},


        //----------------- Foundation

        {GroupPair(StripFoundation_TypeUUID(),      {TG::AXIS_ELEMENT_GROUP})},
        {GroupPair(IndividualFoundation_TypeUUID(), {TG::NO_GROUP})},
        {GroupPair(Any3DFoundation_TypeUUID(),      {TG::NO_GROUP})},
        {GroupPair(SlabFoundation_TypeUUID(),       {TG::NO_GROUP})},
        {GroupPair(SlabFoundationTier_TypeUUID(),   {TG::NO_GROUP})},


        //----------------- Special architecture elements

        {GroupPair(ArchitectureTextBlock_TypeUUID(),              {TG::TEXT_GROUP})},
        {GroupPair(ArchitectureVariableTextBlock_TypeUUID(),      {TG::TEXT_GROUP})},
        {GroupPair(ArchitectureVariableText_TypeUUID(),           {TG::TEXT_GROUP})},

        {GroupPair(AttributeContainer_TypeUUID(),                  {TG::NO_GROUP})},
        {GroupPair(ArchitecturePointSymbol_TypeUUID(),             {TG::NO_GROUP})},
        {GroupPair(ArchitecturePointSymbol3D_TypeUUID(),           {TG::NO_GROUP})},
        {GroupPair(ArchitectureArea3D_TypeUUID(),                  {TG::NO_GROUP})},
        {GroupPair(ArchitectureElevation_TypeUUID(),               {TG::NO_GROUP})},
        {GroupPair(ArchitectureFacestyle_TypeUUID(),               {TG::NO_GROUP})},
        {GroupPair(ArchitectureHatching_TypeUUID(),                {TG::NO_GROUP})},
        {GroupPair(ArchitectureFilling_TypeUUID(),                 {TG::NO_GROUP})},
        {GroupPair(ArchitectureBitmap_TypeUUID(),                  {TG::NO_GROUP})},
        {GroupPair(ArchitectureLine_TypeUUID(),                    {TG::NO_GROUP})},
        {GroupPair(ArchitectureCircle_TypeUUID(),                  {TG::NO_GROUP})},
        {GroupPair(ArchitecturePolyline_TypeUUID(),                {TG::NO_GROUP})},
        {GroupPair(ArchitectureHyperElement_TypeUUID(),            {TG::NO_GROUP})},
        {GroupPair(ArchitectureAdditionalFinishElement_TypeUUID(), {TG::NO_GROUP})},
        {GroupPair(ArchitectureVolume3D_TypeUUID(),                {TG::NO_GROUP})},
        {GroupPair(ArchitectureOpeningPlane_TypeUUID(),            {TG::NO_GROUP})},
        {GroupPair(ArchitectureComponent_TypeUUID(),               {TG::NO_GROUP})},
        {GroupPair(ArchitectureComponentLinkage_TypeUUID(),        {TG::NO_GROUP})},
        {GroupPair(ArchitectureBRep3D_Volume_TypeUUID(),           {TG::NO_GROUP})},
        {GroupPair(ArchitectureBRep3D_Surface_TypeUUID(),          {TG::NO_GROUP})},
        {GroupPair(ArchitectureBRep3D_Wire_TypeUUID(),             {TG::NO_GROUP})},
        {GroupPair(ArchitectureCylinder3D_TypeUUID(),              {TG::NO_GROUP})},
        {GroupPair(ArchitectureSphere3D_TypeUUID(),                {TG::NO_GROUP})},


        //----------------- Stairs

        {GroupPair(Stairs_TypeUUID(),                     {TG::NO_GROUP})},
        {GroupPair(StairsStraightFlight_TypeUUID(),       {TG::NO_GROUP})},
        {GroupPair(StairsHalfTurn_TypeUUID(),             {TG::NO_GROUP})},
        {GroupPair(StairsWinder_TypeUUID(),               {TG::NO_GROUP})},
        {GroupPair(StairsDoubleQuarterTurn_TypeUUID(),    {TG::NO_GROUP})},
        {GroupPair(StairsTripleQuarterTurn_TypeUUID(),    {TG::NO_GROUP})},
        {GroupPair(StairsSpiral_TypeUUID(),               {TG::NO_GROUP})},
        {GroupPair(StairsUType_TypeUUID(),                {TG::NO_GROUP})},
        {GroupPair(StairsQuarterLanding_TypeUUID(),       {TG::NO_GROUP})},
        {GroupPair(StairsDoubleQuarterLanding_TypeUUID(), {TG::NO_GROUP})},
        {GroupPair(StairsElement_TypeUUID(),              {TG::NO_GROUP})},
        {GroupPair(StairsElementContainer_TypeUUID(),     {TG::NO_GROUP})},
        {GroupPair(StairsDirectionSymbol_TypeUUID(),      {TG::NO_GROUP})},
        {GroupPair(StairModeler_TypeUUID(),               {TG::SMART_SYMBOL_GROUP})},


        //----------------- Room, Floor, Surfaces, Storey

        {GroupPair(Room_TypeUUID(),                        {TG::NO_GROUP})},
        {GroupPair(RoomGroup_TypeUUID(),                   {TG::NO_GROUP})},
        {GroupPair(ArchitectureFloorSurface_TypeUUID(),    {TG::NO_GROUP})},
        {GroupPair(ArchitectureVerticalSurface_TypeUUID(), {TG::NO_GROUP})},
        {GroupPair(ArchitectureCeilingSurface_TypeUUID(),  {TG::NO_GROUP})},
        {GroupPair(ArchitectureBaseboard_TypeUUID(),       {TG::NO_GROUP})},
        {GroupPair(FloorSurface_TypeUUID(),                {TG::NO_GROUP})},
        {GroupPair(VerticalSurface_TypeUUID(),             {TG::NO_GROUP})},
        {GroupPair(CeilingSurface_TypeUUID(),              {TG::NO_GROUP})},
        {GroupPair(Baseboard_TypeUUID(),                   {TG::NO_GROUP})},
        {GroupPair(Storey_TypeUUID(),                      {TG::NO_GROUP})},
        {GroupPair(NetStorey_TypeUUID(),                   {TG::NO_GROUP})},
        {GroupPair(StoreyGroup_TypeUUID(),                 {TG::NO_GROUP})},


        //----------------- Timber elements

        {GroupPair(Rafter_TypeUUID(),       {TG::NO_GROUP})},
        {GroupPair(RafterPlaced_TypeUUID(), {TG::NO_GROUP})},
        {GroupPair(RafterPurlin_TypeUUID(), {TG::NO_GROUP})},
        {GroupPair(HipRafter_TypeUUID(),    {TG::NO_GROUP})},
        {GroupPair(Header_TypeUUID(),       {TG::NO_GROUP})},
        {GroupPair(Purlin_TypeUUID(),       {TG::NO_GROUP})},
        {GroupPair(CollarBeam_TypeUUID(),   {TG::NO_GROUP})},
        {GroupPair(CollarTie_TypeUUID(),    {TG::NO_GROUP})},
        {GroupPair(Post_TypeUUID(),         {TG::NO_GROUP})},
        {GroupPair(ValleyRafter_TypeUUID(), {TG::NO_GROUP})},
        {GroupPair(JoistPlaced_TypeUUID(),  {TG::NO_GROUP})},
        {GroupPair(Timber_TypeUUID(),       {TG::NO_GROUP})},


        //----------------- Roof elements

        {GroupPair(RoofFrame_TypeUUID(),         {TG::NO_GROUP})},
        {GroupPair(HyperRoofFrame_TypeUUID(),    {TG::NO_GROUP})},
        {GroupPair(HyperRoofCovering_TypeUUID(), {TG::NO_GROUP})},
        {GroupPair(RoofCovering_TypeUUID(),      {TG::NO_GROUP})},
        {GroupPair(Skylight_TypeUUID(),          {TG::NO_GROUP})},
        {GroupPair(TentRoofFrame_TypeUUID(),     {TG::NO_GROUP})},
        {GroupPair(RoofSurface_TypeUUID(),       {TG::NO_GROUP})},
        {GroupPair(RoofSurfaceContour_TypeUUID(),{TG::NO_GROUP})},


        //----------------- Associative views

        {GroupPair(AssociativeView_TypeUUID(),                           {TG::NO_GROUP})},
        {GroupPair(AssociativeViewFrame_TypeUUID(),                      {TG::NO_GROUP})},
        {GroupPair(AssociativeViewLinearDimension_TypeUUID(),            {TG::NO_GROUP})},
        {GroupPair(AssociativeViewAbsoluteElevationDimension_TypeUUID(), {TG::NO_GROUP})},
        {GroupPair(AssociativeViewCartesianGrid_TypeUUID(),              {TG::NO_GROUP})},


        //----------------- Section along any path

        {GroupPair(SectionAlongPath_TypeUUID(),      {TG::NO_GROUP})},
        {GroupPair(SectionPath_TypeUUID(),           {TG::NO_GROUP})},
        {GroupPair(SectionPathStationing_TypeUUID(), {TG::NO_GROUP})},


        //----------------- Unified views and sections
        {GroupPair(UnifiedView_TypeUUID(),              {TG::NO_GROUP})},
        {GroupPair(UnifiedSection_TypeUUID(),           {TG::NO_GROUP})},
        {GroupPair(UVSLabeling_TypeUUID(),              {TG::NO_GROUP})},
        {GroupPair(UVSClippingPathSymbol_TypeUUID(),    {TG::NO_GROUP}) },


        //----------------- Reports

        {GroupPair(AssociativeReport_TypeUUID(),                  {TG::NO_GROUP})},
        {GroupPair(AssociativeReportAreaVisualisation_TypeUUID(), {TG::NO_GROUP})},
        {GroupPair(AssociativeReportParameter_TypeUUID(),         {TG::NO_GROUP})},
        {GroupPair(LegendStamp_TypeUUID(),                        {TG::NO_GROUP})},


        //----------------- Layout elements

        {GroupPair(LayoutSheet_TypeUUID(),        {TG::NO_GROUP})},
        {GroupPair(LayoutElement_TypeUUID(),      {TG::NO_GROUP})},
        {GroupPair(LayoutWindow_TypeUUID(),       {TG::NO_GROUP})},
        {GroupPair(LayoutBorder_TypeUUID(),       {TG::NO_GROUP})},
        {GroupPair(LayoutFreeElement_TypeUUID(),  {TG::NO_GROUP})},
        {GroupPair(LayoutBorderMaster_TypeUUID(), {TG::NO_GROUP})},
        {GroupPair(LayoutMaster_TypeUUID(),       {TG::NO_GROUP})},
        {GroupPair(LayoutIntersection_TypeUUID(), {TG::NO_GROUP})},
        {GroupPair(LayoutClipRegion_TypeUUID(),   {TG::NO_GROUP})},


        //----------------- Animation

        {GroupPair(AnimationLight_TypeUUID(), {TG::NO_GROUP})},


        //----------------- Reinforcement

        {GroupPair(EngineerDimensionLine_TypeUUID(),              {TG::NO_GROUP})},
        {GroupPair(EngineerDimensionLineOverlap_TypeUUID(),       {TG::NO_GROUP})},
        {GroupPair(EngineerLabel_TypeUUID(),                      {TG::NO_GROUP})},
        {GroupPair(EngineerTextPointer_TypeUUID(),                {TG::NO_GROUP})},
        {GroupPair(EngineerSymbol2D_TypeUUID(),                   {TG::NO_GROUP})},

        {GroupPair(BarsDefinition_TypeUUID(),                     {TG::NO_GROUP})},
        {GroupPair(BarsAreaDefinition_TypeUUID(),                 {TG::NO_GROUP})},
        {GroupPair(BarsLinearPlacement_TypeUUID(),                {TG::BARS_PLACEMENT_GROUP})},
        {GroupPair(BarsLinearMultiPlacement_TypeUUID(),           {TG::BARS_PLACEMENT_GROUP})},
        {GroupPair(BarsAreaPlacement_TypeUUID(),                  {TG::BARS_PLACEMENT_GROUP})},
        {GroupPair(BarsSpiralPlacement_TypeUUID(),                {TG::BARS_PLACEMENT_GROUP})},
        {GroupPair(BarsCircularPlacement_TypeUUID(),              {TG::BARS_PLACEMENT_GROUP})},
        {GroupPair(BarsRotationalSolidPlacement_TypeUUID(),       {TG::BARS_PLACEMENT_GROUP})},
        {GroupPair(BarsRotationalPlacement_TypeUUID(),            {TG::BARS_PLACEMENT_GROUP})},
        {GroupPair(BarsTangentionalPlacement_TypeUUID(),          {TG::BARS_PLACEMENT_GROUP})},
        {GroupPair(BarsEndBendingPlacement_TypeUUID(),            {TG::NO_GROUP})},
        {GroupPair(BarsPlacementConnection_TypeUUID(),            {TG::NO_GROUP})},

        {GroupPair(BarsRepresentation_TypeUUID(),                 {TG::BARS_REPRESENTATION_GROUP})},
        {GroupPair(BarsRepresentationLine_TypeUUID(),             {TG::BARS_REPRESENTATION_GROUP})},
        {GroupPair(BarsAreaRepresentation_TypeUUID(),             {TG::BARS_REPRESENTATION_GROUP})},
        {GroupPair(BarsAreaRepresentationLine_TypeUUID(),         {TG::BARS_REPRESENTATION_GROUP})},
        {GroupPair(BarsLine_TypeUUID(),                           {TG::BARS_REPRESENTATION_GROUP})},
        {GroupPair(BarsPolyline_TypeUUID(),                       {TG::BARS_REPRESENTATION_GROUP})},
        {GroupPair(BarsCircle_TypeUUID(),                         {TG::BARS_REPRESENTATION_GROUP})},
        {GroupPair(BarsSchemaPlacement_TypeUUID(),                {TG::BARS_REPRESENTATION_GROUP})},
        {GroupPair(BarsSchemaRepresentation_TypeUUID(),           {TG::BARS_REPRESENTATION_GROUP})},
        {GroupPair(BarsSchemaCircularPlacement_TypeUUID(),        {TG::BARS_REPRESENTATION_GROUP})},

        {GroupPair(MeshDefinition_TypeUUID(),                     {TG::NO_GROUP})},
        {GroupPair(BendedMeshDefinition_TypeUUID(),               {TG::NO_GROUP})},
        {GroupPair(BendedMeshSchemaPlacement_TypeUUID(),          {TG::NO_GROUP})},
        {GroupPair(BendedMeshSchemaRepresentation_TypeUUID(),     {TG::NO_GROUP})},

        {GroupPair(MeshPlacementDefinition_TypeUUID(),            {TG::NO_GROUP})},
        {GroupPair(MeshPlacement_TypeUUID(),                      {TG::NO_GROUP})},
        {GroupPair(MeshRepresentation_TypeUUID(),                 {TG::MESH_REPRESENTATION_GROUP})},
        {GroupPair(MeshAreaPlacement_TypeUUID(),                  {TG::NO_GROUP})},
        {GroupPair(MeshAreaRepresentation_TypeUUID(),             {TG::MESH_REPRESENTATION_GROUP})},
        {GroupPair(MeshAreaBorder_TypeUUID(),                     {TG::MESH_REPRESENTATION_GROUP})},

        {GroupPair(MeshDiagonal_TypeUUID(),                       {TG::MESH_REPRESENTATION_GROUP})},
        {GroupPair(MeshBorder_TypeUUID(),                         {TG::MESH_REPRESENTATION_GROUP})},

        {GroupPair(MeshSchedule_TypeUUID(),                       {TG::NO_GROUP})},
        {GroupPair(MeshScheduleMaskPoint_TypeUUID(),              {TG::NO_GROUP})},
        {GroupPair(MeshScheduleListPoint_TypeUUID(),              {TG::NO_GROUP})},
        {GroupPair(MeshScheduleListHead_TypeUUID(),               {TG::NO_GROUP})},
        {GroupPair(MeshScheduleMesh_TypeUUID(),                   {TG::NO_GROUP})},
        {GroupPair(MeshScheduleMeshPlaced_TypeUUID(),             {TG::NO_GROUP})},
        {GroupPair(BendingScheduleListHead_TypeUUID(),            {TG::NO_GROUP})},

        {GroupPair(ReinforcementGroup_TypeUUID(),                 {TG::NO_GROUP})},
        {GroupPair(ReinforcementFFUnit_TypeUUID(),                {TG::NO_GROUP})},
        {GroupPair(ReinforcementStampPoint_TypeUUID(),            {TG::NO_GROUP})},
        {GroupPair(ReinforcementStructuralStarterBars_TypeUUID(), {TG::NO_GROUP})},

        {GroupPair(ReinforcementExtrudeRebarAlongPath(),          {TG::NO_GROUP})},
        {GroupPair(ReinforcementSweepBarsAlongPath(),             {TG::NO_GROUP})},
        {GroupPair(ReinforcementPlaceBarsAlongSurface_TypeUUID(), {TG::NO_GROUP})},

        {GroupPair(SecondaryReinforcementGroup_TypeUUID(),        {TG::NO_GROUP})},

        //----------------- Facility management

        {GroupPair(Article_TypeUUID(),       {TG::NO_GROUP})},
        {GroupPair(RoomOccupancy_TypeUUID(), {TG::NO_GROUP})},


        //----------------- Fem

        {GroupPair(FemSmartSymbolFormwork_TypeUUID(),     {TG::NO_GROUP})},
        {GroupPair(FemPlateElementLine_TypeUUID(),        {TG::NO_GROUP})},
        {GroupPair(FemBarLine_TypeUUID(),                 {TG::NO_GROUP})},
        {GroupPair(FemAreaLoad_TypeUUID(),                {TG::NO_GROUP})},
        {GroupPair(FemPointLoad_TypeUUID(),               {TG::NO_GROUP})},
        {GroupPair(FemLineLoad_TypeUUID(),                {TG::NO_GROUP})},
        {GroupPair(FemLineSupport_TypeUUID(),             {TG::NO_GROUP})},
        {GroupPair(FemSpring_TypeUUID(),                  {TG::NO_GROUP})},
        {GroupPair(FemContours_TypeUUID(),                {TG::NO_GROUP})},
        {GroupPair(FemSmartSymbolMeshFormwork_TypeUUID(), {TG::NO_GROUP})},


        //----------------- Position plan

        {GroupPair(PositionPlan_TypeUUID(),        {TG::NO_GROUP})},
        {GroupPair(PositionPlanProject_TypeUUID(), {TG::NO_GROUP})},


        //----------------- Precast

        {GroupPair(PrecastConstructiveElement_TypeUUID(),              {TG::PRECAST_GROUP})},
        {GroupPair(PrecastFormWorkConstructiveElement_TypeUUID(),      {TG::PRECAST_GROUP})},
        {GroupPair(PrecastFormWorkConstructiveElementManual_TypeUUID(),{TG::PRECAST_GROUP})},
        {GroupPair(PrecastFormWorkConstructiveHelpElement_TypeUUID(),  {TG::PRECAST_GROUP})},
        {GroupPair(TentRoofPlane_TypeUUID(),                           {TG::PRECAST_GROUP})},
        {GroupPair(PrecastGrid_TypeUUID(),                             {TG::PRECAST_GROUP})},
        {GroupPair(PrecastGridRegion_TypeUUID(),                       {TG::PRECAST_GROUP})},
        {GroupPair(PrecastGridAxis_TypeUUID(),                         {TG::PRECAST_GROUP})},
        {GroupPair(PrecastSingleAxis_TypeUUID(),                       {TG::PRECAST_GROUP})},
        {GroupPair(PrecastWallDesign_TypeUUID(),                       {TG::PRECAST_GROUP})},
        {GroupPair(PrecastText_TypeUUID(),                             {TG::PRECAST_GROUP})},
        {GroupPair(PrecastStaticSupport_TypeUUID(),                    {TG::PRECAST_GROUP})},
        {GroupPair(PrecastStaticSupportLine_TypeUUID(),                {TG::PRECAST_GROUP})},
        {GroupPair(PrecastSlabSupport_TypeUUID(),                      {TG::PRECAST_GROUP})},
        {GroupPair(PrecastSolidWall_TypeUUID(),                        {TG::PRECAST_GROUP})},
        {GroupPair(PrecastDoubleWall_TypeUUID(),                       {TG::PRECAST_GROUP})},
        {GroupPair(PrecastBrickWall_TypeUUID(),                        {TG::PRECAST_GROUP})},
        {GroupPair(PrecastElementPlan_TypeUUID(),                      {TG::PRECAST_GROUP})},
        {GroupPair(PrecastElementPlanElement_TypeUUID(),               {TG::PRECAST_GROUP})},
        {GroupPair(PrecastSpecialLoadSmartSymbolDefinition_TypeUUID(), {TG::PRECAST_GROUP})},
        {GroupPair(PrecastSpecialLoad_TypeUUID(),                      {TG::PRECAST_GROUP})},
        {GroupPair(PrecastHalfFloor_TypeUUID(),                        {TG::PRECAST_GROUP})},
        {GroupPair(PrecastSolidFloor_TypeUUID(),                       {TG::PRECAST_GROUP})},
        {GroupPair(PrecastPanelComponent_TypeUUID(),                   {TG::PRECAST_GROUP})},
        {GroupPair(PrecastSlabPlacementPolygon_TypeUUID(),             {TG::PRECAST_GROUP})},
        {GroupPair(PrecastSlabPlacement_TypeUUID(),                    {TG::PRECAST_GROUP})},
        {GroupPair(PrecastSlabMandatoryDivision_TypeUUID(),            {TG::PRECAST_GROUP})},
        {GroupPair(PrecastDesign_TypeUUID(),                           {TG::PRECAST_GROUP})},
        {GroupPair(PrecastLayer_TypeUUID(),                            {TG::PRECAST_GROUP})},
        {GroupPair(PrecastRecessAttribute_TypeUUID(),                  {TG::PRECAST_GROUP})},
        {GroupPair(PrecastElement_TypeUUID(),                          {TG::PRECAST_GROUP})},
        {GroupPair(PrecastGirderDefinition_TypeUUID(),                 {TG::PRECAST_GROUP})},
        {GroupPair(PrecastGirderPlacement_TypeUUID(),                  {TG::PRECAST_GROUP})},
        {GroupPair(PrecastConnector_TypeUUID(),                        {TG::PRECAST_GROUP})},
        {GroupPair(PrecastReinforcementGroup_TypeUUID(),               {TG::PRECAST_GROUP})},
        {GroupPair(PrecastMWSReinforcement_TypeUUID(),                 {TG::PRECAST_GROUP})},
        {GroupPair(PrecastWallPanel_TypeUUID(),                        {TG::PRECAST_GROUP})},
        {GroupPair(PrecastWallPanelElement_TypeUUID(),                 {TG::PRECAST_GROUP})},
        {GroupPair(PrecastWallPanelElementTier_TypeUUID(),             {TG::PRECAST_GROUP})},
        {GroupPair(PrecastWallElementTier_TypeUUID(),                  {TG::PRECAST_GROUP})},
        {GroupPair(PrecastSlabRecess_TypeUUID(),                       {TG::PRECAST_GROUP})},
        {GroupPair(PrecastSlabRecessRepresentation_TypeUUID(),         {TG::PRECAST_GROUP})},
        {GroupPair(PrecastWallConnector_TypeUUID(),                    {TG::PRECAST_GROUP})},
        {GroupPair(PrecastReinforcementAttribute_TypeUUID(),           {TG::PRECAST_GROUP})},
        {GroupPair(PrecastPrestHollowCoreElement_TypeUUID(),           {TG::PRECAST_GROUP})},
        {GroupPair(PrecastHollowCoreElement_TypeUUID(),                {TG::PRECAST_GROUP})},
        {GroupPair(PrecastPIPanel_TypeUUID(),                          {TG::PRECAST_GROUP})},
        {GroupPair(PrecastConnectionElement_TypeUUID(),                {TG::PRECAST_GROUP})},
        {GroupPair(PrecastBrickCompositeFloor_TypeUUID(),              {TG::PRECAST_GROUP})},
        {GroupPair(PrecastBrickFloor_TypeUUID(),                       {TG::PRECAST_GROUP})},
        {GroupPair(PrecastBrickSolidFloor_TypeUUID(),                  {TG::PRECAST_GROUP})},
        {GroupPair(PrecastFormworkElement_TypeUUID(),                  {TG::PRECAST_GROUP})},
        {GroupPair(PrecastFormworkCoupler_TypeUUID(),                  {TG::PRECAST_GROUP})},
        {GroupPair(PrecastFormworkSmartSymbol_TypeUUID(),              {TG::PRECAST_GROUP})},
        {GroupPair(PrecastFormworkPlacement_TypeUUID(),                {TG::PRECAST_GROUP})},
        {GroupPair(PrecastFormworkView_TypeUUID(),                     {TG::PRECAST_GROUP})},
        {GroupPair(PrecastBubbleFloor_TypeUUID(),                      {TG::PRECAST_GROUP})},
        {GroupPair(PrecastCrane_TypeUUID(),                            {TG::PRECAST_GROUP})},
        {GroupPair(PrecastOptima_TypeUUID(),                           {TG::PRECAST_GROUP})},
        {GroupPair(PrecastCobiaxSlab_TypeUUID(),                       {TG::PRECAST_GROUP})},
        {GroupPair(PrecastElementSolidWall_TypeUUID(),                 {TG::PRECAST_GROUP})},
        {GroupPair(PrecastElementDoubleWall_TypeUUID(),                {TG::PRECAST_GROUP})},
        {GroupPair(PrecastElementBricksWall_TypeUUID(),                {TG::PRECAST_GROUP})},
        {GroupPair(PrecastElementSandwichWall_TypeUUID(),              {TG::PRECAST_GROUP})},
        {GroupPair(PrecastElementThermoWall_TypeUUID(),                {TG::PRECAST_GROUP})},
        {GroupPair(PrecastElementNLayersWall_TypeUUID(),               {TG::PRECAST_GROUP})},
        {GroupPair(PrecastReinforcementSolidWall_TypeUUID(),           {TG::PRECAST_GROUP})},
        {GroupPair(PrecastReinforcementDoubleWall_TypeUUID(),          {TG::PRECAST_GROUP})},
        {GroupPair(PrecastReinforcementBricksWall_TypeUUID(),          {TG::PRECAST_GROUP})},
        {GroupPair(PrecastReinforcementSandwichWall_TypeUUID(),        {TG::PRECAST_GROUP})},
        {GroupPair(PrecastReinforcementThermoWall_TypeUUID(),          {TG::PRECAST_GROUP})},
        {GroupPair(PrecastReinforcementNLayersWall_TypeUUID(),         {TG::PRECAST_GROUP})},
        {GroupPair(PrecastBaseReinforcement_TypeUUID(),                {TG::PRECAST_GROUP})},
        {GroupPair(PrecastRecessAttributeSolidWall_TypeUUID(),         {TG::PRECAST_GROUP})},
        {GroupPair(PrecastRecessAttributeDoubleWall_TypeUUID(),        {TG::PRECAST_GROUP})},
        {GroupPair(PrecastRecessAttributeBricksWall_TypeUUID(),        {TG::PRECAST_GROUP})},
        {GroupPair(PrecastRecessAttributeSandwichWall_TypeUUID(),      {TG::PRECAST_GROUP})},
        {GroupPair(PrecastRecessAttributeThermoWall_TypeUUID(),        {TG::PRECAST_GROUP})},
        {GroupPair(PrecastRecessAttributeNLayersWall_TypeUUID(),       {TG::PRECAST_GROUP})},
        {GroupPair(DrawingFileAttributes_TypeUUID(),                   {TG::PRECAST_GROUP})},
        {GroupPair(PrecastConnectorPlacement_TypeUUID(),               {TG::PRECAST_GROUP})},
        {GroupPair(PrecastVisibleSideSymbol_TypeUUID(),                {TG::PRECAST_GROUP})},
        {GroupPair(PrecastWallManagerElement_TypeUUID(),               {TG::PRECAST_GROUP})},
        {GroupPair(PrecastFloorManagerElement_TypeUUID(),              {TG::PRECAST_GROUP})},
        {GroupPair(PrecastElementation_TypeUUID(),                     {TG::PRECAST_GROUP})},

        //----------------- Clash

        {GroupPair(Clash_TypeUUID(),                                   {TG::NO_GROUP})},

        //----------------- Type Ids for elements without NAS association

        {GroupPair(DoorOpeningSmartSymbol_TypeUUID(),          {TG::SMART_SYMBOL_GROUP})},
        {GroupPair(WindowOpeningSmartSymbol_TypeUUID(),        {TG::SMART_SYMBOL_GROUP})},
        {GroupPair(NicheSmartSymbol_TypeUUID(),                {TG::SMART_SYMBOL_GROUP})},
        {GroupPair(RecessSmartSymbol_TypeUUID(),               {TG::SMART_SYMBOL_GROUP})},
        {GroupPair(ParapetSmartSymbol_TypeUUID(),              {TG::SMART_SYMBOL_GROUP})},
        {GroupPair(Facade_TypeUUID(),                          {TG::FACADE_GROUP})},
        {GroupPair(SubFacade_TypeUUID(),                       {TG::FACADE_GROUP})},
        {GroupPair(FacadeSmartSymbol_TypeUUID(),               {TG::FACADE_GROUP})},
        {GroupPair(SlabOpeningSmartSymbol_TypeUUID(),          {TG::SMART_SYMBOL_GROUP})},
        {GroupPair(SlabRecessSmartSymbol_TypeUUID(),           {TG::SMART_SYMBOL_GROUP})},
        {GroupPair(SkylightSmartSymbol_TypeUUID(),             {TG::SMART_SYMBOL_GROUP})},
        {GroupPair(Rail_TypeUUID(),                            {TG::SMART_SYMBOL_GROUP})},
        {GroupPair(SubRail_TypeUUID(),                         {TG::SMART_SYMBOL_GROUP})},
        {GroupPair(RailSmartSymbol_TypeUUID(),                 {TG::SMART_SYMBOL_GROUP})},
        {GroupPair(CeilingSystem_TypeUUID(),                   {TG::SMART_SYMBOL_GROUP})},
        {GroupPair(SubCeilingSystem_TypeUUID(),                {TG::SMART_SYMBOL_GROUP})},
        {GroupPair(CeilingSystemSmartSymbol_TypeUUID(),        {TG::SMART_SYMBOL_GROUP})},


        {GroupPair(PointFixture_TypeUUID(),                    {TG::FIXTURE_GROUP})},
        {GroupPair(LineFixture_TypeUUID(),                     {TG::FIXTURE_GROUP})},
        {GroupPair(PlaneFixture_TypeUUID(),                    {TG::FIXTURE_GROUP})},
        {GroupPair(GeneralGroupFixture_TypeUUID(),             {TG::FIXTURE_GROUP})},
        {GroupPair(CadastralPointFixture_TypeUUID(),           {TG::FIXTURE_GROUP})},
        {GroupPair(CadastralLineFixture_TypeUUID(),            {TG::FIXTURE_GROUP})},
        {GroupPair(CadastralPlaneFixture_TypeUUID(),           {TG::FIXTURE_GROUP})},
        {GroupPair(CadastralGeneralGroupFixture_TypeUUID(),    {TG::FIXTURE_GROUP})},

        {GroupPair(AssociativeViewIntersectionBody_TypeUUID(), {TG::NO_GROUP})},
        {GroupPair(AssociativeViewDimensions_TypeUUID(),       {TG::NO_GROUP})},
        {GroupPair(AlignmentDimension_TypeUUID(),              {TG::DIMENSION_GROUP})},
        {GroupPair(Associative_AlignmentDimension_TypeUUID(), {TG::DIMENSION_GROUP})},

        {GroupPair(SmartPartGroup_TypeUUID(),                  {TG::SMART_PART_GROUP})},
        {GroupPair(SmartPart_TypeUUID(),                       {TG::SMART_PART_GROUP})},
        {GroupPair(SubSmartPart_TypeUUID(),                    {TG::SMART_PART_GROUP})},
        {GroupPair(DoorOpeningSmartPart_TypeUUID(),            {TG::SMART_PART_GROUP})},
        {GroupPair(WindowOpeningSmartPart_TypeUUID(),          {TG::SMART_PART_GROUP})},
        {GroupPair(SillSmartPart_TypeUUID(),                   {TG::SMART_PART_GROUP})},
        {GroupPair(SolarScreenSmartPart_TypeUUID(),            {TG::SMART_PART_GROUP})},
        {GroupPair(EquipmentSmartPart_TypeUUID(),              {TG::SMART_PART_GROUP})},
        {GroupPair(LightdomeSmartPart_TypeUUID(),              {TG::SMART_PART_GROUP})},
        {GroupPair(RoofWindowSmartPart_TypeUUID (),            {TG::SMART_PART_GROUP})},
        {GroupPair(PointBuiltInElementSmartPart_TypeUUID (),   {TG::SMART_PART_GROUP})},
        {GroupPair(ReinforcementRobotSmartPart_TypeUUID(),     {TG::SMART_PART_GROUP})},

        {GroupPair(PythonPartGroup_TypeUUID(),                 {TG::PYTHON_PART_GROUP})},
        {GroupPair(PythonPart_TypeUUID(),                      {TG::PYTHON_PART_GROUP})},
        {GroupPair(SubPythonPart_TypeUUID(),                   {TG::PYTHON_PART_GROUP})},

        {GroupPair(PipeWorkGroup_TypeUUID(),                   {TG::PIPEWORK_GROUP})},
        {GroupPair(PipeWork_TypeUUID(),                        {TG::PIPEWORK_GROUP})},
        {GroupPair(SubPipeWork_TypeUUID(),                     {TG::PIPEWORK_GROUP})},
        {GroupPair(PipeBundleGroup_TypeUUID(),                 {TG::PIPEBUNDLE_GROUP})},
        {GroupPair(PipeBundle_TypeUUID(),                      {TG::PIPEBUNDLE_GROUP})},
        {GroupPair(SubPipeBundle_TypeUUID(),                   {TG::PIPEBUNDLE_GROUP})},

        {GroupPair(OpeningPartGroup_TypeUUID(),                {TG::OPENINGPART_GROUP})},
        {GroupPair(OpeningPart_TypeUUID(),                     {TG::OPENINGPART_GROUP})},
        {GroupPair(SubOpeningPart_TypeUUID(),                  {TG::OPENINGPART_GROUP})},

        {GroupPair(OpeningPartWindowGroup_TypeUUID(),          {TG::WINDOW_OPENINGPART_GROUP})},
        {GroupPair(OpeningPartWindow_TypeUUID(),               {TG::WINDOW_OPENINGPART_GROUP})},
        {GroupPair(SubOpeningPartWindow_TypeUUID(),            {TG::WINDOW_OPENINGPART_GROUP})},

        {GroupPair(OpeningPartDoorGroup_TypeUUID(),            {TG::DOOR_OPENINGPART_GROUP})},
        {GroupPair(OpeningPartDoor_TypeUUID(),                 {TG::DOOR_OPENINGPART_GROUP})},
        {GroupPair(SubOpeningPartDoor_TypeUUID(),              {TG::DOOR_OPENINGPART_GROUP})},

        {GroupPair(Legend_TypeUUID(),                          {TG::NO_GROUP})},
        {GroupPair(LegendRow_TypeUUID(),                       {TG::NO_GROUP})},
        {GroupPair(LegendEndSum_TypeUUID(),                    {TG::NO_GROUP})},
        {GroupPair(LegendIntermediateSum_TypeUUID(),           {TG::NO_GROUP})},

        {GroupPair(DTMAreaLabel_TypeUUID(),        {TG::TEXT_GROUP})},
        {GroupPair(DTMGridLabel_TypeUUID(),        {TG::TEXT_GROUP})},
        {GroupPair(DTMContourLineLabel_TypeUUID(), {TG::TEXT_GROUP})},
        {GroupPair(DTMElevationLabel_TypeUUID(),   {TG::TEXT_GROUP})},

        //----------------- Skeleton elements
        {GroupPair(SkeletonGrid_TypeUUID(),                 {TG::NO_GROUP})},
        {GroupPair(SkeletonColumn_TypeUUID(),               {TG::NO_GROUP})},
        {GroupPair(SkeletonBeam_TypeUUID(),                 {TG::NO_GROUP})},
        {GroupPair(SkeletonBrace_TypeUUID(),                {TG::NO_GROUP})},
        {GroupPair(SkeletonPurlin_TypeUUID(),               {TG::NO_GROUP})},
        {GroupPair(SkeletonPortalFrame_TypeUUID(),          {TG::NO_GROUP})},
        {GroupPair(SkeletonPortalFrameStructure_TypeUUID(), {TG::NO_GROUP})},
        {GroupPair(SkeletonSolidElementSystem_TypeUUID(),   {TG::NO_GROUP})},
        {GroupPair(SkeletonBeamSystem_TypeUUID(),           {TG::NO_GROUP})},
        {GroupPair(SkeletonPurlinSystem_TypeUUID(),         {TG::NO_GROUP})},
        {GroupPair(SkeletonAxis_TypeUUID(), {TG::NO_GROUP})},

        { GroupPair(PrecastDesignGeneral_TypeUUID(),                       { TG::PRECAST_GROUP }) },
        { GroupPair(PrecastElementGeneral_TypeUUID(),                      { TG::PRECAST_GROUP }) },
        { GroupPair(PrecastElementCompositeFormworkWall_TypeUUID(),        { TG::PRECAST_GROUP }) },
        { GroupPair(PrecastReinforcementCompositeFormworkWall_TypeUUID(),  { TG::PRECAST_GROUP }) },
        { GroupPair(PrecastRecessAttributeCompositeFormworkWall_TypeUUID(),{ TG::PRECAST_GROUP }) },
    };
