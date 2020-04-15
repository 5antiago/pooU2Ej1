class Email:
    __idcuenta = str
    __dominio = str
    __tipodominio = str
    __contrasena = str
    def __init__(self, id= '', dom='', tdom='', contrasena='123'): #Default password "123"
        if  type(id) == str:                    #Verifica que los parametros sean string
            self.__idcuenta = id
        if type(dom) == str:
            self.__dominio = dom
        if type(tdom) == str:
            self.__tipodominio = tdom
        if type(contrasena) == str:
            self.__contrasena = contrasena
    def retornaEmail(self):
        return str(self.__idcuenta+"@"+self.__dominio+"."+self.__tipodominio)   #Retorna un String con el la forma: example@example.com
    def getDominio(self):
        return str(self.__dominio)          #Devuelve un String con el Dominio
    def CrearCuenta(self, email):
        if type(email) == str:  
            if '@' in email:            
                self.__idcuenta, email = email.split("@")
                self.__dominio, self.__tipodominio = email.split(".", 1)
                return(self)
    def getpassword(self):
        return str(self.__contrasena)
    def changepassword(self, password):
        if type(password) == str:
            self.__contrasena = password
    def emailbyname(self, name, dom, tdom):
        if type(name) == str:
            self.__idcuenta=name.replace(" ", "")
            self.__dominio=dom
            self.__tipodominio=tdom
            return(self)