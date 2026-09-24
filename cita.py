from paciente import Paciente
from medico import Medico




class Cita:

    def __init__(self,nro_cita,paciente,fecha,hora,medico,diagnostico):
        self.nro_cita=nro_cita
        self.fecha=fecha
        self.hora=hora
        self.diagnostico=diagnostico
        self.paciente=paciente
        self.medico=medico

    @property
    def nro_cita(self):
        return self._nro_cita
    @property
    def fecha(self):
        return self._fecha
    @property
    def hora(self):
        return self._hora
    @property
    def diagnostico(self):
        return self._diagnostico
    @property
    def paciente(self):
        return self._paciente
    @property
    def medico(self):
        return self._medico
    @nro_cita.setter
    def nro_cita(self,valor):

        valido = True
        
        if len(valor) !=4:
            valido=False
        else:
            if valor[0] !="C":
                valido=False
            if not valor[1].isdigit():
                valido=False
            if not valor[2].isdigit():
                valido=False
            if not valor[3].isdigit():
                valido=False
        

        if valido:
            self._nro_cita = valor
        else:
            print("Cita no valida")
            self._nro_cita = ""
    @fecha.setter
    def fecha(self,valor):
        valido=True
        if len(valor) !=10:
            valido=False
        else:
            if valor[2] !="/" or valor[5] !="/":
                valido=False
        
        for letra in valor:
            if not letra.isdigit() and letra !="/":
                valido=False
                
        if valido:
            self._fecha=valor
        else:
            print("Fecha no valida")
            self._fecha=""
    @hora.setter
    def hora(self, valor):
        valido = True

        if len(valor) !=5:
            valido=False
        else:
            
            if not valor[0].isdigit():
                valido=False
            if not valor[1].isdigit():
                valido=False
            if valor[2] !=":":
                valido=False
            if not valor[3].isdigit():
                valido=False
            if not valor[4].isdigit():
                valido=False
        

        if valido:
            self._hora = valor
        else:
            print("Hora no valida")
            self._hora = ""
    @diagnostico.setter
    def diagnostico(self,valor):
        valido=True
        if valor=="" or valor ==" ":
            valido=False
        if valido:
            self._diagnostico=valor
        else:
            print("Diagnostico no valido")
            self._diagnostico=""
    @paciente.setter
    def paciente(self, valor):
        if isinstance(valor, Paciente):
            self._paciente = valor
        else:
            print("Paciente no valido")
            self._paciente =None
    @medico.setter
    def medico(self,valor):
        if isinstance(valor,Medico):
            self._medico=valor
        else:
            print("Medico no valido")
            self._medico=None


