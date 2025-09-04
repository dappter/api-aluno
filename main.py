from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "API funcionando corretamente 🚀"}

@app.get("/me")
def me():
    return {
        "nome": "Seu Nome",
        "email": "seuemail@exemplo.com",
        "curso": "Seu Curso",
        "github": "https://github.com/seuusuario",
        "cidade": "Sua Cidade",
        "interesses": ["Python", "APIs", "Backend", "FastAPI"]
    }
