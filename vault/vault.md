# Guía de Uso de HashiCorp Vault para Almacenamiento Seguro de Claves y Fragmentos

Este documento proporciona una guía paso a paso para utilizar HashiCorp Vault para almacenar de forma segura las claves generadas mediante el algoritmo de Shamir's Secret Sharing y cómo acceder a ellas. Además, incluye información sobre cómo gestionar las claves de cifrado/descifrado de manera segura y cómo garantizar la confidencialidad de las imágenes almacenadas.

## Requisitos previos

Antes de comenzar, asegúrate de tener los siguientes elementos:

- **Vault** instalado y configurado en tu sistema o nube privada.
- **Algoritmo de Shamir's Secret Sharing** para generar y gestionar los fragmentos de la clave (puedes usar el ejemplo en Python o cualquier implementación que prefieras).
- **Acceso administrativo a Vault** para configurar la autenticación y la política de acceso.

## Configuración de Vault

Para comenzar a usar Vault, debes configurarlo correctamente. A continuación se muestra una configuración básica para Vault en un archivo `vault.hcl`.

### Ejemplo de configuración (`vault.hcl`)

```
storage "file" {
    path = "/path/to/vault/storage"
}

listener "tcp" {
    address     = "127.0.0.1:8200"
    tls_disable = 1
}

ui = true
disable_mlock = true
api_addr = "https://127.0.0.1:8200"
```

## Iniciar Vault

Para iniciar Vault en modo desarrollo, utiliza el siguiente comando:

```bash
vault server -config=/path/to/vault.hcl
```



## Almacenar fragmentos de la clave
Para autenticarse ejecute:

```bash
vault login <token>
```

Para almacenar los fragmentos de la clave:

```bash
vault kv put secret/shamir/fragment1 value=<fragment1_value>
vault kv put secret/shamir/fragment2 value=<fragment2_value>
vault kv put secret/shamir/fragment3 value=<fragment3_value>
...
```
## Acceder a los fragmentos de la clave

Una vez iniciado sesión en vault, para recuperar los fragmentos de clave con el siguiente comando:

```bash
vault kv get secret/shamir/fragment1
vault kv get secret/shamir/fragment2
...
```
Se recomienda establecer políticas de acceso a los fragmentos de la clave para garantizar que únicamente los usuarios permitidos puedan acceder a ellas.