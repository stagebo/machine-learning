import urllib
import time
import os
import sys
import requests

index = 0
def get_save_img(url,file_name):
    global index
    img_folder = "../../img/%s/"%(index//500)
    if not os.path.exists(img_folder):
        os.makedirs(img_folder)
    urls = url.split("/")
    content = requests.get(url).content
    path = img_folder + str(file_name) + ".jpg"
    f = open(path, "wb")
    f.write(content)
    print('download done:%s'%file_name)
    index += 1
if __name__ == "__main__":
    for i in range(999999999-100000901):
        file_name = str(i+100000901)
        url = 'https://shp.qlogo.cn/ttsing/1/%s/100' % file_name

        get_save_img(url,file_name)