import csv
import numpy as np 
import Email

class arrayemail():
    __cantidad = int
    __dimension = int
    __incremento = 5
    __correos = ""
    def __init__(self, dim):
        self.__cantidad = 0
        self.__dimension = dim
        self.__correos = np.empty(dim, dtype=Email.Email)
    def agregarcorreo(self, correo):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__correos.resize(self.__dimension)
        else:
            pass
        if type(correo) == Email.Email:
            self.__correos[self.__cantidad] = correo
            self.__cantidad +=1
            return True
        else:
            return False
    def getcorreo(self, ind):
        return (self.__correos[ind])
    def ultposicion(self):
        return(self.__cantidad-1)

   
   
def testing(emails):   
    Name = "Santiago Graziano"
    if emails.agregarcorreo(Email.Email().emailbyname(Name, "gmail", "com")):   
        print("Estimado {} te enviaremos tus mensajes a la dirección {}".format(Name, emails.getcorreo(emails.ultposicion()).retornaEmail()))
    else: 
        print("Error al crear")

    if emails.agregarcorreo(Email.Email().CrearCuenta("alumnopoo.com")):
        while input("Ingrese Contrasena actual: ") != emails.getcorreo(emails.ultposicion()).getpassword():
            print("Contrasena incorrecta")
        emails.getcorreo(emails.ultposicion()).changepassword(input('Ingrese su nueva contrasena: '))
    else:
        print("Error al crear")

    archi = open('poo.csv')
    reader = csv.reader(archi, delimiter=',')
    dombuscar = input('Ingrese Dominio a buscar: ')
    contador = int(0)
    bandera = True
    for fila in reader:
        if bandera:
            bandera = False
        else:
            for em in fila:
                emails.agregarcorreo(Email.Email().CrearCuenta(em))
                if emails.getcorreo(emails.ultposicion()).getDominio() == dombuscar:
                    contador += 1
    archi.close()
    print('Hay {} emails con ese Dominio'.format(contador))

if __name__ == "__main__":
    emails = arrayemail(15)
    testing(emails)