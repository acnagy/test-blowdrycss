# builtin
from unittest import TestCase, main
from os import path, getcwd
# custom
from blowdrycss.filehandler import FileFinder
from blowdrycss.classparser import ClassParser


class TestGeneralClassParser(TestCase):
    def test_build_file_path_list(self):
        original_cwd = getcwd()

        if original_cwd.endswith('unit_tests'):                     # Allows running of pycharm unittest.
            import blowdrycss.blowdrycss_settings as settings
            cwd = original_cwd
        else:                                                       # Run unittest cmd from the root directory.
            import blowdrycss_settings as settings
            cwd = path.join(original_cwd, 'blowdrycss', 'unit_tests')
        
        expected_file_paths = {
            path.join(cwd, 'test_aspx', 'test.aspx'),
            path.join(cwd, 'test_jinja', 'test.jinja2'),
        }

        project_directory = cwd

        settings.file_types = ('*.html', '*.aspx', '*.jinja2')                              # Override file_types
        file_finder = FileFinder(project_directory=project_directory)
        self.assertTrue('.aspx' in list(file_finder.file_dict), msg=settings.file_types)
        class_parser = ClassParser(file_dict=file_finder.file_dict)
        self.assertEqual(set(class_parser.file_path_list), expected_file_paths, msg=class_parser.file_path_list)
        settings.file_types = ('*.html', )                                                  # Reset file_types


if __name__ == '__main__':
    main()


