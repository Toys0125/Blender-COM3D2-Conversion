bl_info = {
    "name":         "COM3D2 Group Converter",
    "author":       "Toys0125",
    "blender":      (2,93,0),
    "version":      (0,1,0),
    "location":     "View 3D > Tool Shelf > Misc > COM3D2 group Converter",
    "description":  "Remap vertex groups into simplfied armature",
    "category":     "3D View"
}

import os
import sys

# Append files to sys path
file_dir = os.path.join(os.path.dirname(__file__), 'extern_tools')
if file_dir not in sys.path:
    sys.path.append(file_dir)

import bpy
from . import translatetable
class COM3D2ObjectProperties(bpy.types.PropertyGroup):
    selectedObject : bpy.props.PointerProperty(  # bl 2.80 use testint: bpy.props
        name="selectedObject",
        description="selectedObject",
        type=bpy.types.Object
        )
    applyMods: bpy.props.BoolProperty(
        name="Apply Vertex Mix Mods",
        description="Apply all Vertex Mix mods",
        default=True
    )
    
    

class ExecuteVertexRemapping(bpy.types.Operator):
    bl_idname = "object.execute_vertex_remapping"
    bl_label = "ExecuteVertexRemapping"

    # Here you declare everything you want to show in the dialog 

    # This is the method that is called when the ok button is pressed
    # which is what calls the ApplyModifers() method 
    def execute(self, context):
        try:
            bpy.ops.object.decode_cm3d2_vertex_group_names()
        except RuntimeError:
            pass
        translateVertexGroups(context,context.scene.COM3D2objectProperties)
        self.report({'INFO'}, "Remapping done")
        return {'FINISHED'}
    def cancel(self,context):
        return None

# This method adds a cube to the current scene and then applys scale and
# name to the cube  
def apply_modifiers(obj):
    ctx = bpy.context.copy()
    ctx['object'] = obj
    for _, m in enumerate(obj.modifiers):
        if m.type == 'VERTEX_WEIGHT_MIX':
            try:
                ctx['modifier'] = m
                bpy.ops.object.modifier_apply(ctx, modifier=m.name)
            except RuntimeError:
                print(f"Error applying {m.name} to {obj.name}.")

# Calls the menu when the script is ran
class COM3D2GroupConverter(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Misc"  # not used in blender 2.80
    bl_context = "objectmode"
    bl_label = "COM3D2 Group Converter"
    bl_idname = "VIEW3D_PT_COM3D2_Group_Converter"

    def draw(self, context):
        layout = self.layout
        obj = context.object
        props = context.scene.COM3D2objectProperties
        row = layout.row()
        row.prop(props,"applyMods")
        row= layout.row()
        row.operator('object.execute_vertex_remapping')
def translateVertexGroups(context,props):
    
    translate = translatetable.translateTable
    selected = context.selected_objects
    if len(selected) == 0:
        raise ValueError("No objects selected")
    for item in selected:
        for modifiername,mod in item.modifiers.items():
            if mod.type == 'VERTEX_WEIGHT_MIX':
                item.modifiers.remove(mod)
                print("Removed modifier for "+ modifiername)
        for key,value in translate.items():
            if value["L/R"]:
                if item.vertex_groups.find(key+"L") != -1:
                    item.vertex_groups.remove(item.vertex_groups[key+"L"])
                if item.vertex_groups.find(key+"R") != -1:
                    item.vertex_groups.remove(item.vertex_groups[key+"R"])
                item.vertex_groups.new(name=key+"L")
                item.vertex_groups.new(name=key+"R")
            else:
                if item.vertex_groups.find(key) != -1:
                    item.vertex_groups.remove(item.vertex_groups[key])
                item.vertex_groups.new(name=key)
            Nogroups = True
            isLeftorRightUsed = [True,True]
            for group in value["Groups"]:
                if value["L/R"]:
                    if item.vertex_groups.find(group+"L") == -1 and item.vertex_groups.find(group+"R") == -1:
                        continue
                    if item.vertex_groups.find(group+"L") != -1:
                        mod1 = item.modifiers.new(key+"L+"+group+"L",type="VERTEX_WEIGHT_MIX")
                        mod1.mix_mode='ADD'
                        mod1.mix_set='ALL'
                        mod1.vertex_group_a=key+"L"
                        mod1.vertex_group_b=group+"L"
                        mod1.show_expanded = False
                        isLeftorRightUsed[0] = False
                    if item.vertex_groups.find(group+"R") != -1:
                        mod2 = item.modifiers.new(key+"R+"+group+"R",type="VERTEX_WEIGHT_MIX")
                        mod2.mix_mode='ADD'
                        mod2.mix_set='ALL'
                        mod2.vertex_group_a=key+"R"
                        mod2.vertex_group_b=group+"R"
                        mod2.show_expanded = False
                        isLeftorRightUsed[1]= False
                else:
                    if item.vertex_groups.find(group) == -1:
                        continue
                    mod = item.modifiers.new(key+"+"+group,type="VERTEX_WEIGHT_MIX")
                    mod.mix_mode='ADD'
                    mod.mix_set='ALL'
                    mod.vertex_group_a=key
                    mod.vertex_group_b=group
                    mod.show_expanded = False
                Nogroups = False
            if Nogroups:
                if value["L/R"]:
                        if isLeftorRightUsed[0]:
                            item.vertex_groups.remove(item.vertex_groups[key+"L"])
                        if isLeftorRightUsed[1]:
                            item.vertex_groups.remove(item.vertex_groups[key+"R"])
                else:
                    item.vertex_groups.remove(item.vertex_groups[key])
        if props.applyMods:
            apply_modifiers(item)

def register():
    classes = [COM3D2GroupConverter,ExecuteVertexRemapping,COM3D2ObjectProperties]
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.COM3D2objectProperties = bpy.props.PointerProperty(
            type=COM3D2ObjectProperties)


def unregister():
    classes = [COM3D2GroupConverter,ExecuteVertexRemapping,COM3D2ObjectProperties]
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.COM3D2objectProperties

if __name__ == "__main__":
    register()