#-*- coding: utf-8 -*-

#把已知人脸添加到人脸集合中

#------------------------------------------------------------------------------
#准备阶段
API_KEY = "0IbBJA_Q_jlLawnmMYC8kFQpTSbMQD6Q"
API_SECRET = "KAxMY5T7OMXYVpv5q2O8LxhKhOTTcVNV"
#国际版的服务器地址
api_server_international = 'https://api-us.faceplusplus.com/facepp/v3/'
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

# 创建一个Faceset用来存储FaceToken
#ret = api.faceset.create(outer_id='gtl')
# 本地图片的地址
face_1 = './gtl.jpeg'
face_2 = './gtl2.jpeg'
face_3 = './gtl3.jpg'
face_4 = './gtl4.jpg'
face_5 = './gtl5.jpg'

# 对图片进行检测
Face = {}

res = api.faceset.getdetail(outer_id='gtl')
print_result("111111",res)


res = api.detect(image_file=File(face_1))
print_result("person_1", res)
Face['person_1'] = res["faces"][0]["face_token"]
res=api.face.setuserid(face_token=Face['person_1'] ,user_id="古天乐")
api.faceset.addface(outer_id='gtl', face_tokens=Face.itervalues())

res = api.detect(image_file=File(face_2))
print_result("person_2", res)
Face['person_2'] = res["faces"][0]["face_token"]
res=api.face.setuserid(face_token=Face['person_2'] ,user_id="古天乐")
api.faceset.addface(outer_id='gtl', face_tokens=Face.itervalues())

res = api.detect(image_file=File(face_3))
print_result("person_3", res)
Face['person_3'] = res["faces"][0]["face_token"]
res=api.face.setuserid(face_token=Face['person_3'] ,user_id="古天乐")
api.faceset.addface(outer_id='gtl', face_tokens=Face.itervalues())

res = api.detect(image_file=File(face_4))
print_result("person_4", res)
Face['person_4'] = res["faces"][0]["face_token"]
res=api.face.setuserid(face_token=Face['person_4'] ,user_id="古天乐")
api.faceset.addface(outer_id='gtl', face_tokens=Face.itervalues())

res = api.detect(image_file=File(face_5))
print_result("person_5", res)
Face['person_5'] = res["faces"][0]["face_token"]
res=api.face.setuserid(face_token=Face['person_5'] ,user_id="古天乐")
api.faceset.addface(outer_id='gtl', face_tokens=Face.itervalues())


# 将得到的FaceToken存进Faceset里面
api.faceset.addface(outer_id='gtl', face_tokens=Face.itervalues())

