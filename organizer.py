import os
import os.path
import sys
import re
import mimetypes
from collections import defaultdict
from documenthandler import DocumentHandler


FILE_TYPES = {'Presentations': ['pptx', 'ppt'],
              'Documents': ['pdf', 'docx', 'doc'],
              'Text Files': ['txt'],
              'Executables': ['exe', 'bat', 'bin', 'app', 'osx', 'msi'],
              'Torrents': ['torrent'],
              'Music': ['mp3', 'wav'],
              'Pictures': ['png', 'jpg', 'jpeg']}


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
                if extension == '':
                    files_by_extensions["no extension"].append(file)
        return files_by_extensions

    def organize_by_type(self):
        files_by_type = defaultdict(list)
        files_by_extensions = self.organize_by_esxtension()

        for extension in files_by_extensions:
            for file_type in FILE_TYPES:
                if extension in FILE_TYPES[file_type]:
                    files_by_type[file_type] += files_by_extensions[extension]

        return files_by_type

    def organize_by_content(self, match_strings):
        files_by_content = defaultdict(list)
        files_by_extensions = self.organize_by_esxtension()
        docx_files = files_by_extensions['docx']
        doc_handler = DocumentHandler()
        for file in docx_files:
            for string in match_strings:
                if doc_handler.search_content(self.directory + "\\" + file, string) is True:
                    files_by_content[string].append(file)
        return files_by_content
