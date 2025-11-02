from os import path


class FileUtilities:
    @staticmethod
    def is_folder_exists(folder_path: str) -> bool:
        return path.exists(folder_path) and path.isdir(folder_path)
