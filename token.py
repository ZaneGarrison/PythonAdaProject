class Token:
    def __int__(self, value, id, keyword):
        self.value = value
        self.ID = id
        self.keyword = keyword

    def setvalue(self, v):
        self.value = v

    def returnvalue(self):
        return self.value

    def setid(self, id):
        self.ID = id

    def returnid(self):
        return self.ID

    def setkeyword(self, kw):
        self.keyword = kw

    def returnkeyword(self):
        return self.keyword

#    @classmethod
#    def __str__(self):
#        print("VALUE: " + self.returnValue() + "\nID: " + self.returnID() + "\nKEYWORD: " + self.returnKeyWord())
