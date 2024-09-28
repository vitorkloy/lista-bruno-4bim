import hashlib

try:
    nome_arquivo = "arquivo.txt"

    with open(nome_arquivo, "w") as arquivo:
        arquivo.write("Este é o conteúdo do arquivo.")

    with open(nome_arquivo, "rb") as arquivo:
        dados = arquivo.read()
        hash_original = hashlib.sha256(dados).hexdigest()

    print(f"Hash original: {hash_original}")

    with open(nome_arquivo, "w") as arquivo:
        arquivo.write("Conteúdo alterado do arquivo.")

    with open(nome_arquivo, "rb") as arquivo:
        dados = arquivo.read()
        hash_novo = hashlib.sha256(dados).hexdigest()

    print(f"Novo hash: {hash_novo}")

    if hash_original == hash_novo:
        print("O arquivo não foi alterado.")
    else:
        print("O arquivo foi alterado.")
except Exception as e:
    print(f"Erro: {e}")