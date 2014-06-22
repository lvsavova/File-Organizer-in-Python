from organizer import Organizer
from collections import defaultdict
import shutil
import os


class FolderReorganizer:
    source_folder_path = ""
    target_folder_path = ""
    match_strings = []

    def __init__(self, source_folder_path, target_folder_path):
        self.source_folder_path = source_folder_path
        self.target_folder_path = target_folder_path

    def create_new_dirs(self, organization, path):
        for type in organization:
            new_dir_path = path + "\\" + type
            if os.path.exists(new_dir_path) is False:
                os.mkdir(new_dir_path)

    def copy_files(self, file_list, destination_folder):
        for file in file_list:
            destination = destination_folder + "\\" + file
            source = self.source_folder_path + "\\" + file
            shutil.copy(source, destination)

    def reorganize(self, type_of_reorganization):
        organizer = Organizer(self.source_folder_path)
        organization = defaultdict(list)

        if type_of_reorganization == 'extension':
            organization = organizer.organize_by_esxtension()

        if type_of_reorganization == 'type':
            organization = organizer.organize_by_type()

        if type_of_reorganization == 'content':
            organization = organizer.organize_by_content(self.match_strings)

        type_folder = self.target_folder_path + "\\" + type_of_reorganization
        if os.path.exists(type_folder) is False:
            os.mkdir(type_folder)
        self.create_new_dirs(organization, type_folder)
        for folder_name in organization:
            self.copy_files(organization[folder_name], type_folder + "\\" + folder_name)
