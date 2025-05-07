# 📄 ChatPDF com Streamlit + Autenticação

Este projeto é uma aplicação web desenvolvida com **Streamlit** que permite aos usuários interagir com seus próprios arquivos PDF através de uma interface de chatbot com suporte a RAG (Retrieval-Augmented Generation).

## ✨ Funcionalidades

- 🔐 **Login seguro** com autenticação básica de usuários.
- 📁 **Upload de múltiplos arquivos PDF**.
- 🤖 **Chatbot que responde com base no conteúdo dos PDFs enviados**.
- 🧠 Memória de conversação preservada durante a sessão.
- 🔄 Recarregamento automático após novo envio de arquivos ou inicialização do bot.

## 🚀 Como executar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/Esdras-Emerson/Chat-IA-Streamlit.git
cd Chat-IA-Streamlit

### 2. Crie e ative um ambiente virtual
bash
Copiar
Editar
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

### 3. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt
Certifique-se de que o arquivo utils.py esteja presente na raiz, contendo as funções cria_chain_conversa e folder_files.

### 4. Execute a aplicação
bash
Copiar
Editar
streamlit run app.py
🔐 Usuários cadastrados (exemplo)
Usuário 	Senha
alta cupula	pergunteaouniverso

📂 Estrutura esperada do projeto
Copiar
Editar
Chat-IA-Streamlit/
├── app.py
├── utils.py
├── requirements.txt
├── .venv/
└── uploads/ (pasta usada para armazenar PDFs)
📌 Observações
Os arquivos PDF enviados são sobrescritos a cada novo upload.

O modelo só pode responder com base nas informações presentes nos arquivos PDF.

Ideal para usos com LLMs conectadas a uma vector store, como FAISS ou ChromaDB.