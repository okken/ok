import importlib.metadata

__all__ = ["__version__", "version_tuple"]

__version__ = importlib.metadata.version('ok')
version_tuple = tuple([ int(num) for num in __version__.split('.')])
