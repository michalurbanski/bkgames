import os
from os import listdir
from os.path import isfile


class Autofinder:
    """Autofinder automatically searches for an input file."""

    def __init__(self, folder_path: str):
        self._folder_path = folder_path

    def find_input_file(self) -> str:
        if(Autofinder._does_folder_path_exist(self._folder_path)):

            only_files: list = [f for f in listdir(
                self._folder_path) if isfile(os.path.join(self._folder_path, f))]

            if not only_files:
                raise Exception(
                    "Autofinder: No file with input data can be found")

            # Files have naming convention based on year, like:
            # s2021.dat
            # s2020.dat
            # If we sort files in the reverse order, then to get the most recent
            # one, we can just get the first one from the sort result.
            only_files.sort(reverse=True)

            return os.path.join(self._folder_path, only_files[0])
        else:
            raise ValueError("Autofinder: Provided path does not exist")

    @staticmethod
    def _does_folder_path_exist(path: str) -> bool:
        return os.path.exists(path)
