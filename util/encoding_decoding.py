"""
    Archivo con las funciones para el cifrado de la contraseña.

    Autor: Manuel Vico Arboledas.
"""
from cryptography.fernet import Fernet

def encrypted(password:str):
    """
    Método que encripta la contraseña

    Args:
        password (str): Contraseña
    
    Returns:
        str: Contraseña encriptada
    """
    f = Fernet(b'FINEHtwMUOxgvyYM9fOvpXcQHYDDZKb3-NkPWTrZN5g=')
    b_password = bytes(password, 'ascii')
    encrypted_password = f.encrypt(b_password)
    return encrypted_password.decode('ascii')

def decrypt(password:str):
    """
    Método que desencripta la contraseña

    Args:
        password (str): Contraseña

    Returns:
        str: Contraseña desencriptada
    """
    f = Fernet(b'FINEHtwMUOxgvyYM9fOvpXcQHYDDZKb3-NkPWTrZN5g=')
    b_password = bytes(password, 'ascii')
    b_password_decrypt = f.decrypt(b_password)
    return b_password_decrypt.decode('ascii')