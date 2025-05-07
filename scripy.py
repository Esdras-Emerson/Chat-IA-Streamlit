from streamlit_authenticator import Hasher

# Lista de senhas em texto puro
senhas = ["senhaDoEsdra", "senhaDoJoao"]

# Corrigido: criar Hasher sem argumentos
hasher = Hasher()

# Gerar os hashes
hashes = hasher.generate(senhas)

# Mostrar os hashes
for i, h in enumerate(hashes):
    print(f"Hash da senha '{senhas[i]}':\n{h}\n")
