import os
from consulta_2.cifrado_imagenes import cifrar_imagen
from consulta_1.key_generator.keygen import generate_aes_key
from consulta_1.shamir.secretSharing import create_shares

def main():
    # Generar la clave AES
    aes_key = generate_aes_key()
    
    try:
        # Mostrar la clave generada en formato hexadecimal
        print("Clave AES generada")
        
        # Cifrar la imagen
        archivo_imagen = "consulta_2/imagenes_a_cifrar/0002.DCM"
        
                # Crear las partes compartidas de la clave
        secret = aes_key.hex()
        total_shares = 5
        threshold = 3
        shares = create_shares(secret, total_shares, threshold)
        
        
        print("Fragmento de la clave generados")
        
        ciphered_image = cifrar_imagen(archivo_imagen, aes_key)
        
        # Crear la carpeta imagenes_cifradas dentro de consulta_2 si no existe
        output_dir = "consulta_2/imagenes_cifradas"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Created directory: {output_dir}")
        
        encrypted_file_path = os.path.join(output_dir, "ciphered_dcm.enc")
        
        try:
            with open(encrypted_file_path, 'wb') as f:
                f.write(ciphered_image)
            print(f"Encrypted image saved to: {encrypted_file_path}")
        except Exception as e:
            print(f"Error saving encrypted image: {e}")
        
        
    finally:
        #Eliminar de memoria la clave AES y sus fragmentos
        del aes_key
        del shares
        print("Clave eliminada de la memoria")

if __name__ == "__main__":
    main()