import requests
import traceback
session = requests.session()
key = "81410c064db0455ca2debf20c5aa9972"
data = {
    'key': key,
    'info': "今天天气怎么样啊",
    'loc':'天津市',
    'userid':'abc'}
result = session.post('http://www.tuling123.com/openapi/api', data)
print(result.text)