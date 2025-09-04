from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "API funcionando corretamente 🚀"}

@app.get("/me")
def me():
    return {
        "produto": "Burger API",
        "preço": "47.99R$",
        "acompanhamento": "Nenhum",
        "descrição": "O melhor burger do mundo",
        "disponivel": "Sim",
        "interesses": ["Comida", "Bebida", "Tecnologia", "Programação", "FastAPI"]
    }
