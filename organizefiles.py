import configparser
from folderorganizator import FolderReorganizer

properties = configparser.ConfigParser()
properties.read("config.ini")

source_directory = properties['directory']['SourceDirectoryPath']
target_directory = properties['directory']['TargetDirectoryPath']

type_of_reorganization = properties['orgtype']['ReorganizationType']
match_contents = properties['content']['SearchedText'].split(";")


fileorg = FolderReorganizer(source_directory, target_directory)
fileorg.match_strings = match_contents
fileorg.reorganize(type_of_reorganization)
