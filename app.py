import streamlit as st
import time
from utils import cria_chain_conversa, folder_files

# Dicionário simples de usuários
USUARIOS = {
    "alta cupula": "pergunteaouniverso"
    
}

def autenticar():
    st.title("🔐 Login")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if username in USUARIOS and USUARIOS[username] == password:
            st.session_state["autenticado"] = True
            st.session_state["usuario"] = username
            st.success("Login realizado com sucesso!")
            st.rerun()

        else:
            st.error("Usuário ou senha incorretos")

def chat_window():
    st.header("🤖 Bem Vindo ao ChatPDF", divider=True)
    if not 'chain' in st.session_state:
        st.error("Faça o upload de PDFs para começar")
        st.stop()
    
    chain = st.session_state["chain"]
    memory = chain.memory 

    mensagens = memory.load_memory_variables({})["chat_history"]
    container = st.container()
    for mensagem in mensagens:
        chat = container.chat_message(mensagem.type)
        chat.markdown(mensagem.content)
        
    nova_mensagem = st.chat_input("Converse com seus documentos")
    if nova_mensagem:
        chat = container.chat_message("human")
        chat.markdown(nova_mensagem)
        chat = container.chat_message("ai")
        chat.markdown("Gerando Resposta")
        chain.invoke({"question": nova_mensagem})
        st.rerun()

def save_uploaded_files(uploaded_files, folder):
    """Salva arquivos enviados na pasta especificada."""
    for file in folder.glob("*.pdf"):
        file.unlink()
    for file in uploaded_files:
        (folder / file.name).write_bytes(file.read())

def main():
    if not st.session_state.get("autenticado", False):
        autenticar()
        return  # Só continua se estiver autenticado

    with st.sidebar:
        st.header("Upload de PDFs")
        uploaded_pdfs = st.file_uploader("Adicione arquivos PDF", 
                                         type="pdf", 
                                         accept_multiple_files=True)
        if uploaded_pdfs:
            save_uploaded_files(uploaded_pdfs, folder_files)
            st.success(f"{len(uploaded_pdfs)} arquivo(s) salvo(s) com sucesso!")
        
        label_botao = "Inicializar Chatbot"
        if "chain" in st.session_state:
            label_botao = "Atualizar Chatbot"
        if st.button(label_botao, use_container_width=True):
            if len(list(folder_files.glob("*.pdf"))) == 0:
                st.error("Adicione arquivos pdf para inicializar o chatbot")
            else:
                st.success("Inicializando o Chatbot...")
                cria_chain_conversa()
                st.rerun()
    
    chat_window()

if __name__ == "__main__":
    main()
