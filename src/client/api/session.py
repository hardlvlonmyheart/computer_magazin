from src.server.database.pydantic_models import User, LoginData
from src.client.api import resolvers



class Session:
    user: User = User(
        id=-1,
        password='',
        login='',
        position=0
    )
    auth: bool = False
    error: str = None
    server_available: bool = None
    
    def __init__(self) -> None:
        self.check_connect()

    def check_connect(self) -> bool:
        self.server_available = type(resolvers.check_connection) is bool

    def sign_in(self, login: str, password: str) -> None:
        answer: dict = resolvers.login(password, login)

        match answer['code']:
            case 400:
                self.error = answer['msg']
            case 200:
                self.error = None
                self.user = User(
                    id=answer['result']['id'],
                    password=answer['result']['password'],
                    login=answer['result']['login'],
                    position=answer['result']['position']
                )
                self.auth = True
    
    def register(self, login: str, password: str, position: str) -> None:
        answer: dict = resolvers.register(data=User(
            password=password,
            login=login,
            position=position,
        ))

        match answer['code']:
            case 400:
                self.error = answer['msg']

            case 200: 
                self.error = None
    
    def update(self, password: str) -> None:
        answer: dict = resolvers.update_password(id=self.user.id, password=password)

        match answer['code']:
            case 400: 
                self.error = answer['msg']

            case 200:
                self.user.password = password
    
    def delete(self) -> None:
        resolvers.delete_account(self.user.id)
        self.leave()

    def leave(self) -> None:
        self.user = User(
            id=-1,
            login='',
            password='',
            position=0
        )
        self.auth = False