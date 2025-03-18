from .nodes import LoadTheraModel, TheraProcess
 
NODE_CLASS_MAPPINGS = { 
    "LoadTheraModel" : LoadTheraModel,
    "TheraProcess" : TheraProcess
}

NODE_DISPLAY_NAME_MAPPINGS = {
     "LoadTheraModel" : "Load InvSR Models",
     "TheraProcess" : "Thera Process"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']