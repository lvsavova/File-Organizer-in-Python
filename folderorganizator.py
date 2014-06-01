from organizer import Organizer
from collections import defaultdict
import shutil
import os


class FolderReorganizer:
    folder_path = ""

    def __init__(self, folder_path):
        self.folder_path = folder_path

    def create_new_dirs(self, organization, path):
        for type in organization:
            new_dir_path = path + "\\" + type
            if os.path.exists(new_dir_path) is False:
                os.mkdir(new_dir_path)

    def move_files(self, file_list, folder_name):
        for file in file_list:
            destination = self.folder_path + "\\" + folder_name + "\\" + file
            source = self.folder_path + "\\" + file
            shutil.move(source, destination)

    def reorganize(self, type_of_reorganization):
        organizer = Organizer(self.folder_path)
        organization = defaultdict(list)

        if type_of_reorganization == 'extension':
            organization = organizer.organize_by_esxtension()

        if type_of_reorganization == 'type':
            organization = organizer.organize_by_type()

        self.create_new_dirs(organization, self.folder_path)
        for folder_name in organization:
            self.move_files(organization[folder_name], folder_name)
