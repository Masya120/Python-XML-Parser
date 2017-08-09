import xml.etree.ElementTree as ET


class Xml_Parser(object):


    def parser_method(self, xmlCont):

        tree = ET.fromstring(str(xmlCont))

        for child in tree.findall('Abbr'):
            sendMode = child.find('./SendConfiguration/AddressInfo/SendMode')
            if(sendMode.text == "Fax"):
                entryNum = child.find('AbbrNo').text
                entryName = child.find('Name').text
                faxNumber = child.find('./SendConfiguration/AddressInfo/FaxMode/PhoneNumber')

                outputFile = open('result_1', 'a')
                outputFile.write("%s: %s , Type: %s , Number: %s \n" % (entryNum, entryName, sendMode.text, faxNumber.text))
                outputFile.close()

                #print("%s: %s , %s , Number: %s" % (entryNum, entryName, sendMode.text, faxNumber.text))