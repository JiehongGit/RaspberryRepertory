#-*- coding: utf-8 -*-

#把已知人脸添加到人脸集合中

#------------------------------------------------------------------------------
#准备阶段
API_KEY = "feI5hwgMw9zQKaDmDCjq1SFdVZynhy38"
API_SECRET = "y8NTlkYNLJQOmGErZzGUnegmUZROER0r"
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

# 本地图片的地址
face_6 = './gtl6.jpg'
face_7 = './gtl7.jpg'
face_8 = './gtl8.jpg'
face_9 = './gtl9.jpg'
face_10 = './gtl10.jpg'
# 对图片进行检测
Face = {}

res = api.detect(image_file=File(face_6))
print_result("person_6", res)
Face['person_6'] = res["faces"][0]["face_token"]
res=api.face.setuserid(face_token=Face['person_6'] ,user_id="古天乐")

res = api.detect(image_file=File(face_7))
print_result("person_7", res)
Face['person_7'] = res["faces"][0]["face_token"]
res=api.face.setuserid(face_token=Face['person_7'] ,user_id="古天乐")

res = api.detect(image_file=File(face_8))
print_result("person_8", res)
Face['person_8'] = res["faces"][0]["face_token"]
res=api.face.setuserid(face_token=Face['person_8'] ,user_id="古天乐")

res = api.detect(image_file=File(face_9))
print_result("person_9", res)
Face['person_9'] = res["faces"][0]["face_token"]
res=api.face.setuserid(face_token=Face['person_9'] ,user_id="古天乐")

res = api.detect(image_file=File(face_10))
print_result("person_10", res)
Face['person_10'] = res["faces"][0]["face_token"]
res=api.face.setuserid(face_token=Face['person_10'] ,user_id="古天乐")

# 将得到的FaceToken存进Faceset里面
api.faceset.addface(outer_id='gtl', face_tokens=Face.itervalues())

