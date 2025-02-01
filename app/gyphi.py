

class GyphiClient:
    def __init__(self, api_key, timeout):
        self.api_key = api_key
        self.timeout = timeout

    def run(self):
        print('Running main GyphiClient')
