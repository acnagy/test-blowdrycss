from os import chdir, getcwd, path
from datetime import datetime
# custom classes
from filehandler import FileFinder, CSSFile, GenericFile
from htmlattributeparser import HTMLClassParser
from classpropertyparser import ClassPropertyParser
from cssbuilder import CSSBuilder
from datalibrary import clashing_alias_markdown, property_alias_markdown, clashing_alias_html, property_alias_html
__author__ = 'chad nelson'
__project__ = 'blow dry css'


def main():
    # Set project_directory to the one containing the files you want to DRY out.
    # In this case it is set to the "examplesite" by default for demonstration purposes.
    chdir('..')                                                 # Navigate up one directory relative to this script.
    project_directory = path.join(getcwd() + '\\examplesite')    # Change to whatever you want.
    css_directory = path.join(project_directory + '\\css')

    # Generate Markdown documentation files.
    generic_file = GenericFile(file_directory=getcwd(), file_name='clashing_aliases')
    generic_file.write_file(clashing_alias_markdown, extension='.md')
    generic_file.file_name = 'property_aliases'                     # Changes file name.
    generic_file.write_file(property_alias_markdown, extension='.md')

    # Generate HTML documentation files. (This location is important since it allows encoded css to be included.)
    generic_file.file_directory = project_directory                 # Change directory to /examplesite
    generic_file.file_name = 'clashing_aliases'                     # Change file name.
    generic_file.write_file(clashing_alias_html, extension='.html')
    generic_file.file_name = 'property_aliases'                     # Change file name.
    generic_file.write_file(property_alias_html, extension='.html')

    # Define File all file types/extensions to search for in project_directory
    file_types = ('*.html', '*.aspx', '*.master', '*.ascx')

    # Get all files associated with defined file_types in project_directory
    file_finder = FileFinder(project_directory=project_directory, file_types=file_types)

    # Get set of all defined classes
    class_parser = HTMLClassParser(files=file_finder.files)

    # Filter class names only keeping classes that match the defined class encoding.
    class_property_parser = ClassPropertyParser(class_set=class_parser.class_set)
    # print('\nclass_property_parser.class_set:', class_property_parser.class_set)

    # Build a set() of valid css properties. Some classes may be removed during cssutils validation.
    css_builder = CSSBuilder(property_parser=class_property_parser)
    css_text = css_builder.get_css_text()
    # print('CSS Text:')
    # print(css_text)

    # Output the DRY CSS file. (user command option)
    css_file = CSSFile(file_directory=css_directory, file_name='blowdry')
    css_file.write_css(css_text=css_text)
    print(css_directory + css_file.file_name + '.css', "created.")

    # Output the Minified DRY CSS file. (user command option)
    css_file.minify(css_text=css_text)
    print(css_directory + css_file.file_name + '.min.css', "created.")
    print('--- Completed @', datetime.now(), '---')


if __name__ == '__main__':
    main()
