import requests


class Xml_Get_Network(object):

    def net_request(self, url):
        r = requests.get(str(url)) 
        return r.text

class Xml_Get_File(object):

    def file_reader(self, filePath):
        file_open = open(filePath,'r')
        file_cont = file_open.read()

        file_open.close()

        return file_cont