class Header:
    def __init__(self, date, time, scope):
        """
        """
        self._headerList=[date, time, scope]

    def getHeader(self):
        return self._headerList
        
