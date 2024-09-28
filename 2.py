import hashlib

try:
    string1 = input("Digite a primeira string: ")
    string2 = input("Digite a segunda string: ")

    if string1 and string2:
        hash1 = hashlib.sha256(string1.encode()).hexdigest()
        hash2 = hashlib.sha256(string2.encode()).hexdigest()

        print(f"Hash da primeira string: {hash1}")
        print(f"Hash da segunda string: {hash2}")

        if hash1 == hash2:
            print("Os hashes são iguais.")
        else:
            print("Os hashes são diferentes.")
    else:
        print("Ocorreu um erro.")
        exit()
except Exception as e:
    print(f"Erro: {e}")
    exit()