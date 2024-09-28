import hashlib

try: 
    senha = input("Digite a senha: ")

    if senha:
        hash_md5 = hashlib.md5(senha.encode()).hexdigest()
        print(f"Hash MD5 da senha: {hash_md5}")
    else:
        print("Ocorreu um erro.")
        exit()
except Exception as e:
    print(f"Erro: {e}")
    exit()