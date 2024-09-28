import hashlib

try:
    string = input("Digite a string para gerar os hashes: ")

    if string:
        hash_md5 = hashlib.md5(string.encode()).hexdigest()
        hash_sha1 = hashlib.sha1(string.encode()).hexdigest()
        hash_sha256 = hashlib.sha256(string.encode()).hexdigest()

        print("\nHashes gerados:")
        print(f"Hash MD5:     {hash_md5}")
        print(f"Hash SHA-1:   {hash_sha1}")
        print(f"Hash SHA-256: {hash_sha256}")

        print("\nDiferenças entre os algoritmos:")
        print(f"Tamanho do hash MD5:     {len(hash_md5)} caracteres")
        print(f"Tamanho do hash SHA-1:   {len(hash_sha1)} caracteres")
        print(f"Tamanho do hash SHA-256: {len(hash_sha256)} caracteres")
    else:
        print("Ocorreu um erro.")
        exit()

except Exception as e:
    print(f"Erro: {e}")
    exit()