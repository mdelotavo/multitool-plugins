plugins = []

from .encrypt import encrypt
plugins.append('encrypt')

__all__ = []
for plugin in plugins:
    __all__.append(plugin)
