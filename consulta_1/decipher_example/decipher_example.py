import os
from consulta_2.cifrado_imagenes import descifrar_imagen
from consulta_1.shamir.secretSharing import reconstruct_secret

def main():
    # Definir la clave cifrada
    try:
        fragment_1 = str(input("Ingrese el fragmento 1 de la clave: "))
        fragment_2 = str(input("Ingrese el fragmento 2 de la clave: "))
        fragment_3 = str(input("Ingrese el fragmento 3 de la clave: "))
        
        # Definir las partes compartidas de la clave
        shares = [
            (1, fragment_1),
            (2, fragment_2),
            (3, fragment_3),
        ]
        
        # Reconstruir la clave
        recovered_key = reconstruct_secret(shares, 3)
        
        # Descifrar la imagen
        encrypted_image_path = "consulta_2/imagenes_cifradas/ciphered_dcm.enc"
        with open(encrypted_image_path, 'rb') as f:
            encrypted_image = f.read()
        
        decrypted_image = descifrar_imagen(encrypted_image, recovered_key)
        
        # Guardar la imagen descifrada en la carpeta imagenes_descifradas
        output_dir = "consulta_2/imagenes_descifradas"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Created directory: {output_dir}")
        
        decrypted_image_path = os.path.join(output_dir, "0002.DCM")
        with open(decrypted_image_path, 'wb') as f:
            f.write(decrypted_image)
        print(f"Decrypted image saved to: {decrypted_image_path}")
    finally:
        # Eliminar de memoria la clave y sus fragmentos
        del recovered_key
        del shares
        print("Clave eliminada de la memoria")

if __name__ == "__main__":
    main()
    