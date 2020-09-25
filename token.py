class token:
    def __int__(self,v,id,kw):
        self.value = v
        self.ID = id
        self.keyword = kw
""""   
    def __init__(self):
        self.value = 0
        self.ID = 0
        self.keyword = ""

    def token(self,v,id,kw):
        self.value = v
        self.ID = id
        self.keyword = kw
"""
    def setValue(self,v):
        self.value = v

    def returnValue(self):
        return self.value

    def setID(self,id):
        self.ID = id

    def returnID(self):
        return self.ID

    def setKeyWord(self,kw):
        self.keyword = kw

    def returnKeyWord(self):
        return self.keyword

    @classmethod
    def __str__(self):
        print("VALUE: " + self.returnValue() + "\nID: " + self.returnID() + "\nKEYWORD: " + self.returnKeyWord())