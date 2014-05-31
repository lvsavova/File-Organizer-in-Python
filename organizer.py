import os
import os.path
import sys
import re
import mimetypes
from collections import defaultdict

FILE_TYPES = {'Presentations': ['pptx', 'ppt'],
              'Documents': ['pdf', 'docx', 'doc'],
              'Text Files': ['txt'],
              'Executables': ['exe', 'bat', 'bin', 'app', 'osx', 'msi'],
              'Torrents': ['torrent'],
              'Music': ['mp3', 'wav']}


class Organizer:

    file_list = []

    def __init__(self, directory):
        self.directory = directory
        self.file_list = os.listdir(directory)

    def organize_by_esxtension(self):
        files_by_extensions = defaultdict(list)

        for file in self.file_list:
                extension = os.path.splitext(file)[1].split('.')[-1]
                files_by_extensions[extension].append(file)
        return files_by_extensions

    def organize_by_mime_type(self):
        files_by_mime_type = defaultdict(list)

        for file in self.file_list:
            mime_type = mimetypes.guess_type(file, strict=True)[0]
            files_by_mime_type[mime_type].append(file)
        return files_by_mime_type

    def organize_by_type(self):
        files_by_type = defaultdict(list)
        files_by_extensions = self.organize_by_esxtension()
        print(files_by_extensions)
        for extension in files_by_extensions:
            for file_type in FILE_TYPES:
                if extension in FILE_TYPES[file_type]:
                    files_by_type[file_type] += files_by_extensions[extension]

        return files_by_type
