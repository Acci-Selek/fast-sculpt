import bpy
from bpy.types import Panel


class FSC_PT_Panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Fast Sculpt"
    bl_category = "Fast Sculpt"
    
    def draw(self, context):
        pass

class FSC_PT_Bool_Objects_Panel(FSC_PT_Panel, Panel):
    bl_parent_id = "FSC_PT_Panel"
    bl_label = "Bool objects"
    
    def draw(self, context): 

        layout = self.layout

        row = layout.row()
        row.prop_search(context.scene, "target_object", context.scene, "objects", text="Target")

        row = layout.row()
        row.operator('object.fsc_bool_union', text='Bool Union')

        row = layout.row()
        row.operator('object.fsc_bool_diff', text='Bool Difference')

class FSC_PT_Add_Objects_Panel(FSC_PT_Panel, Panel):
    bl_parent_id = "FSC_PT_Panel"
    bl_label = "Add objects"
    
    def draw(self, context): 

        layout = self.layout
        row = layout.row()
        row.prop(context.scene, "add_object_type", text="Type")

        row = layout.row()
        row.prop(context.scene, "add_scene_object", text="Scene")

        row = layout.row()
        row.prop(context.scene, "align_to_face", text="Align to face orientation")

        layout = self.layout
        row = layout.row()
        row.prop(context.scene, "add_object_mirror", text="Mirror")

        row = layout.row()
        row.operator('object.fsc_add_object', text="Add object mode")

class FSC_PT_Extract_Mask_Panel(FSC_PT_Panel, Panel):
    bl_parent_id = "FSC_PT_Panel"
    bl_label = "Extract objects"
    
    def draw(self, context): 

        layout = self.layout

        row = layout.row()
        row.prop(context.scene, "extract_thickness", text="Thickness")

        row = layout.row()
        row.prop(context.scene, "extract_offset", text="Offset")

        row = layout.row()
        row.operator('object.fsc_ot_mask_extract', text="Extract Mask")


class FSC_PT_Remesh_Panel(FSC_PT_Panel, Panel):
    bl_parent_id = "FSC_PT_Panel"
    bl_label = "Remesh objects"
    
    def draw(self, context): 

        layout = self.layout

        row = layout.row()
        row.prop(context.scene, "remesh_after_union", text="Remesh after union")

        row = layout.row()
        row.prop(context.scene, "remesh_after_extract", text="Remesh after extract")

        row = layout.row()
        row.prop(context.scene, "remesh_fix_poles", text="Fix poles")

        row = layout.row()
        row.prop(context.scene, "remesh_smooth_normals", text="Smooth normals")

        row = layout.row()
        row.prop(context.scene, "remesh_preserve_volume", text="Preserve volume")

        row = layout.row()
        row.prop(context.scene, "remesh_voxel_size", text="Voxel size")

        row = layout.row()
        row.operator('object.fsc_remesh', text="Remesh")


class FSC_PT_Retopo_Panel(FSC_PT_Panel, Panel):
    bl_parent_id = "FSC_PT_Panel"
    bl_label = "Retopo objects"
    
    def draw(self, context): 

        layout = self.layout
        row = layout.row()
        row.prop(context.scene, "retopo_object", text="Target")

        row = layout.row()
        row.operator('object.fsc_retopo', text="Add retopo mesh")