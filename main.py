import csv
import Email
import manejaemail 

if __name__ == "__main__":
    emails = manejaemail.arrayemail(15)
    Name = input("Ingrese Nombre: ")
    if emails.agregarcorreo(Email.Email().emailbyname(Name, "gmail", "com")):   
        print("Estimado {} te enviaremos tus mensajes a la dirección {}".format(Name, emails.getcorreo(emails.ultposicion()).retornaEmail()))
    else: 
        print("Error al crear")

    if emails.agregarcorreo(Email.Email().CrearCuenta(input("Ingrese Correo: "))):
        while input("Ingrese Contrasena actual: ") != emails.getcorreo(emails.ultposicion()).getpassword():
            print("Contrasena incorrecta")
        emails.getcorreo(emails.ultposicion()).changepassword(input('Ingrese su nueva contrasena: '))
    else:
        print("Error al crear")

    archi = open('poo.csv')
    reader = csv.reader(archi)
    dombuscar = input('Ingrese Dominio a buscar: ')
    contador = int(0)
    bandera = True
    for fila in reader:
        if bandera:
            bandera = False
        else:
            emails.agregarcorreo(Email.Email().CrearCuenta(fila[0]))
            if emails.getcorreo(emails.ultposicion()).getDominio() == dombuscar:
                contador += 1
    archi.close()

    print('Hay {} emails con ese Dominio'.format(contador))