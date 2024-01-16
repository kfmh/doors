import os
import pkg_resources


class FileManager:
    def __init__(self):
        pass

    def filepath_list(self, directory:str, exclude_files:list):
        """Creates a list of files path from a directory"""
        dir = pkg_resources.resource_filename(__name__, directory)
        file_paths = [os.path.join(dir, f) for f in os.listdir(dir)
                      if f not in exclude_files]
        return file_paths
