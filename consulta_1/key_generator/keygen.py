import secrets

def generate_aes_key():
    """
    Genera una clave AES de 256 bits (32 bytes) de forma segura.
    """
    # Generar 32 bytes de clave segura
    key = secrets.token_bytes(32)
    return key

def main():
    # Generar la clave AES
    aes_key = generate_aes_key()
    
    try:
        # Mostrar la clave generada en formato hexadecimal
        print("Clave AES generada:")
        print(aes_key.hex())
        
    finally:
        del aes_key
        print("Clave eliminada de la memoria.")

if __name__ == "__main__":
    main()
