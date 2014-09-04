import os
import os.path
import sys
import re
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
    """
    Implements the logic by which files are organized.
    Has an attribute - list of file names, which are
    indeed the file names of the directory we would like
    to have organized (source directory)
    """
    file_list = []

    def __init__(self, directory):
        """
        Initializes the source directory associated
        with the Organizer object.
        """
        self.directory = directory
        self.file_list = os.listdir(directory)

    def organize_by_extension(self):
        """
        Iterates through all the files in the source directory and
        returns a dictionary with key the file extension and value -
        list of file names that have this extension
        """
        files_by_extensions = defaultdict(list)
        for file in self.file_list:
                extension = os.path.splitext(file)[1].split('.')[-1]
                files_by_extensions[extension].append(file)
                if extension == '':
                    files_by_extensions["no extension"].append(file)
        return files_by_extensions

    def organize_by_type(self):
        """
        Iterates through all the files in the source directory and
        returns a dictionary with key the file type and value -
        list of file names that are of this type.
        Types of files are defined in FILES_TYPE dict.
        """
        files_by_type = defaultdict(list)
        files_by_extensions = self.organize_by_extension()
        for extension in files_by_extensions:
            for file_type in FILE_TYPES:
                if extension in FILE_TYPES[file_type]:
                    files_by_type[file_type] += files_by_extensions[extension]
        return files_by_type

    def organize_by_content(self, match_strings):
        """
        Iterates through all the files in the source directory and
        returns a dictionary with key the string we want to
        match and values- the docx files containing the string
        """
        files_by_content = defaultdict(list)
        files_by_extensions = self.organize_by_extension()
        docx_files = files_by_extensions['docx']
        doc_handler = DocumentHandler()
        for file in docx_files:
            for string in match_strings:
                if doc_handler.search_content(self.directory +
                                              "\\" + file, string) is True:
                    files_by_content[string].append(file)
        return files_by_content
