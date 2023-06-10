import uuid
from datetime import datetime
class BaseModel:
    def __init__(self):
        #print("i just created an object")
        #Every object the we are going to be creating will have the following attributes
        self.id = str(uuid.uuid4())
        # 
        self.created_at = datetime.fromisoformat('2023-06-08T17:16:59.005586')
        self.updated_at = datetime.fromisoformat('2023-06-08T17:16:59.005586')
    def __str__(self):
        str_dict = f"{[self.__class__.__name__]} {(self.id)} {self.__dict__}"
        return (str_dict)
    def save(self):
        self.updated_at = datetime.now().isoformat()
        return self.updated_at
        #self.created_at = datetime.datetime.now().isoformat()
    def to_dict(self):
        #to_dict = {}
        key = '__class__'
        value =  self.__class__.__name__
        #to_dict['__class__'] = self.__class__.__name__
        #to_dict.update(self.__dict__)
        #for (key, value) in self.__dict__.items():
        #    to_dict[key] = value
        to_dict = {key: value for (key, value) in self.__dict__.items()}
        return to_dict
#my_object = BaseModel()
#print(f" User id is {my_object.uuid}")
#print(f" Created the account in {my_object.updated_at}")
#print(f" Updated the account in {my_object.created_at}")
#print( my_object.__str__())
#my_object.save()
#print(f" save method {my_object.updated_at}")
#my_object.to_dict()
#print(my_object.to_dict)