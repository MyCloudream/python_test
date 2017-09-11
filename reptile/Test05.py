class SendSms:
    def __init__(self, sms_host, port, version, url, api_key):
        self.sms_host = sms_host
        self.port = port
        self.version = version
        self.url = url
        self.api_key = api_key

    def send_sms(self, text, mobile):
        """
        通用接口发短信
        """
        params = urllib.urlencode({self.api_key, 'text': text, 'mobile': mobile})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = httplib.HTTPSConnection(self.sms_host, port=self.port, timeout=30)
        conn.request("POST", sms_send_uri, params, headers)
        response = conn.getresponse()
        response_str = response.read()
        conn.close()
        return response_str

