from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "API funcionando corretamente 🚀"}

@app.get("/me")
def me():
    return {
        "nome": "Guilherme Lossio",
        "email": "guilhermelossio3@gmail.com",
        "curso": "Sistemas de Informação",
        "github": "https://github.com/dappter",
        "cidade": "Juazeiro do Norte - CE",
        "interesses": ["Python", "APIs", "Backend", "FastAPI"]
    }
