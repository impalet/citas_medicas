

from paciente import Paciente
from medico import Medico
from cita import Cita


class Main:

    def __init__(self):

        pacientes=[]
        medicos=[]
        citas=[]



        #prueba objetos
        paciente1=Paciente("P001","jean carlos","04/12/2000","47201398",70.5)
        paciente2=Paciente("P002","Ana li","12/11/2000","43232111",65.70)
        paciente3=Paciente("P003","Alexandra sanchez","02/01/2012","66666666",22.90)
        medico1=Medico("M001","Juan Perez","Cardiologia")
        cita1=Cita("C001","23/09/2026","14:00","Gripe",paciente1,medico1)

        pacientes.append(paciente1)
        medicos.append(medico1)
        citas.append(cita1)
        pacientes.append(paciente2)
        pacientes.append(paciente3)

        
        opcion=0
        while opcion !=4:
            #opciones
            print("""
1. Buscar Paciente
2. Buscar Cita
3. Listar Pacientes
4. Salir
5. Registrar Paciente
6. Registrar Cita
7. Registrar Medico
8. Listar Medicos

""")
            opcion=int(input("Ingrese una opcion: "))
            match opcion:             
                case 1:     
                    #buscar Paciente
                    codigo_buscar=input("ingrese codigo del paciente: ")
                    encontrado=False
                    for paciente in pacientes:
                        
                        if paciente.codigo ==codigo_buscar:
                            print(f"""Codigo paciente:      {paciente.codigo}
Nombre Paciente:      {paciente.nombre}
Fecha de nacimiento:  {paciente.fecha_nacimiento}
DNI:                  {paciente.dni}
Peso:                 {paciente.peso}
""")
                            encontrado=True
                        
                    if not encontrado :
                        print("Paciente no encontrado")
                case 2:
                    #Buscar cita
                    codigo_buscar=input("Ingrese codigo de cita: ")
                    encontrado=False
                    for cita in citas:
                        if cita.nro_cita == codigo_buscar:
            
                            print(f"""----------------------------------------------
N° de Cita: {cita.nro_cita}
----------------------------------------------
Nombre : {cita.paciente.nombre}
Fecha de cita: {cita.fecha}
Hora de cita: {cita.hora} 
----------------------------------------------
Dr.:  {cita.medico.nombre}         
Especialidad:  {cita.medico.especialidad}
Diagnostico:   {cita.diagnostico}
----------------------------------------------""")
                            encontrado=True
                    if not encontrado:
                        print("Cita no encontrada")
                case 3:
                    for paciente in pacientes:
                                print(f"""Codigo paciente:      {paciente.codigo}
Nombre Paciente:      {paciente.nombre}
Fecha de nacimiento:  {paciente.fecha_nacimiento}
DNI:                  {paciente.dni}
Peso:                 {paciente.peso}
""")
                case 4:
                    print("Salir")

                case 5:

                    encontrado=False
                    
                    cod_pac=input("Ingrese codigo de paciente: ")
                    nom_pac=input("Ingrese nombre de paciente: ")
                    fec_nac=input("Ingrese fecha de nacimiento: ")
                    dni=input("Ingrese DNI: ")
                    peso=float(input("Ingrese peso: "))
                    for paciente in pacientes:
                        if paciente.codigo == cod_pac:
                            encontrado=True
                            break

                    if encontrado:
                        print("Paciente ya existe!!! ")
                    else:
                        paciente=Paciente(cod_pac,nom_pac,fec_nac,dni,peso)

                        pacientes.append(paciente)

                        print("Paciente registrado correctamente")
                case 6:
                    encontrado = False
                    paciente_encontrado = None
                    medico_encontrado = None

                    num_cita = input("Ingrese N° de cita (C000): ")
                    num_pac = input("Ingrese Codigo paciente (P000): ")
                    fecha = input("Ingrese fecha (11/11/2222): ")
                    hora = input("Ingrese hora (24:00): ")
                    num_medico = input("Ingrese codigo de Medico (M000): ")
                    diagnostico = input("Ingrese diagnostico: ")

                    # Buscar si la cita ya existe
                    for cita in citas:
                        if cita.nro_cita == num_cita:
                            encontrado = True
                            break

                    # Buscar paciente
                    for paciente in pacientes:
                        if paciente.codigo == num_pac:
                            paciente_encontrado = paciente
                            break

                    # Buscar medico
                    for medico in medicos:
                        if medico.codigo == num_medico:
                            medico_encontrado = medico
                            break

                    if encontrado:
                        print("Cita ya existe!!!")

                    elif paciente_encontrado is None:
                        print("Paciente no encontrado")

                    elif medico_encontrado is None:
                        print("Medico no encontrado")

                    else:
                        cita = Cita(num_cita,paciente_encontrado,fecha,hora,medico_encontrado,diagnostico)

                        citas.append(cita)

                        print("Cita registrada correctamente")

                case 7:
                    encontrado=False
                                        
                    cod_med=input("Ingrese codigo de Medico: ")
                    nom_med=input("Ingrese nombre de Medico: ")
                    esp_med=input("Ingrese especialidad: ")
                    
                    for medico in medicos:
                        if medico.codigo == cod_med:
                            encontrado=True
                            break

                    if encontrado:
                        print("Medico ya existe!!! ")
                    else:
                        medico=Medico(cod_med,nom_med,esp_med)

                        medicos.append(medico)

                        print("Medico registrado correctamente")
                case 8:
                    for medico in medicos:
                        print(f"""Codigo Medico:      {medico.codigo}
Nombre del Medico:  {medico.nombre}
Especialidad:       {medico.especialidad}
""")                      
                case _:
                    print("Opcion no valida")
        
        
Main()