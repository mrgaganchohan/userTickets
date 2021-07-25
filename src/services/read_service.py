import json
import os
import glob


class ReadFilesFromFolder:
    def __init__(self):
        pass

    def read(self, file_path):
        """
            reads single file and puts it to memory, not used in code,
            but good to have if needed.
        Args:
            file_path (str): contains exact location of a file e.g. path/to/file.json

        Returns:
            []: returns file's data in python readable format, in this case array or a list
        """
        # reads single file_path
        with open(file_path) as f:
            data = json.load(f)
        return data

    def read_all_files_directory(self, directory):
        """combines data from a diectory into one variable

        Args:
            directory (str): location of a directory /path/to/directory
            directory contains all user or tickets files

        Returns:
            []: python readable format
        """
        json_pattern = os.path.join(directory, "*.json")
        file_list = glob.glob(json_pattern)
        combined_data = []
        for file in file_list:
            with open(file) as f:
                combined_data.extend(json.load(f))
        return combined_data
