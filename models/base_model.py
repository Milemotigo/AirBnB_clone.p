import uuid
class BaseModel:
    def __init__(self):
        print("i just created an object")
        #Every object the we are going to be creating will have the following attributes
        self.uuid = uuid.uuid4()
        self.created_at = created_at
        self.updated_at = updated_at
    def __str__(self):
        return (f"UUID: {self.uuid.uuid4}, created_at: {self.created_at}, updated_at: {self.updated_at}")
print(str(BaseModel()))
my_object = BaseModel("2023-6-7", "2023-6-7")
print(f" User id is {my_object.uuid}")
print(f" Created the account in {my_object.updated_at}")
print(f"Updated the account in {my_object.created}")
print(my_object)