'''
Created by Samuel B

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {
    "name": "Active swap",
    "description": "Allow to iterate active object over selected with shortcuts (shift+`: next, ctrl+shift+` : prev)",
    "author": "Samuel Bernou",
    "version": (0, 0, 1),
    "blender": (2, 77, 0),
    "location": "View3D",
    "warning": "This addon is still in development.",
    "wiki_url": "",
    "category": "Object" }

import bpy
import bmesh

C = bpy.context

def AS_SwapObject(state):
    '''swap Active object to next or previous according to parameter (1 or -1)'''
    
    ###control > what to do if only one object selected
    ###if possible find selection order (selection history ?)

    #OBJECT MODE - swap active or deselect active
    if C.mode == 'OBJECT':
        if C.selected_objects:
            if len(C.selected_objects) > 1:
                if state: #swap
                    #objs = C.selected_objects
                    #act = C.active_object
                    #pos =  objs.index(act)
                    #C.scene.objects.active = objs[(pos+1) % len(objs)]
                    
                    C.scene.objects.active = C.selected_objects[\
                    (C.selected_objects.index(C.active_object)+state) % len(C.selected_objects)]
                
                else: # deselect and pass to nextActive
                    current = C.scene.objects.active
                    C.scene.objects.active = C.selected_objects[\
                    (C.selected_objects.index(C.active_object)+1) % len(C.selected_objects)]
                    current.select = False

            else:
                pass #dont do anything
                # print("only one object selected (needs at least two to swap active)")
        else:
            pass
            # print("no object selected")
    
    #EDIT MODE - swap active vertex/edge/face or deselect it
    elif C.mode == 'EDIT_MESH':
        pass
        # bm = bmesh.from_edit_mesh(bpy.context.active_object.data)

        # if 'VERT' in bm.select_mode: #vertex ##check selection mode C.scene.tool_settings.mesh_select_mode[0] == True
        #     active_vert = bm.select_history[-1]

        # elif 'EDGE' in bm.select_mode: #edges
        #     pass
        # else : #faces
    elif C.mode == 'EDIT_ARMATURE':
        pass
        # if C.selected_bones:
        #     if len(C.selected_bones) > 1:
        #         if state:
        #             C.active_bone = C.selected_bones[\
        #             (C.selected_bones.index(C.active_bone)+state) % len(C.selected_bones)]
        #         else:
        #             current = C.active_bone
        #             C.active_bone = C.selected_bones[\
        #             (C.selected_bones.index(C.active_bone)+state) % len(C.selected_bones)]
        #             current.select = False


    elif C.mode == 'POSE':
        pass
        # if C.selected_pose_bones:
        #     if len(C.selected_pose_bones) > 1:
        #         if state:
        #             C.active_pose_bone = C.selected_pose_bones[\
        #             (C.selected_pose_bones.index(C.active_pose_bone)+state) % len(C.selected_pose_bones)]
        #         else:
        #             current = C.active_pose_bone
        #             C.active_pose_bone = C.selected_pose_bones[\
        #             (C.selected_pose_bones.index(C.active_pose_bone)+state) % len(C.selected_pose_bones)]
        #             current.select = False




class AS_DeselectActive(bpy.types.Operator):
    bl_idname = "view3d.deselect_active"
    bl_label = "Deselect Active"
    bl_description = "Delelect active and set next item in selection to active"
    bl_options = {"REGISTER"}
    
    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        AS_SwapObject(0)
        return {"FINISHED"}    

class AS_ActiveNext(bpy.types.Operator):
    bl_idname = "view3d.as_active_next"
    bl_label = "Active Next"
    bl_description = "Active next item in selection"
    bl_options = {"REGISTER"}
    
    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        AS_SwapObject(1)
        return {"FINISHED"}


class AS_ActivePrev(bpy.types.Operator):
    bl_idname = "view3d.as_active_prev"
    bl_label = "Active Prev"
    bl_description = "Active previous item in selection"
    bl_options = {"REGISTER"}
 
    @classmethod
    def poll(cls, context):
        return True
 
    def execute(self, context):
        AS_SwapObject(-1)
        return {"FINISHED"}

###---keymap---------------

addon_keymaps = []
def register_keymaps():
    addon = bpy.context.window_manager.keyconfigs.addon
    km = addon.keymaps.new(name = "3D View", space_type = "VIEW_3D")
    kmi = km.keymap_items.new("view3d.as_active_next", type = "ACCENT_GRAVE", value = "PRESS", shift = True)
    kmi = km.keymap_items.new("view3d.as_active_prev", type = "ACCENT_GRAVE", value = "PRESS", shift = True, ctrl = True)
    kmi = km.keymap_items.new("view3d.deselect_active", type = "ACCENT_GRAVE", value = "PRESS", shift = True, alt = True)
    addon_keymaps.append(km)


def unregister_keymaps():
    wm = bpy.context.window_manager
    for km in addon_keymaps:
        for kmi in km.keymap_items:
            km.keymap_items.remove(kmi)
        wm.keyconfigs.addon.keymaps.remove(km)
    addon_keymaps.clear()


###---register--------------

def register():
    register_keymaps()
    bpy.utils.register_module(__name__)

def unregister():
    unregister_keymaps()
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
