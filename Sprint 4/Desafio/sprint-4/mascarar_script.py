import hashlib

while True:
    string_input = input("Digite algo - (sair: 'sair'): ")

    if string_input.lower() == 'sair':
        break

    hash_object = hashlib.sha1(string_input.encode())
    hash_hex = hash_object.hexdigest()

    print(f'Hash: {hash_hex}')
