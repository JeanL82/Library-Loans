# 📚 Secure CLI App – Sistema de Préstamos de Biblioteca

Este proyecto es una mini aplicación de consola (**CLI**) desarrollada en **Python**, diseñada para manejar usuarios y préstamos de libros en una biblioteca, siguiendo buenas prácticas de **seguridad en el código (Secure Coding Practices)**.

---

## Características principales
- **Autenticación segura** con contraseñas hasheadas (SHA-256)
- **Validación de entrada** (anti inyección tipo SQL)
- **Registro y login** de usuarios
- **Operaciones CRUD** básicas:
  - Agregar libros
  - Ver libros registrados
  - Prestar libros
  - Devolver libros
- **Registro de auditoría (logs)** de todas las acciones del usuario
- **Persistencia** en archivos planos (`.txt`)
- **Diseño seguro:** aplica el principio de mínimo privilegio y control de errores

---

## Instrucciones de ejecución

1️⃣ **Clonar o descargar** este repositorio:  
git clone https://github.com/JeanL82/secure-cli-app.git

2️⃣ Entrar al proyecto
cd secure-cli-app

3️⃣ Instalar dependencias
pip install pwinput


4️⃣ Ejecutar el programa
python app.py

