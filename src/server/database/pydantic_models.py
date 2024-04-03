from pydantic import BaseModel

class ModifyBaseModel(BaseModel):
    id: int = 0

class LoginData(BaseModel):
    password: str
    login: str

class ChangePassword(BaseModel):
    password: str

class Client(ModifyBaseModel):
    full_name: str = ""
    phone_number: str = ''
    email: str = ""

class Manager(ModifyBaseModel):
    full_name: str = ""
    phone_number: str = ''

class Storekeeper(ModifyBaseModel):
    full_name: str = ""
    phone_number: str = ''

class Order(ModifyBaseModel):
    id_client: int
    id_master: int
    description: str = ""
    price: str = ""
    state_order: str = ""
    review: str = ""

class Report(ModifyBaseModel):
    id_order: int
    state: str = ""
    review: str = ""

class Supply(ModifyBaseModel):
    id_storekeeper: int
    name: str = ""
    quantity: int = 0
    date: str

class Master(ModifyBaseModel):
    full_name: str = ""
    phone_number: str = ''

class Details(ModifyBaseModel):
    name: str = ""
    quantity: int = 0

class Post(ModifyBaseModel):
    post: str = ""
    power_level: int = 0

class User(ModifyBaseModel):
    position: int
    login: str = ""
    password: str = ""