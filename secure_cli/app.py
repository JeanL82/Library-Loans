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
                return
            
    logging.warning(f"Fallo de login para el usuario: {username}")
    print("Nombre de usuario o contrasena incorrectos.")








def main():
    while True:
        print("\n1. Registrar")
        print("2. Login")
        print("3. Salir")
        choice = input("Seleccione una opcion: ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Saliendo...")
            break
        else:
            print("Opcion invalida. Intente de nuevo.")