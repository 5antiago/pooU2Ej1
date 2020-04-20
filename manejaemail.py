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
    def testing(self):
        lista = []
        lista.append(Email.Email("alumno", "poo", "com" ))
        print(lista[0].retornaEmail())
        lista.append(Email.Email().CrearCuenta("alumnogmail.com"))
        print(lista[-1])
        lista.append(Email.Email().emailbyname("Nombre Apellido", "gmail", "com"))
        print("{}".format(lista[-1].retornaEmail()))
        print(lista[-1].getpassword == "1236")