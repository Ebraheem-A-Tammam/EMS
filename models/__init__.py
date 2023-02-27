import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(BASE_DIR)

from .console import console
from .course import course
from .doctor import doctor
from .student import student