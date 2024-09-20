import importlib.metadata


version = importlib.metadata.version('ok')
__version__ = version
version_tuple = tuple([ int(num) for num in __version__.split('.')])