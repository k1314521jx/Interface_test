import os
import codecs
import configparser

#codecs 自然语言编码转换模块，由于python中默认的编码是ascii，
#如果直接使用open方法得到文件对象然后进行文件的读写，都将无法使用包含中文字符（以及其他非ascii码字符）

#configparser  读写配置文件ini

proDir = os.path.split(os.path.realpath(__file__))[0] #在.py文件的完整路径 等同于os.path.dirname(__file__)
configPath = os.path.join(proDir, "config.ini")


class ReadConfig(object):
    def __init__(self):  
        fd = open(configPath)
        data = fd.read()

        #  remove BOM BOM：BOM头是放在UTF-8编码的文件的头部的，占用三个字节，用来标识该文件属于UTF-8编码。现在已经有很多软件识别BOM头，但是还有些不能识别BOM头，比如PHP就不能识别BOM头
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_headers(self, name):
        value = self.cf.get("HEADERS", name)
        return value

    def set_headers(self, name, value):
        self.cf.set("HEADERS", name, value)
        with open(configPath, 'w+') as f:
            self.cf.write(f)

    def get_url(self, name):
        value = self.cf.get("URL", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value
        

# if __name__ == '__main__':
    # print(ReadConfig().get_db_T134('host'))
 
 
 
 


