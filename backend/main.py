from typing import Optional

import firebase_admin
from fastapi import FastAPI, HTTPException
from firebase_admin import credentials, auth
from pydantic import BaseModel

app = FastAPI()

# Init Firebase Auth
cred = credentials.Certificate("config/serviceAccountKey.json")
firebase_admin.initialize_app(cred)


class UserCreate(BaseModel):
    email: Optional[str] = "hongseongtaek@gmail.com"
    password: Optional[str] = None


class UserLogin(BaseModel):
    email: Optional[str] = "hongseongtaek@gmail.com"
    password: Optional[str] = None


@app.get("/")
def read_root():
    return {"Hello": "Taek!"}


@app.post("/signup/")
def sign_up(user_data: UserCreate):
    try:
        user = auth.create_user(
            email=user_data.email,
            password=user_data.password
        )
        return {"message": "회원가입 성공"}
    except Exception as e:
        raise HTTPException(status_code=400, detail="회원가입 실패")


# 로그인 엔드포인트
@app.post("/login/")
async def log_in(user_data: UserLogin):
    try:
        # 이메일을 사용하여 사용자를 가져옵니다.
        user = auth.get_user_by_email(user_data.email)

        # 가져온 사용자 정보와 클라이언트가 제공한 비밀번호를 사용하여 Firebase에서 로그인을 시도합니다.
        auth_user = auth.update_user(user.uid, password=user_data.password)

        # 로그인에 성공한 경우, ID 토큰을 반환합니다.
        id_token = auth.create_custom_token(user.uid)
        return {"message": "로그인 성공", "idToken": id_token}
    except Exception as e:
        raise HTTPException(status_code=400, detail="로그인 실패")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
