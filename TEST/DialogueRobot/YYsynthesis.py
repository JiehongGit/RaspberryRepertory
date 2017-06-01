#coding: utf-8
import sys 
import urllib2 
import json 
import os 
import YYrecognition

reload(sys) 
sys.setdefaultencoding("utf-8")

def YYsynthesis_api(tok,tex): 
	cuid = "XX-XX-XX-XX-XX-XX"
	spd = "4" 
	url = "http://tsn.baidu.com/text2audio?tex="+tex+"&lan=zh&cuid="+cuid+"&ctp=1&tok="+tok+"&per=3"
	#print url 
	#response = requests.get(url) 
	#date = response.read() 
	return url

def tts_main(filename,words,tok): 
	voice_date = YYsynthesis_api(tok,words)
	f = open(filename,"wb")
	f.write(voice_date)
	f.close()
