
class Paciente:

    def __init__(self,codigo,nombre,fecha_nacimiento,dni,peso):
        self._codigo=codigo
        self.nombre=nombre
        self._fecha_nacimiento=fecha_nacimiento
        self.dni=dni
        #necsitamos que pase por el setter antes de ser usado
        self.peso=peso

    @property
    def codigo(self):
        return self._codigo
    @property
    def nombre(self):
        return self._nombre
    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento
    @property
    def dni(self):
        return self._dni
    @property
    def peso(self):
        return self._peso
    #isinstancie  nos ayuda a verificar si es int,float etc 
    @codigo.setter
    def codigo(self,valor):
        self._codigo=valor
    @nombre.setter
    def nombre(self,valor):
        anterior=""

        for letra in valor:

            if not letra.isalpha() and not letra.isspace():
                print("nombre no valido")

            if letra==" " and anterior==" " :
                print("Nombre no valido")
            
            anterior=letra
            
        self._nombre=valor
    @fecha_nacimiento.setter
    def fecha_nacimiento(self,valor):
        self._fecha_nacimiento=valor
    @dni.setter
    def dni(self,valor):
        if len(valor) == 8 and valor.isdigit():
            self._dni=valor
        else:
            print("DNI ingresado no es valido")
            self._dni=""
    @peso.setter
    def peso(self,valor):
        if isinstance(valor,(int,float)) and valor >= 0:
            self._peso=valor
        else:
            print("Peso ingresado no es valido")
            self._peso=0