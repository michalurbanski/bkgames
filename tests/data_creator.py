import os
import uuid
from tests.data_creator_action import DataCreatorAction
from typing import List


class DataCreator:
    def __init__(self):
        self._creation_actions: List[DataCreatorAction] = []
        self._cleanup_actions: List[DataCreatorAction] = []
        self._folder_name = str(uuid.uuid1())
        self._file_path = os.path.join(self._folder_name, "input.txt")
        self._folder_creation_requested = False

    @property
    def folder_name(self):
        return self._folder_name

    @property
    def file_path(self):
        return self._file_path

    def create_folder(self):

        self._creation_actions.append(
            DataCreatorAction(self._create_folder_action(),
                              priority_for_creation=1))
        self._cleanup_actions.append(
            DataCreatorAction(self._remove_folder_action()))
        self._folder_creation_requested = True
        return self

    def create_file_with_data(self):
        # Note: in the current, simple, implementation, sufficient for now,
        # file has to exist inside a folder.
        if not self._folder_creation_requested:
            self.create_folder()

        self._creation_actions.append(
            DataCreatorAction(self._create_file_with_data_action()))
        self._cleanup_actions.append(
            DataCreatorAction(self._remove_file_with_data_action(),
                              priority_for_removal=1))
        return self

    def execute(self):
        """ Executes previously scheduled actions."""
        col = sorted(self._creation_actions,
                     key=lambda x: x.priority_for_creation)
        for f in col:
            f.func()

    def cleanup(self):
        """ Cleans up after executed actions - by design in the reverse order."""
        col = sorted(self._cleanup_actions,
                     key=lambda x: x.priority_for_removal)
        for f in col:
            f.func()

    def _create_folder_action(self):
        def body():
            os.mkdir(self._folder_name)
        return body

    def _remove_folder_action(self):
        def body():
            os.rmdir(self._folder_name)
        return body

    def _create_file_with_data_action(self):
        def body():
            with open(self._file_path, mode='w') as f:
                f.write("DONE - Nba game 16.10 phi at bos -> bos?\n")
                f.write("DONE - Nba game 17.10 dal at phx -> phx\n")
        return body

    def _remove_file_with_data_action(self):
        def body():
            os.remove(self._file_path)
        return body
