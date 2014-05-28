import os
import sys
import re
import mimetypes
from collections import defaultdict


class Organizer:

    file_list = []

    def __init__(self, directory):
        self.directory = directory
        self.file_list = os.listdir(directory)

    def organize_by_esxtension(self):
        files_by_extensions = defaultdict(list)

        pattern_file_name = r'.+(?=\.)|^[^\.]+\Z'
        pattern_extension = r'(?:\.).+'

        for file in self.file_list:
            list_potential_extenions = re.findall(pattern_extension, file)
            if len(list_potential_extenions) > 0:
                extension = list_potential_extenions[len(list_potential_extenions)-1]
            else:
                extension = ""
            file_name = re.match(pattern_file_name, file, flags=0).group()
            if extension is not "":
                files_by_extensions[extension].append(file_name)
            else:
                files_by_extensions["No extension"] = file_name

        return files_by_extensions

    def organize_by_type(self):
        files_by_type = defaultdict(list)

        for file in self.file_list:
            mime_type = mimetypes.guess_type(file, strict=True)[0]
            files_by_type[mime_type].append(file)
        return files_by_type
