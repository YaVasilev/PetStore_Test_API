from dataclasses import dataclass, asdict


@dataclass
class RequestCreateUserModel:
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: str

    def to_dict(self):
        return asdict(self)


@dataclass
class ResponseCreateUserModel:
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: str

    def to_dict(self):
        return asdict(self)