# 🍔 Burger API

Uma API simples feita em **Python + FastAPI** para demonstração de endpoints.

- **`/health`** → retorna o status da aplicação.  
- **`/me`** → retorna informações sobre um produto fictício (Burger).

---

## 🚀 Como rodar localmente

### 1. Clonar este repositório
```bash
git clone https://github.com/SEU-USUARIO/api-aluno.git
cd api-aluno
2. Criar e ativar um ambiente virtual
No Windows (CMD):

cmd
Copiar código
python -m venv venv
venv\Scripts\activate.bat
No PowerShell:

powershell
Copiar código
.\venv\Scripts\Activate
No Linux/Mac:

bash
Copiar código
python3 -m venv venv
source venv/bin/activate
3. Instalar as dependências
bash
Copiar código
pip install -r requirements.txt
4. Rodar a aplicação
bash
Copiar código
uvicorn main:app --reload
A API ficará disponível em:

http://127.0.0.1:8000/health

http://127.0.0.1:8000/me

🌐 API Online no Render
A API está publicada no Render e pode ser acessada aqui:
🔗 https://api-aluno-0y1h.onrender.com

📌 Endpoints
GET /health
Exemplo de resposta:

json
Copiar código
{"status": "API funcionando corretamente 🚀"}
GET /me
Exemplo de resposta:

json
Copiar código
{
  "produto": "Burger API",
  "preço": "47.99R$",
  "acompanhamento": "Nenhum",
  "descrição": "O melhor burger do mundo",
  "disponivel": "Sim",
  "interesses": ["Comida", "Bebida", "Tecnologia", "Programação", "FastAPI"]
}
🛠️ Tecnologias usadas
Python

FastAPI

Uvicorn

Render
