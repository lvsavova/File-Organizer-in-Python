import configparser
from folderorganizator import FolderReorganizer


properties = configparser.ConfigParser()
properties.read("config.ini")

directory = properties['directory']['DirectoryPath']
type_of_reorganization = properties['orgtype']['ReorganizationType']

fileorg = FolderReorganizer(directory)
fileorg.reorganize(type_of_reorganization)
