__author__ = 'Edward Pie'
import requests
import json

class GcmServer(object):

    def __init__(self,api_key):
        self.api_key = api_key
        self.headers = {"Authorization": "%s=%s" % ("key", self.api_key), "Content-Type": "application/json"}
        self.url = "https://android.googleapis.com/gcm/send"

    def push(self,title,message,gcm_ids):
        try:
            payload = {"data": {"title": title, "message": message}, "registration_ids": gcm_ids}
            response = requests.post(self.url, headers=self.headers, data=json.dumps(payload))

            print 'STATUS CODE : ',response.status_code
            print 'RESPONSE BODY : ',response.json()
        except Exception, e:
            print 'Oops! An error occured ', e.message
