import requests

url = 'https://slack.com/api/chat.postMessage'
params = {  'token':'[token_key]',
            'channel':'[channel_name]',
            'as_user':'true',
            'text':'Hello',
            }


class Response(object):
    def __init__(self):
        self.counter = 0 #現在の状態が何回続いたか数えるもの
        self.pre_status = False #False:ついていない、True:ついている
        self.now_status = False
    def judge(self,v0,v1):
        self.pre_status = self.now_status

        #与えられた値の判定
        if v0 > 50:
            self.now_status = True

        else:
            self.now_status = False

        #照明が変化したかを判定
        if self.pre_status!=self.now_status:
            self.counter=0
        else:
            self.counter+=1
        #3回連続していたらpostする
        if self.counter==1:
            if self.now_status:
                params['text']="照明がつきました。鍵は貸し出しされています。"
                request=requests.post(url,params=params)
            else:
                params['text']="照明が消えました。"
                request=requests.post(url,params=params)
                

