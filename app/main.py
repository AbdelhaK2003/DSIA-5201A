from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

from app import models, schemas, crud, auth, database
from app.dependencies import get_db

import time
tries = 5
while tries > 0:
    try:
        models.Base.metadata.create_all(bind=database.engine)
        break
    except Exception as e:
        print("DB pas encore prête...")
        time.sleep(3)
        tries -= 1
        if tries == 0:
            raise e


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/register", response_model=schemas.User)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db, user)

@app.post("/token", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/movies/", response_model=schemas.Movie)
def create_movie(
    movie: schemas.MovieCreate,  
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    return crud.create_movie(db=db, movie=movie, user_id=current_user.id)

   



@app.get("/movies/", response_model=list[schemas.Movie])
def read_movies(current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    return crud.get_movies_by_user(db, current_user.id)