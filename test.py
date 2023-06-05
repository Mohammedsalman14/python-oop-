class test:
    
    def __init__(self,name:str,id:int) -> None:
        self._name=name
        self._id=id
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        self._name=value
    @property
    def id(self):
        return self._id;
    @id.setter
    def id(self,value):
        if self._id>=10:
            return self._id
        raise Exception("The name is too long")
t=test("mohammedsalman",21)
print(t.name)