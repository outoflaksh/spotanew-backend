from fastapi import FastAPI, HTTPException, status
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from .spotify_handler import get_random_song

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1",
    "http://127.0.0.1:3000",
    "https://spotanew.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_index():
    return {"msg": "OK"}


@app.get("/random")
def read_random_song():
    try:
        random_song_details = get_random_song()

        return random_song_details
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Sorry, there was an error!",
        )
