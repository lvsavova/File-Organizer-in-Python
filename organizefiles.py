import configparser
from folderorganizator import FolderReorganizer


def main():
    properties = configparser.ConfigParser()
    properties.read("config.ini")

    source_directory = properties['Directory']['SourceDirectoryPath']
    target_directory = properties['Directory']['TargetDirectoryPath']

    type_of_reorganization = properties['Orgtype']['ReorganizationType']
    match_contents = properties['Content']['SearchedText'].split(";")

    fileorg = FolderReorganizer(source_directory, target_directory)
    fileorg.match_strings = match_contents
    fileorg.reorganize(type_of_reorganization)

if __name__ == "__main__":
    main()
