import os,hashlib,pwinput,logging

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename='logs/login.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a',
    force=True
)

def Hashpassword(password) :
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed



def register():
    os.makedirs("data",exist_ok=True)
    path = "data/users.txt"

    Invalid = ["select","from","Drop","insert","delete","update","user",";","--","'","\""]


    username=input("Enter su nombre de usuario: ")
    
    username_lower = username.lower()

    for palabras in Invalid:
        if palabras.lower() in username_lower:
            print("Nombre de usuario invalido. Intente de nuevo.")
            return
        
    password=pwinput.pwinput("Entre la contrasena: ", mask='*')

  
    hashed_password=Hashpassword(password)

    with open(path,'a') as file:
        file.write(f"{username},{hashed_password}\n")
    logging.info(f"Nuevo usuario registrado: {username}")
    print("Registracion exitosa!")



def login():
    

    path = "data/users.txt"

    if not os.path.exists(path):
        print("No hay usuarios registrados. Por favor registrese primero.")
        return
    
    
    
    
    username=input("Ingrese su nombre de usuario: ")
    password=pwinput.pwinput("Ingrese su contrasena: ", mask='*')
    hashed_password=Hashpassword(password)
    

    with open(path,"r") as file:
        for linea in file:
            user_guardado,password_guardado = linea.strip().split(",")
            if username == user_guardado and hashed_password == password_guardado:
                logging.info(f"Usuario logueado exitosamente: {username}")
                print(f"Bienvenido,{username}!")
                return username
            
    logging.warning(f"Fallo de login para el usuario: {username}")
    print("Nombre de usuario o contrasena incorrectos.")


def agregar_libros():

    os.makedirs("data",exist_ok=True)
    path = "data/libros.txt"

    titulo = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el autor del libro: ")

    with open(path,"r") as file:
        for linea in file:
            libro_titulo, autor = linea.strip().split(",")
            if titulo.lower() == libro_titulo.lower():
                print("El libro ya esta registrado.")
                return

    

    with open(path,'a') as file:
        file.write(f"{titulo},{autor}\n")
    print("Libro agregado exitosamente!")

    logging.info(f"Nuevo libro agregado: {titulo} por {autor}")



def ver_libros():

    path = "data/libros.txt"

    if not os.path.exists(path):
        print("No hay libros registrados.")
        return

    print("\nLibros registrados:")
    with open(path,'r') as file:
        for linea in file:
            linea = linea.strip()
            if not linea or "," not in linea:
                continue
            titulo, autor = linea.split(",", 1)
            print(f"Titulo: {titulo}, Autor: {autor}")


def prestar_libro(username):
    path_libros = "data/libros.txt"
    path_prestamos = "data/prestamos.txt"


    if not os.path.exists(path_libros):
        print("No hay libros registrados.")
        return
    

    titulo = input("Ingrese el titulo del libro a prestar: ")

    
    disponible = "False"
    with open(path_libros, 'r') as file:
        for linea in file:
            libro_titulo, autor = linea.strip().split(",")
            if libro_titulo.lower() == titulo.lower():
                disponible = "True"

                with open(path_prestamos, 'a') as file:
                    file.write(f"{libro_titulo},{username}\n")

                logging.info(f"Libro prestado: {libro_titulo} por {username}")
                print(f"Libro: {libro_titulo} prestado exitosamente")
                break  

    if disponible == "False":
        print("El libro no esta disponible.")





    
def devolver_libro(username):
    path_prestamos = "data/prestamos.txt"

    if not os.path.exists(path_prestamos):
        print("No hay prestamos registrados.")
        return

    titulo = input("Ingrese el titulo del libro a devolver: ")

    prestamos = []
    encontrado = False

    with open(path_prestamos,'r') as file:
        for linea in file:
            libro_titulo,usuario = linea.strip().split(",")
            prestamos.append((libro_titulo,usuario))
            if libro_titulo.lower() == titulo.lower() and usuario == username:
                encontrado = True

    if not encontrado:
        print("No se encontro el prestamo para este libro y usuario.")
        return

    with open(path_prestamos,'w') as file:
        for libro_titulo,usuario in prestamos:
            if not (libro_titulo.lower() == titulo.lower() and usuario == username):
                file.write(f"{libro_titulo},{usuario}\n")

    logging.info(f"Libro devuelto: {titulo} por {username}")
    print("Libro devuelto exitosamente!")



def menu_usuario(username):
    while True:
        print(f"\nBienvenido, {username}")
        print("1. Ver libros")
        print("2. Agregar libro")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            ver_libros()
        elif opcion == '2':
            agregar_libros()
        elif opcion == '3':
            prestar_libro(username)
        elif opcion == '4':
            devolver_libro(username)
        elif opcion == '5':
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")





def main():
    while True:
        print("\n1. Registrar")
        print("2. Login")
        print("3. Salir")
        choice = input("Seleccione una opcion: ")

        if choice == '1':
            register()
        elif choice == '2':
            username = login()  
            if username:
                menu_usuario(username)
        elif choice == '3':
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

main()