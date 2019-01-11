from dins import DbSession
from dins.data.users import User
from passlib.handlers.sha2_crypt import sha512_crypt



def create_user(email: str, name: str, password: str, role: str) -> User:
    user = User()
    user.name = name
    user.email = email
    user.role = role
    user.hashed_password = hash_text(password)

    session = DbSession.factory()
    session.add(user)
    session.commit()

    return user

def hash_text(text: str) -> str:
    hashed_text = sha512_crypt.encrypt(text, rounds=150000)
    return hashed_text

def verify_hash(hashed_text: str, plain_text: str) -> bool:
    return sha512_crypt.verify(plain_text, hashed_text)
