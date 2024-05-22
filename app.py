from repositories.UserRepository import UserRepository
from services.UserService import UserService
from models.User import User, Base
from sqlalchemy import create_engine
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

engine = create_engine('sqlite:///database/database.db', echo=True)
user_repository: UserRepository = UserRepository(engine=engine, base=Base)
user_service: UserService = UserService(user_repository=user_repository)

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    users_list = user_service.get_all_users()
    return templates.TemplateResponse("index.html", {"request": request, "users": users_list})


@app.post("/submit", response_class=HTMLResponse)
async def submit(
        request: Request,
        name: str = Form(...),
        surname: str = Form(...),
        email: str = Form(...),
        phone: str = Form(...)
):
    error_message = None

    try:
        user_service.add_user(User(name=name, surname=surname, email=email, phone_number=phone))
    except ValueError as e:
        error_message = str(e)

    users_list = user_service.get_all_users()
    return templates.TemplateResponse("index.html",
                                      {"request": request, "users": users_list, "error_message": error_message})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
