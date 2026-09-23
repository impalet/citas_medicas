class Medico:

    def __init__(self,codigo,nombre,especialidad):
        self.codigo=codigo
        self.nombre=nombre
        self.especialidad=especialidad

    @property
    def codigo(self):
        return self._codigo
    @property
    def nombre(self):
        return self._nombre
    @property
    def especialidad(self):
        return self._especialidad
    @codigo.setter
    def codigo(self, valor):
        valido = True

        if len(valor) !=4:
            valido=False
        else:
            if valor[0] !="M":
                valido=False
            if not valor[1].isdigit():
                valido=False
            if not valor[2].isdigit():
                valido=False
            if not valor[3].isdigit():
                valido=False
        

        if valido:
            self._codigo = valor
        else:
            print("Codigo no valido")
            self._codigo = ""
    @nombre.setter
    def nombre(self,valor):
            anterior=""
            valido= True
            if valor=="":
                valido=False
                print("Nombre no valido")
            for letra in valor:
    
                if not letra.isalpha() and not letra.isspace():
                    valido=False
                    
    
                if letra==" " and anterior==" " :
                    valido=False
                    
                
                anterior=letra
            if valido:
                self._nombre=valor
            else:
                print("Nombre no valido")
                self._nombre=""
    @especialidad.setter
    def especialidad(self,valor):
                anterior=""
                valido= True
                if valor=="":
                    valido=False
                    print("Especialidad no valida")
                for letra in valor:
        
                    if not letra.isalpha() and not letra.isspace():
                        valido=False
                        
        
                    if letra==" " and anterior==" " :
                        valido=False
                        
                    
                    anterior=letra
                if valido:
                    self._especialidad=valor
                else:
                    print("Especialidad no valida")
                    self._especialidad=""