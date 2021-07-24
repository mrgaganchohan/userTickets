import json 
import os 
import glob
class ReadFiles:
    def __init__(self):
        pass
    # TODO: add karg here
    def read(self):
        pass

class ReadFilesFromFolder(ReadFiles):
    # used for reading multiple files from a folder
    def __init__(self):
        pass
    def read(self, file ):
        # reads single file
        with open(file) as f:
            data = json.load(f)
        return data
    def read_all_files_directory(self, directory):
        json_pattern = os.path.join(directory, '*.json')
        file_list = glob.glob(json_pattern)
        print("part 1 ")
        combined_data = []
        for file in file_list:
            with open(file) as f:
                combined_data.extend(json.load(f))
        return combined_data
