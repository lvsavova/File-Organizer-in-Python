import unittest

from organizer import Organizer
from collections import defaultdict


class TestValidateOrganization(unittest.TestCase):

    def test_valid_extension_organization(self):
        file_list = ['file1.docx',
                     'file2.exe.exe', 'file3.docx.exe',
                     'file5.sdx',
                     'some.power']
        organizer = Organizer('C:')
        organizer.file_list = file_list

        files_by_extensions = organizer.organize_by_extension()

        self.assertCountEqual(files_by_extensions['exe'], ['file2.exe.exe',
                                                           'file3.docx.exe'])
        self.assertCountEqual(files_by_extensions['docx'], ['file1.docx'])
        self.assertCountEqual(files_by_extensions['power'], ['some.power'])

    def test_valid_type_organization(self):
        file_list = ['file.doc', 'file.docx', 'file.pdf',
                     'song.mp3', 'song.wav',
                     'some torrent.torrent',
                     'picture.png', 'picture.jpg',
                     'exec.exe', 'exec.bin', 'exec.app',
                     'exec.osx', 'exec.msi',
                     'presentation.pptx']

        organizer = Organizer('C:')
        organizer.file_list = file_list

        files_by_type = organizer.organize_by_type()

        self.assertCountEqual(files_by_type['Documents'],
                                           ['file.doc', 'file.docx',
                                            'file.pdf'])
        self.assertCountEqual(files_by_type['Music'],
                                           ['song.wav', 'song.mp3'])
        self.assertCountEqual(files_by_type['Torrents'],
                                           ['some torrent.torrent'])
        self.assertCountEqual(files_by_type['Pictures'],
                                           ['picture.png', 'picture.jpg'])
        self.assertCountEqual(files_by_type['Executables'],
                                           ['exec.exe', 'exec.bin',
                                            'exec.app', 'exec.osx',
                                            'exec.msi'])
        self.assertCountEqual(files_by_type['Presentations'],
                                           ['presentation.pptx'])

if __name__ == '__main__':
    unittest.main()
