print("Inicializando el paquete app...")

__all__ = [
    'config',
    'usuarios'
]

from . import config
from . import usuarios

VERSION = "1.1.0"