from pydantic import EmailStr
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta,timezone
from passlib.context import CryptContext
import jwt
import uuid

from core.config import settings


passwd_context = CryptContext(
    schemes=['bcrypt'],
    deprecated = "auto"
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")



def generate_hashed_password(password : str) -> str:
    return passwd_context.hash(password)

def verify_password(password : str, hash : str) -> bool:
    return passwd_context.verify(password,hash)

async def get_current_user(token : str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        email = payload.get('sub')
        user_uid = uuid.UUID(payload.get('user_uid'))
        if email is None or user_uid is None:
            raise credentials_exception 
        return {'email': email, 'user_uid': user_uid}
    except jwt.PyJWTError:
        raise credentials_exception

def create_access_token(email : EmailStr , user_uid : uuid.UUID, expire : timedelta | None = None):
    encode = {"sub":email,"user_uid":user_uid}
    exp = datetime.now() + (expire if expire is not None else timedelta(minutes=120))
    encode.update({"exp":exp})
    encoded_jwt = jwt.encode(
        encode,settings.secret_key,algorithm=settings.algorithm
    )

    return encoded_jwt
