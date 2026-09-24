import tkinter as tk
from tkinter import messagebox

from paciente import Paciente
from medico import Medico
from cita import Cita


class Main:

    def __init__(self):

        # Creamos las listas donde vamos a guardar los objetos
        self.pacientes = []
        self.medicos = []
        self.citas = []

        # Creamos la ventana principal
        ventana = tk.Tk()
        ventana.title("Sistema de Salud")
        ventana.geometry("600x500")

        # Titulo de la ventana
        tk.Label(
            ventana,
            text="SISTEMA DE SALUD",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

        # =========================
        # BOTONES DE PACIENTES
        # =========================

        boton_registrar = tk.Button(
            ventana,
            text="Registrar Paciente",
            width=25,
            command=self.registrar_paciente
        )
        boton_registrar.pack(pady=5)

        boton_listar = tk.Button(
            ventana,
            text="Listar Pacientes",
            width=25,
            command=self.listar_pacientes
        )
        boton_listar.pack(pady=5)

        boton_buscar = tk.Button(
            ventana,
            text="Buscar Paciente",
            width=25,
            command=self.buscar_paciente
        )
        boton_buscar.pack(pady=5)

        # =========================
        # BOTONES DE MEDICOS
        # =========================

        boton_registrar_medico = tk.Button(
            ventana,
            text="Registrar Médico",
            width=25,
            command=self.registrar_medico
        )
        boton_registrar_medico.pack(pady=5)

        boton_listar_medicos = tk.Button(
            ventana,
            text="Listar Médicos",
            width=25,
            command=self.listar_medicos
        )
        boton_listar_medicos.pack(pady=5)

        boton_listar_medicos = tk.Button(
            ventana,
            text="Listar Médicos",
            width=25,
            command=self.listar_medicos
        )
        boton_listar_medicos.pack(pady=5)

        # =========================
        # BOTONES DE CITAS
        # =========================

        boton_registrar_cita = tk.Button(
            ventana,
            text="Registrar Cita",
            width=25,
            command=self.registrar_cita
        )
        boton_registrar_cita.pack(pady=5)

        boton_listar_citas = tk.Button(
            ventana,
            text="Listar Citas",
            width=25,
            command=self.listar_citas
        )
        boton_listar_citas.pack(pady=5)

        boton_buscar_cita = tk.Button(
            ventana,
            text="Buscar Cita",
            width=25,
            command=self.buscar_cita
        )
        boton_buscar_cita.pack(pady=5)

        # =========================
        # DATOS DE PRUEBA
        # =========================

        paciente1 = Paciente(
            "P001",
            "Jean Carlos",
            "04/12/2000",
            "47201398",
            70.5
        )

        paciente2 = Paciente(
            "P002",
            "Ana Li",
            "12/11/2000",
            "43232111",
            65.7
        )

        paciente3 = Paciente(
            "P003",
            "Alexandra Sanchez",
            "02/01/2012",
            "66666666",
            22.9
        )

        medico1 = Medico(
            "M001",
            "Juan Perez",
            "Cardiologia"
        )

        cita1 = Cita(
            "C001",
            paciente1,
            "23/09/2026",
            "14:00",
            medico1,
            "Gripe"
        )

        # Agregamos los objetos a sus respectivas listas
        self.pacientes.append(paciente1)
        self.pacientes.append(paciente2)
        self.pacientes.append(paciente3)

        self.medicos.append(medico1)

        self.citas.append(cita1)

        # Iniciamos la ventana
        ventana.mainloop()

    # ==================================================
    # REGISTRAR PACIENTE
    # ==================================================

    def registrar_paciente(self):

        # Creamos una ventana para registrar
        ventana = tk.Toplevel()
        ventana.title("Registrar Paciente")
        ventana.geometry("400x400")

        # Codigo
        tk.Label(ventana, text="Código:").pack()
        codigo = tk.Entry(ventana)
        codigo.pack()

        # Nombre
        tk.Label(ventana, text="Nombre:").pack()
        nombre = tk.Entry(ventana)
        nombre.pack()

        # Fecha
        tk.Label(ventana, text="Fecha de nacimiento:").pack()
        fecha = tk.Entry(ventana)
        fecha.pack()

        # DNI
        tk.Label(ventana, text="DNI:").pack()
        dni = tk.Entry(ventana)
        dni.pack()

        # Peso
        tk.Label(ventana, text="Peso:").pack()
        peso = tk.Entry(ventana)
        peso.pack()

        # Boton para guardar
        boton = tk.Button(
            ventana,
            text="Registrar",
            command=lambda: self.guardar_paciente(
                codigo,
                nombre,
                fecha,
                dni,
                peso,
                ventana
            )
        )

        boton.pack(pady=20)

    # ==================================================
    # GUARDAR PACIENTE
    # ==================================================

    def guardar_paciente(
        self,
        codigo,
        nombre,
        fecha,
        dni,
        peso,
        ventana
    ):

        # Verificamos si el codigo ya existe
        for paciente in self.pacientes:

            if paciente.codigo == codigo.get():

                messagebox.showerror(
                    "Error",
                    "El paciente ya existe"
                )

                return

        # Creamos el objeto paciente
        paciente = Paciente(
            codigo.get(),
            nombre.get(),
            fecha.get(),
            dni.get(),
            float(peso.get())
        )

        # Agregamos el paciente a la lista
        self.pacientes.append(paciente)

        print("Paciente registrado correctamente")
        print("Cantidad de pacientes:", len(self.pacientes))

        messagebox.showinfo(
            "Registro",
            "Paciente registrado correctamente"
        )

        # Cerramos la ventana
        ventana.destroy()

    # ==================================================
    # LISTAR PACIENTES
    # ==================================================

    def listar_pacientes(self):

        ventana = tk.Toplevel()
        ventana.title("Lista de Pacientes")
        ventana.geometry("600x600")

        # Recorremos todos los pacientes
        for paciente in self.pacientes:

            texto = f"""
Código: {paciente.codigo}
Nombre: {paciente.nombre}
Fecha de nacimiento: {paciente.fecha_nacimiento}
DNI: {paciente.dni}
Peso: {paciente.peso}
--------------------------------
"""

            tk.Label(
                ventana,
                text=texto,
                justify="left"
            ).pack(
                anchor="w",
                padx=20,
                pady=5
            )

    # ==================================================
    # BUSCAR PACIENTE
    # ==================================================

    def buscar_paciente(self):

        ventana = tk.Toplevel()
        ventana.title("Buscar Paciente")
        ventana.geometry("400x250")

        tk.Label(
            ventana,
            text="Ingrese código del paciente:"
        ).pack(pady=10)

        codigo = tk.Entry(ventana)
        codigo.pack()

        resultado = tk.Label(
            ventana,
            text="",
            justify="left"
        )
        resultado.pack(pady=20)

        def buscar():

            encontrado = False

            for paciente in self.pacientes:

                if paciente.codigo == codigo.get():

                    texto = f"""
Código: {paciente.codigo}
Nombre: {paciente.nombre}
Fecha de nacimiento: {paciente.fecha_nacimiento}
DNI: {paciente.dni}
Peso: {paciente.peso}
"""

                    resultado.config(text=texto)

                    encontrado = True
                    break

            if not encontrado:

                resultado.config(
                    text="Paciente no encontrado"
                )

        tk.Button(
            ventana,
            text="Buscar",
            command=buscar
        ).pack()

    # ==================================================
    # REGISTRAR MEDICO
    # ==================================================

    def registrar_medico(self):

        ventana = tk.Toplevel()
        ventana.title("Registrar Médico")
        ventana.geometry("400x300")

        tk.Label(ventana, text="Código:").pack()
        codigo = tk.Entry(ventana)
        codigo.pack()

        tk.Label(ventana, text="Nombre:").pack()
        nombre = tk.Entry(ventana)
        nombre.pack()

        tk.Label(ventana, text="Especialidad:").pack()
        especialidad = tk.Entry(ventana)
        especialidad.pack()

        boton = tk.Button(
            ventana,
            text="Registrar",
            command=lambda: self.guardar_medico(
                codigo,
                nombre,
                especialidad,
                ventana
            )
        )

        boton.pack(pady=20)

    # ==================================================
    # GUARDAR MEDICO
    # ==================================================

    def guardar_medico(
        self,
        codigo,
        nombre,
        especialidad,
        ventana
    ):

        # Buscamos si el medico ya existe
        for medico in self.medicos:

            if medico.codigo == codigo.get():

                messagebox.showerror(
                    "Error",
                    "El médico ya existe"
                )

                return

        # Creamos el objeto medico
        medico = Medico(
            codigo.get(),
            nombre.get(),
            especialidad.get()
        )

        # Agregamos el medico a la lista
        self.medicos.append(medico)

        print("Médico registrado correctamente")

        messagebox.showinfo(
            "Registro",
            "Médico registrado correctamente"
        )

        ventana.destroy()

    # ==================================================
    # LISTAR MEDICOS
    # ==================================================

    def listar_medicos(self):

        ventana = tk.Toplevel()
        ventana.title("Lista de Médicos")
        ventana.geometry("500x500")

        for medico in self.medicos:

            texto = f"""
Código: {medico.codigo}
Nombre: {medico.nombre}
Especialidad: {medico.especialidad}
--------------------------------
"""

            tk.Label(
                ventana,
                text=texto,
                justify="left"
            ).pack(
                anchor="w",
                padx=20,
                pady=5
            )

    # ==================================================
    # REGISTRAR CITA
    # ==================================================

    def registrar_cita(self):

        ventana = tk.Toplevel()
        ventana.title("Registrar Cita")
        ventana.geometry("400x450")

        tk.Label(ventana, text="Número de cita:").pack()
        nro_cita = tk.Entry(ventana)
        nro_cita.pack()

        tk.Label(ventana, text="Código del paciente:").pack()
        codigo_paciente = tk.Entry(ventana)
        codigo_paciente.pack()

        tk.Label(ventana, text="Fecha:").pack()
        fecha = tk.Entry(ventana)
        fecha.pack()

        tk.Label(ventana, text="Hora:").pack()
        hora = tk.Entry(ventana)
        hora.pack()

        tk.Label(ventana, text="Código del médico:").pack()
        codigo_medico = tk.Entry(ventana)
        codigo_medico.pack()

        tk.Label(ventana, text="Diagnóstico:").pack()
        diagnostico = tk.Entry(ventana)
        diagnostico.pack()

        boton = tk.Button(
            ventana,
            text="Registrar",
            command=lambda: self.guardar_cita(
                nro_cita,
                codigo_paciente,
                fecha,
                hora,
                codigo_medico,
                diagnostico,
                ventana
            )
        )

        boton.pack(pady=20)

    # ==================================================
    # GUARDAR CITA
    # ==================================================

    def guardar_cita(
        self,
        nro_cita,
        codigo_paciente,
        fecha,
        hora,
        codigo_medico,
        diagnostico,
        ventana
    ):

        # Buscamos el paciente
        paciente_encontrado = None

        for paciente in self.pacientes:

            if paciente.codigo == codigo_paciente.get():

                paciente_encontrado = paciente
                break

        # Buscamos el medico
        medico_encontrado = None

        for medico in self.medicos:

            if medico.codigo == codigo_medico.get():

                medico_encontrado = medico
                break

        # Verificamos si existe la cita
        for cita in self.citas:

            if cita.nro_cita == nro_cita.get():

                messagebox.showerror(
                    "Error",
                    "La cita ya existe"
                )

                return

        # Verificamos que exista el paciente
        if paciente_encontrado is None:

            messagebox.showerror(
                "Error",
                "Paciente no encontrado"
            )

            return

        # Verificamos que exista el medico
        if medico_encontrado is None:

            messagebox.showerror(
                "Error",
                "Médico no encontrado"
            )

            return

        # Creamos la cita
        cita = Cita(
            nro_cita.get(),
            paciente_encontrado,
            fecha.get(),
            hora.get(),
            medico_encontrado,
            diagnostico.get()
        )

        # Agregamos la cita a la lista
        self.citas.append(cita)

        print("Cita registrada correctamente")

        messagebox.showinfo(
            "Registro",
            "Cita registrada correctamente"
        )

        ventana.destroy()

    # ==================================================
    # LISTAR CITAS
    # ==================================================

    def listar_citas(self):

        ventana = tk.Toplevel()
        ventana.title("Lista de Citas")
        ventana.geometry("600x600")

        for cita in self.citas:

            texto = f"""
Número de cita: {cita.nro_cita}
Paciente: {cita.paciente.nombre}
Fecha: {cita.fecha}
Hora: {cita.hora}
Médico: {cita.medico.nombre}
Especialidad: {cita.medico.especialidad}
Diagnóstico: {cita.diagnostico}
--------------------------------
"""

            tk.Label(
                ventana,
                text=texto,
                justify="left"
            ).pack(
                anchor="w",
                padx=20,
                pady=5
            )

    # ==================================================
    # BUSCAR CITA
    # ==================================================

    def buscar_cita(self):

        ventana = tk.Toplevel()
        ventana.title("Buscar Cita")
        ventana.geometry("450x350")

        tk.Label(
            ventana,
            text="Ingrese número de cita:"
        ).pack(pady=10)

        nro_cita = tk.Entry(ventana)
        nro_cita.pack()

        resultado = tk.Label(
            ventana,
            text="",
            justify="left"
        )

        resultado.pack(pady=20)

        def buscar():

            encontrado = False

            for cita in self.citas:

                if cita.nro_cita == nro_cita.get():

                    texto = f"""
Número de cita: {cita.nro_cita}
Paciente: {cita.paciente.nombre}
Fecha: {cita.fecha}
Hora: {cita.hora}
Médico: {cita.medico.nombre}
Especialidad: {cita.medico.especialidad}
Diagnóstico: {cita.diagnostico}
"""

                    resultado.config(text=texto)

                    encontrado = True
                    break

            if not encontrado:

                resultado.config(
                    text="Cita no encontrada"
                )

        tk.Button(
            ventana,
            text="Buscar",
            command=buscar
        ).pack()


Main()