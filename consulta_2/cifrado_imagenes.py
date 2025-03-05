# Instalar PyCryptodome: pip install pycryptodome

# Ejemplo de cifrado y descifrado de una imagen con AES-256-GCM
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

# Función para cifrar la imagen
def cifrar_imagen(archivo_imagen, clave):
    # Generar un nonce aleatorio (necesario para AES-GCM)
    nonce = get_random_bytes(12)
    
    # Leer la imagen
    with open(archivo_imagen, 'rb') as f:
        datos_imagen = f.read()
    
    # Crear el cifrador AES en modo GCM
    cipher = AES.new(clave, AES.MODE_GCM, nonce=nonce)
    
    # Cifrar los datos
    ciphertext, tag = cipher.encrypt_and_digest(datos_imagen)
    
    # Devolver el nonce, el tag y el texto cifrado
    return nonce + tag + ciphertext

# Función para descifrar la imagen
def descifrar_imagen(archivo_cifrado, clave):
    # Extraer el nonce, tag y ciphertext
    nonce = archivo_cifrado[:12]
    tag = archivo_cifrado[12:28]
    ciphertext = archivo_cifrado[28:]
    
    # Crear el descifrador AES en modo GCM
    cipher = AES.new(clave, AES.MODE_GCM, nonce=nonce)
    
    # Descifrar los datos
    datos_descifrados = cipher.decrypt_and_verify(ciphertext, tag)
    
    return datos_descifrados

if __name__ == "__main__":
    # Crear la carpeta imagenes_a_cifrar dentro de consulta_2 si no existe
    input_dir = "consulta_2/imagenes_a_cifrar"
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)
        print(f"Created directory: {input_dir}")

    # Crear la carpeta imagenes_cifradas dentro de consulta_2 si no existe
    output_dir = "consulta_2/imagenes_cifradas"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")
        
    dechipher_dir = "consulta_2/imagenes_descifradas"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")


    # Definir el archivo de entrada (imagen a cifrar)
    archivo_imagen = os.path.join(input_dir, "imagen_original.png")

    # Verificar si la imagen existe en imagenes_a_cifrar
    if not os.path.exists(archivo_imagen):
        print(f"Error: The file '{archivo_imagen}' was not found in {input_dir}.")
        print(f"Please move 'imagen_original.png' to {input_dir} and try again.")
        exit(1)

    # Ejemplo de uso
    clave = get_random_bytes(32)  # Clave de 256 bits

    # Cifrar la imagen
    imagen_cifrada = cifrar_imagen(archivo_imagen, clave)

    # Guardar la imagen cifrada en la carpeta imagenes_cifradas
    encrypted_file_path = os.path.join(output_dir, "imagen_cifrada.enc")
    try:
        with open(encrypted_file_path, 'wb') as f:
            f.write(imagen_cifrada)
        print(f"Encrypted image saved to: {encrypted_file_path}")
    except Exception as e:
        print(f"Error saving encrypted image: {e}")

    # Leer la imagen cifrada y descifrarla
    with open(encrypted_file_path, 'rb') as f:
        archivo_cifrado = f.read()

    imagen_descifrada = descifrar_imagen(archivo_cifrado, clave)

    # Guardar la imagen descifrada en la carpeta imagenes_cifradas
    decrypted_file_path = os.path.join(dechipher_dir, "imagen_descifrada.png")
    try:
        with open(decrypted_file_path, 'wb') as f:
            f.write(imagen_descifrada)
        print(f"Decrypted image saved to: {decrypted_file_path}")
    except Exception as e:
        print(f"Error saving decrypted image: {e}")