import secrets
import base64

def generate_password(length=12, use_uppercase=True, use_numbers=True):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    if use_uppercase:
        characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if use_numbers:
        characters += '0123456789'

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def hash_password(password):
    salt = secrets.token_hex(16)
    hashed_password = base64.b64encode(f"{password}:{salt}".encode()).decode()
    return hashed_password

def verify_password(stored_hash, provided_password):
    try:
        decoded = base64.b64decode(stored_hash)
        stored_password, salt = decoded.decode().split(':')

        if secrets.compare_digest(provided_password, stored_password):
            return True
        return False
    except:
        return False

password = generate_password(length=16, use_uppercase=True, use_numbers=True)
print(f"Сгенерированный пароль: {password}")

hashed_password = hash_password(password)
print(f"Хеш пароля: {hashed_password}")

is_valid = verify_password(hashed_password, password)
print(f"Проверка пароля: {'Верный' if is_valid else 'Неверный'}")
