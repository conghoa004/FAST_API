## 1. FastAPI là gì?

**FastAPI** là framework Python để xây dựng **REST API**:

- 🚀 Rất nhanh (dựa trên Starlette + Pydantic)

- 📄 Tự sinh Swagger UI & OpenAPI

- 🔒 Validate dữ liệu tự động

- 🔥 Rất hợp làm API cho AI / Mobile / Web

---

## 2. Cài đặt FastAPI

```bash
pip install "fastapi[standard]"
```

---

## 3. Tạo API đầu tiên

📁 main.py

```python
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

---

## ▶️ Chạy server:

```bash
fastapi dev main.py
```

🌐 Truy cập:

- API: http://127.0.0.1:8000

- Swagger: http://127.0.0.1:8000/docs

- Redoc: http://127.0.0.1:8000/redoc

---

## 4. Tạo API GET / POST

**GET**

```python
@app.get("/users")
def get_users():
    return ["A", "B", "C"]
```

**POST**

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    return user

```

📌 FastAPI tự validate JSON:

```json
{
  "name": "Cong",
  "age": 22
}
```

---

## 5. Query params & Path params

```python
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"id": item_id, "q": q}
```

➡️ `/items/10?q=abc`

---

## 6. Trả HTTP status code

```python
from fastapi import HTTPException

@app.get("/products/{id}")
def get_product(id: int):
    if id != 1:
        raise HTTPException(status_code=404, detail="Not found")
    return {"id": 1, "name": "Laptop"}
```

## 7. Kết nối Database (ví dụ MySQL)

```bash
pip install sqlalchemy pymysql
```

```python
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:password@localhost/db_name"
)
```

---

## 8. Kiến trúc Feature / Module-based Architecture

📁 Cấu trúc:

```css
src/
 ┣ config/ # Cấu hình hệ thống như db...
 ┣ middleware/ # Xử lý các validate về quyền chặn router...
 ┣ user/
 ┃ ┣ user_controller.py # Xử lý nhận dữ liệu và validate như kiểm tra dữ liệu đầu vào (không hướng nghiệp vụ)
 ┃ ┣ user_service.py # Thực hiện xử lý ngiệp vụ gọi repo để thực hiện thao tác với DB
 ┃ ┣ user_repository.py # Thực hiện thao tác với DB
 ┃ ┣ user_model.py # Tạo schema cho DB
 ┃ ┣ user_router.py # Cấu hình tuyến đường
 ┃ ┣ user_dto.py # Các hàm validate dữ liệu
 ┃ ┣ user_utils.py # Các hàm tiện ích như (hash password)
 ┣ utils/ # Thành phần tiện ích sẽ nằm ở đây
 ┃ ┣ utils_router.py
 ┃ ┣ utils_controller.py
```

📄 `src/user/user_controller.py`

```python
# User controller
def index():
    return {"user": "hoaze", "age": 22, "address": "VL"}
```

📄 `src/user/user_router.py`

```python
from fastapi import APIRouter
from src.user.user_controller import index

router = APIRouter()

# GET info user
router.get("/users")(index)
```

📄 `main.py`

```python
from typing import Union
from fastapi import FastAPI
from src.user.user_router import router as user_router
from src.utils.utils_router import router as utils_router

# Create the app
app = FastAPI()

# Include routers
app.include_router(utils_router)
app.include_router(user_router)
```

---

## 9. Auth JWT (tóm tắt)

```bash
pip install python-jose passlib[bcrypt]
```

- Login → trả JWT

- Request sau → gửi Authorization: Bearer token

👉 FastAPI rất mạnh cho:

- 🔐 Auth API

- 🤖 AI model API

- 📱 Backend cho React / Flutter / Expo

---

## 10. Dùng `.env`

**Cài thư viện**

```bash
pip install python-dotenv
```

**Tạo file `.env`**

```env
APP_NAME=FastAPI App
DEBUG=true
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=123456
DB_NAME=test_db
JWT_SECRET=supersecret
```

📌 **KHÔNG commit file** `.env`

```bash
# .gitignore
.env
```

**Load biến môi trường**

```python
from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = os.getenv("APP_NAME")
DEBUG = os.getenv("DEBUG")
```

---

## 11. Build & run bằng docker-compose

```bash
docker compose up --build -d
```

