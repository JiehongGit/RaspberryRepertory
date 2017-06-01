#-*- coding: utf-8 -*-
import sys
reload(sys)
from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
import time
sys.setdefaultencoding( "utf-8" )

import RPi.GPIO as GPIO
from time import sleep

#from work import main
from work import get_weather
from work import text2voice
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import re
import time
import requests
from datetime import datetime,timedelta
from bs4 import BeautifulSoup
import work

def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13,GPIO.OUT)
    pass
def beep():
    GPIO.output(13,GPIO.LOW)


        
#将需要识别的图片和集合对比
#------------------------------------------------------------------------------
#Face++人脸识别准备阶段
API_KEY = "feI5hwgMw9zQKaDmDCjq1SFdVZynhy38"
API_SECRET = "y8NTlkYNLJQOmGErZzGUnegmUZROER0r"
#国际版的服务器地址
api_server_international = 'https://api-us.faceplusplus.com/facepp/v3/'

#------------------------------------------------------------------------------
#七牛云上传图片准备阶段
#需要填写你的 Access Key 和 Secret Key
access_key = 'tCDfRDFsEs5goiRLPr-tXxy4zHZ_9IiTO08VJx9S'
secret_key = 'HS8j9J99pGQehABaj2HhRJMr-wTbIWoWnQM-FEls'
#构建鉴权对象
q = Auth(access_key, secret_key)
#要上传的空间
bucket_name = 'camera'
#上传到七牛后保存的文件名（以时间作为图片的命名）
key = '%s/%s/%s/%s:%s:%s.jpg'%(time.localtime()[0],time.localtime()[1],time.localtime()[2],time.localtime()[3],time.localtime()[4],time.localtime()[5])
#生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 3600)


# 导入系统库并定义辅助函数
from pprint import pformat
def print_result(hit, result):
    def encode(obj):
        if type(obj) is unicode:
            return obj.encode('utf-8')
        if type(obj) is dict:
            return {encode(v): encode(k) for (v, k) in obj.iteritems()}
        if type(obj) is list:
            return [encode(i) for i in obj]
        return obj
    print hit
    result = encode(result)
    print '\n'.join("  " + i for i in pformat(result, width=75).split('\n'))
#导入SDK中的API类
from facepp import API, File
#创建一个API对象
api = API(API_KEY, API_SECRET)

#-----------------------------------------------------------------------------
# 本地图片的地址
face_search = './foo.jpg'
# 对待比对的图片进行检测
Face = {}
res = api.detect(image_file=File(face_search))
#print_result("face_search", res)
#搜索相似脸
search_result = api.search(face_token=res["faces"][0]["face_token"], outer_id='gtl')
# 输出结果
search_confidence = search_result['results'][0]['confidence']
uers=search_result['results'][0]['user_id']
print '置信度:', search_confidence
if search_confidence >=80:
    #print '你好!',uers.decode('utf-8')
    
    text = '你好! %s!%s'% \
           (uers.decode('utf-8'),get_weather())
    print(text)
    #text2voice(text)
    #mp3path1 = os.path.join(os.path.dirname(__file__), '1.mp3')
    #os.system('mplayer %s' % mp3path1)
    #os.remove(mp3path1)
    
    
else:
    print '何方妖孽！'
    init()
    print '警报响起！'
    beep()
    time.sleep(5)
    localfile = './foo.jpg'
    ret, info = put_file(token, key, localfile)
    assert ret['key'] == key
    assert ret['hash'] == etag(localfile)

GPIO.cleanup()
