import configparser
from folderorganizator import FolderReorganizer

properties = configparser.ConfigParser()
properties.read("config.ini")

directory = properties['directory']['DirectoryPath']
type_of_reorganization = properties['orgtype']['ReorganizationType']
match_content = properties['content']['SearchedText']

fileorg = FolderReorganizer(directory)
fileorg.match_string = match_content
fileorg.reorganize(type_of_reorganization)
