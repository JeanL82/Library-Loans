About

Este proyecto implementa un sistema de registro e inicio de sesión en una interfaz de línea de comandos (CLI).
Incluye hashing de contraseñas con SHA-256, validación básica de entrada, manejo de archivos para guardar usuarios y registro de acciones mediante logs.
Sirve como demostración de conceptos de programación segura.

Autores

Jean L. Padilla Rivera
Correo institucional: jpadilla3192@interbayamon.edu
## Instrucciones de ejecución

1️⃣ **Clonar o descargar** este repositorio:  
git clone https://github.com/JeanL82/secure-cli-app.git

2️⃣ Entrar al proyecto
cd secure-cli-app

3️⃣ Instalar dependencias
pip install pwinput


4️⃣ Ejecutar el programa
python app.py

Credenciales de prueba

Puedes iniciar sesión usando este usuario predefinido:

Usuario: Admin  
Contraseña: 1234


Ejemplo de entrada y salida

Registro de usuario:

Enter su nombre de usuario: jean
Entre la contrasena: ******
Usuario registrado exitosamente.


Inicio de sesión:

Nombre de usuario: jean
Contrasena: ******
Inicio de sesión exitoso.


Los datos se almacenan en data/users.txt y las acciones se registran en logs/login.log.

Logs y datos

Carpeta de datos: /data (ej. users.txt)

Carpeta de logs: /logs (ej. login.log)


El modelo de amenazas
<img width="1536" height="1024" alt="Threat Model" src="https://github.com/user-attachments/assets/a883b965-51ce-4859-9a78-36bcabb6a127" />


Se utilizó pip-audit para verificar vulnerabilidades.
<img width="741" height="54" alt="Screenshot 2025-11-26 130719" src="https://github.com/user-attachments/assets/32641cd3-9460-4c8e-bf71-e621172d2b18" />


