import xml.etree.ElementTree as ET


class Xml_Parser(object):


    def parser_method(self, xmlCont, fileName):

        tree = ET.fromstring(str(xmlCont))

        # The code below would need to be swapped for something specific to what your looking for. Left here as an example.
        for child in tree.findall('Abbr'):
            sendMode = child.find('./SendConfiguration/AddressInfo/SendMode')
            if(sendMode.text == "Fax"):
                entryNum = child.find('AbbrNo').text
                entryName = child.find('Name').text
                faxNumber = child.find('./SendConfiguration/AddressInfo/FaxMode/PhoneNumber')

                outputFile = open('result - %s' % fileName, 'a')
                outputFile.write("%s: %s , Type: %s , Number: %s  \n\n" % (entryNum, entryName, sendMode.text, faxNumber.text))
                outputFile.close()

        print("Parsed " + fileName)   
