class Client:
    def __init__(self,cid,name,age):
        if cid == None:
            raise ValueError("Client Id can not be None")
        self._clientId = cid
        self.Name = name
        self.Age = age
    
    @property
    def clientId(self):
        return self._clientId

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self,value):
        if value == None or len(value) < 3:
            raise ValueError("Client name is too short")
        self._name = value

    @property
    def Age(self):
        return self._age

    @Age.setter
    def Age(self,value):
        if value ==  None or value < 18:
            raise ValueError("Client is too young!")
        self._age = value


'''
This tells Python that TestClient is a special type of class, which contains tests
Python should find these classes and run the tests on its own
'''



'''
1. Must not forget to run the tests
2. First test failure crashes my program
    - What's the status of remaining tests?
    - No reports, no feedback, nada
3. No difference between running the program and testing it

Support for running unit tests is spotty in VS Code
    - It's ok in PyCharm and Eclipse
    - Probably OK in Visual Community

'''
# tc = TestClient()
# tc.test_client()
# tc.test_client_again()
# test_client()
# test_client_again()

print("Hello world!")