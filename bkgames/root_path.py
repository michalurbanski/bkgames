# Temporary solution for AutoFinder, to be fixed.
import os

file_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.abspath(os.path.join(file_path, os.pardir))
ROOT_PATH = os.path.abspath(os.path.join(parent_path, os.pardir))
