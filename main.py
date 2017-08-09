import parser_class
import xml_getter


xfile = xml_getter.Xml_Get_File()

parse_this = parser_class.Xml_Parser()

parse_this.parser_method(xfile.file_reader('test.xml'))


# https://www.w3schools.com/xml/note.xml