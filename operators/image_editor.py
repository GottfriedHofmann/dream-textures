import bpy

class NextImage(bpy.types.Operator):
    """Switch to next image"""
    bl_idname = 'image.next_image'
    bl_label = 'Next Image'

    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.type == 'IMAGE_EDITOR'

    def execute(self, context):
        space = context.space_data
        images = bpy.data.images
        current_image_index = images.find(space.image.name)
        next_image_index = (current_image_index + 1) % len(images)
        space.image = images[next_image_index]
        return {'FINISHED'}

class PrevImage(bpy.types.Operator):
    """Switch to previous image"""
    bl_idname = 'image.prev_image'
    bl_label = 'Previous Image'

    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.type == 'IMAGE_EDITOR'

    def execute(self, context):
            space = context.space_data
            images = bpy.data.images
            current_image_index = images.find(space.image.name)
            prev_image_index = (current_image_index - 1) % len(images)
            space.image = images[prev_image_index]
            return {'FINISHED'}