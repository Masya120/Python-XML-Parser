import parser_class
import xml_getter
import os


xfile = xml_getter.Xml_Get_File()

parse_this = parser_class.Xml_Parser()

# Can be to a directory or a specific file
path = './test/'

for filename in os.listdir(path):
    parse_this.parser_method(xfile.file_reader(path + filename), str(filename))
