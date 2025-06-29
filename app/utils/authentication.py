from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi import Security

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def generate_jwt_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=60)
    to_encode.update({"exp": expire.timestamp()})
    encoded_jwt = jwt.encode(to_encode, "1234", algorithm="HS256")
    return encoded_jwt 

def decode_jwt_toke(token: str):
    try:
        payload = jwt.decode(token, "1234",  algorithms="HS256")
        if payload.get("exp") and payload["exp"] >= datetime.now().timestamp():
            return payload
    except JWTError:
        return None 
    
def get_current_user(token: str = Security(oauth2_scheme)) -> dict:
    return decode_jwt_toke(token)
