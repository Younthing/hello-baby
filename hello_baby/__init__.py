"""init file"""

try:
    from importlib.metadata import version as get_version

    __version__ = get_version("hello-baby")
except ImportError:
    __version__ = "0.0.0"
