import tkinter as tk
from paciente import Paciente
from medico import Medico
from cita import Cita


class Main:

    def __init__(self):

        # Listas donde se guardan los objetos
        self.pacientes = []
        self.medicos = []
        self.citas = []

        # -----------------------------
        # DATOS DE PRUEBA
        # -----------------------------

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
            65.70
        )

        paciente3 = Paciente(
            "P003",
            "Alexandra Sanchez",
            "02/01/2012",
            "66666666",
            22.90
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

        # Agregamos los objetos a las listas
        self.pacientes.append(paciente1)
        self.pacientes.append(paciente2)
        self.pacientes.append(paciente3)

        self.medicos.append(medico1)

        self.citas.append(cita1)

        # -----------------------------
        # VENTANA PRINCIPAL
        # -----------------------------

        ventana = tk.Tk()

        ventana.title("Sistema de Salud")
        ventana.geometry("700x500")
        ventana.configure(bg="#EAF4F8")

        # -----------------------------
        # ENCABEZADO
        # -----------------------------

        encabezado = tk.Frame(
            ventana,
            bg="#1976D2",
            height=100
        )

        encabezado.pack(fill="x")

        titulo = tk.Label(
            encabezado,
            text="SISTEMA DE SALUD",
            font=("Arial", 24, "bold"),
            bg="#1976D2",
            fg="white"
        )

        titulo.pack(pady=(20, 0))

        subtitulo = tk.Label(
            encabezado,
            text="Gestión de pacientes, médicos y citas",
            font=("Arial", 11),
            bg="#1976D2",
            fg="white"
        )

        subtitulo.pack()

        # -----------------------------
        # MENÚ PRINCIPAL
        # -----------------------------

        menu = tk.Frame(
            ventana,
            bg="#EAF4F8"
        )

        menu.pack(pady=30)

        # Título del menú

        texto_menu = tk.Label(
            menu,
            text="MENÚ PRINCIPAL",
            font=("Arial", 16, "bold"),
            bg="#EAF4F8",
            fg="#263238"
        )

        texto_menu.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(0, 20)
        )

        # Botón registrar paciente

        boton_registrar = tk.Button(
            menu,
            text="Registrar Paciente",
            command=self.registrar_paciente,
            width=22,
            height=2,
            bg="#2196F3",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat"
        )

        boton_registrar.grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        # Botón listar pacientes

        boton_listar = tk.Button(
            menu,
            text="Listar Pacientes",
            command=self.listar_pacientes,
            width=22,
            height=2,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat"
        )

        boton_listar.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        # Botón registrar médico

        boton_medico = tk.Button(
            menu,
            text="Registrar Médico",
            command=self.registrar_medico,
            width=22,
            height=2,
            bg="#673AB7",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat"
        )

        boton_medico.grid(
            row=2,
            column=0,
            padx=10,
            pady=10
        )

        # Botón listar médicos

        boton_listar_medicos = tk.Button(
            menu,
            text="Listar Médicos",
            command=self.listar_medicos,
            width=22,
            height=2,
            bg="#9C27B0",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat"
        )

        boton_listar_medicos.grid(
            row=2,
            column=1,
            padx=10,
            pady=10
        )

        # Botón registrar cita

        boton_cita = tk.Button(
            menu,
            text="Registrar Cita",
            command=self.registrar_cita,
            width=22,
            height=2,
            bg="#009688",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat"
        )

        boton_cita.grid(
            row=3,
            column=0,
            padx=10,
            pady=10
        )

        # Botón listar citas

        boton_listar_citas = tk.Button(
            menu,
            text="Listar Citas",
            command=self.listar_citas,
            width=22,
            height=2,
            bg="#FF9800",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat"
        )

        boton_listar_citas.grid(
            row=3,
            column=1,
            padx=10,
            pady=10
        )

        # -----------------------------
        # INFORMACIÓN INFERIOR
        # -----------------------------

        pie = tk.Label(
            ventana,
            text="Sistema de gestión clínica",
            font=("Arial", 10),
            bg="#EAF4F8",
            fg="#607D8B"
        )

        pie.pack(side="bottom", pady=15)

        # Iniciamos la ventana
        ventana.mainloop()

    # =====================================================
    # REGISTRAR PACIENTE
    # =====================================================

    def registrar_paciente(self):

        ventana = tk.Toplevel()

        ventana.title("Registrar Paciente")
        ventana.geometry("400x400")
        ventana.configure(bg="#EAF4F8")

        titulo = tk.Label(
            ventana,
            text="REGISTRAR PACIENTE",
            font=("Arial", 18, "bold"),
            bg="#EAF4F8",
            fg="#1976D2"
        )

        titulo.pack(pady=20)

        # Código

        tk.Label(
            ventana,
            text="Código:",
            bg="#EAF4F8"
        ).pack()

        codigo = tk.Entry(ventana)
        codigo.pack(pady=5)

        # Nombre

        tk.Label(
            ventana,
            text="Nombre:",
            bg="#EAF4F8"
        ).pack()

        nombre = tk.Entry(ventana)
        nombre.pack(pady=5)

        # Fecha

        tk.Label(
            ventana,
            text="Fecha de nacimiento:",
            bg="#EAF4F8"
        ).pack()

        fecha = tk.Entry(ventana)
        fecha.pack(pady=5)

        # DNI

        tk.Label(
            ventana,
            text="DNI:",
            bg="#EAF4F8"
        ).pack()

        dni = tk.Entry(ventana)
        dni.pack(pady=5)

        # Peso

        tk.Label(
            ventana,
            text="Peso:",
            bg="#EAF4F8"
        ).pack()

        peso = tk.Entry(ventana)
        peso.pack(pady=5)

        # Botón

        boton = tk.Button(
            ventana,
            text="Registrar",
            width=20,
            bg="#2196F3",
            fg="white",
            font=("Arial", 10, "bold"),
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

    # =====================================================
    # GUARDAR PACIENTE
    # =====================================================

    def guardar_paciente(
        self,
        codigo,
        nombre,
        fecha,
        dni,
        peso,
        ventana
    ):

        paciente = Paciente(
            codigo.get(),
            nombre.get(),
            fecha.get(),
            dni.get(),
            float(peso.get())
        )

        self.pacientes.append(paciente)

        print("Paciente registrado correctamente")

        ventana.destroy()

    # =====================================================
    # LISTAR PACIENTES
    # =====================================================

    def listar_pacientes(self):

        ventana = tk.Toplevel()

        ventana.title("Lista de Pacientes")
        ventana.geometry("550x500")
        ventana.configure(bg="#EAF4F8")

        titulo = tk.Label(
            ventana,
            text="LISTA DE PACIENTES",
            font=("Arial", 18, "bold"),
            bg="#EAF4F8",
            fg="#1976D2"
        )

        titulo.pack(pady=15)

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
                justify="left",
                bg="white",
                font=("Arial", 10)
            ).pack(
                anchor="w",
                padx=30,
                pady=5,
                fill="x"
            )

    # =====================================================
    # REGISTRAR MÉDICO
    # =====================================================

    def registrar_medico(self):

        ventana = tk.Toplevel()

        ventana.title("Registrar Médico")
        ventana.geometry("400x300")
        ventana.configure(bg="#EAF4F8")

        titulo = tk.Label(
            ventana,
            text="REGISTRAR MÉDICO",
            font=("Arial", 18, "bold"),
            bg="#EAF4F8",
            fg="#673AB7"
        )

        titulo.pack(pady=20)

        tk.Label(
            ventana,
            text="Código:",
            bg="#EAF4F8"
        ).pack()

        codigo = tk.Entry(ventana)
        codigo.pack(pady=5)

        tk.Label(
            ventana,
            text="Nombre:",
            bg="#EAF4F8"
        ).pack()

        nombre = tk.Entry(ventana)
        nombre.pack(pady=5)

        tk.Label(
            ventana,
            text="Especialidad:",
            bg="#EAF4F8"
        ).pack()

        especialidad = tk.Entry(ventana)
        especialidad.pack(pady=5)

        boton = tk.Button(
            ventana,
            text="Registrar",
            width=20,
            bg="#673AB7",
            fg="white",
            font=("Arial", 10, "bold"),
            command=lambda: self.guardar_medico(
                codigo,
                nombre,
                especialidad,
                ventana
            )
        )

        boton.pack(pady=20)

    # =====================================================
    # GUARDAR MÉDICO
    # =====================================================

    def guardar_medico(
        self,
        codigo,
        nombre,
        especialidad,
        ventana
    ):

        medico = Medico(
            codigo.get(),
            nombre.get(),
            especialidad.get()
        )

        self.medicos.append(medico)

        print("Médico registrado correctamente")

        ventana.destroy()

    # =====================================================
    # LISTAR MÉDICOS
    # =====================================================

    def listar_medicos(self):

        ventana = tk.Toplevel()

        ventana.title("Lista de Médicos")
        ventana.geometry("500x400")
        ventana.configure(bg="#EAF4F8")

        titulo = tk.Label(
            ventana,
            text="LISTA DE MÉDICOS",
            font=("Arial", 18, "bold"),
            bg="#EAF4F8",
            fg="#673AB7"
        )

        titulo.pack(pady=15)

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
                justify="left",
                bg="white",
                font=("Arial", 10)
            ).pack(
                anchor="w",
                padx=30,
                pady=5,
                fill="x"
            )

    # =====================================================
    # REGISTRAR CITA
    # =====================================================

    def registrar_cita(self):

        ventana = tk.Toplevel()

        ventana.title("Registrar Cita")
        ventana.geometry("400x450")
        ventana.configure(bg="#EAF4F8")

        titulo = tk.Label(
            ventana,
            text="REGISTRAR CITA",
            font=("Arial", 18, "bold"),
            bg="#EAF4F8",
            fg="#009688"
        )

        titulo.pack(pady=15)

        tk.Label(
            ventana,
            text="Número de cita:",
            bg="#EAF4F8"
        ).pack()

        nro_cita = tk.Entry(ventana)
        nro_cita.pack(pady=5)

        tk.Label(
            ventana,
            text="Código del paciente:",
            bg="#EAF4F8"
        ).pack()

        codigo_paciente = tk.Entry(ventana)
        codigo_paciente.pack(pady=5)

        tk.Label(
            ventana,
            text="Fecha:",
            bg="#EAF4F8"
        ).pack()

        fecha = tk.Entry(ventana)
        fecha.pack(pady=5)

        tk.Label(
            ventana,
            text="Hora:",
            bg="#EAF4F8"
        ).pack()

        hora = tk.Entry(ventana)
        hora.pack(pady=5)

        tk.Label(
            ventana,
            text="Código del médico:",
            bg="#EAF4F8"
        ).pack()

        codigo_medico = tk.Entry(ventana)
        codigo_medico.pack(pady=5)

        tk.Label(
            ventana,
            text="Diagnóstico:",
            bg="#EAF4F8"
        ).pack()

        diagnostico = tk.Entry(ventana)
        diagnostico.pack(pady=5)

        boton = tk.Button(
            ventana,
            text="Registrar Cita",
            width=20,
            bg="#009688",
            fg="white",
            font=("Arial", 10, "bold"),
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

        boton.pack(pady=15)

    # =====================================================
    # GUARDAR CITA
    # =====================================================

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

        paciente_encontrado = None
        medico_encontrado = None

        # Buscamos el paciente

        for paciente in self.pacientes:

            if paciente.codigo == codigo_paciente.get():

                paciente_encontrado = paciente
                break

        # Buscamos el médico

        for medico in self.medicos:

            if medico.codigo == codigo_medico.get():

                medico_encontrado = medico
                break

        # Verificamos que existan

        if paciente_encontrado is None:

            print("Paciente no encontrado")

        elif medico_encontrado is None:

            print("Médico no encontrado")

        else:

            cita = Cita(
                nro_cita.get(),
                paciente_encontrado,
                fecha.get(),
                hora.get(),
                medico_encontrado,
                diagnostico.get()
            )

            self.citas.append(cita)

            print("Cita registrada correctamente")

            ventana.destroy()

    # =====================================================
    # LISTAR CITAS
    # =====================================================

    def listar_citas(self):

        ventana = tk.Toplevel()

        ventana.title("Lista de Citas")
        ventana.geometry("600x500")
        ventana.configure(bg="#EAF4F8")

        titulo = tk.Label(
            ventana,
            text="LISTA DE CITAS",
            font=("Arial", 18, "bold"),
            bg="#EAF4F8",
            fg="#009688"
        )

        titulo.pack(pady=15)

        for cita in self.citas:

            texto = f"""
N° de Cita: {cita.nro_cita}
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
                justify="left",
                bg="white",
                font=("Arial", 10)
            ).pack(
                anchor="w",
                padx=30,
                pady=5,
                fill="x"
            )


Main()