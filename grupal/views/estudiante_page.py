import reflex as rx
from grupal.modelos.estudiantes import Estudiantes
from ..servicios.estudiante_servicio import *

class EstudianteState(rx.State):
    estudiantes : list[Estudiantes]
    buscar_cedula : str = ""

    rx.background
    def get_todos_estudiantes(self):
        self.estudiantes = servicio_estudiantes_all()

    rx.background
    def get_estudiante_cedula(self):
        self.estudiantes = servicio_consultar_cedula(self.buscar_cedula)
    
    def buscar_onchange(self, value:str):
        self.buscar_cedula = value

    # crear el metodo para guardar un registro en la bd
    rx.background
    def crear_estudiante(self, data:dict):
        try:
            self.estudiantes = servicio_crear_estudiante(
                data['nombres'], data['apellidos'], data['cedula'],
                data['correo'],data['celular'],data['direccion'],
                data['fono']
                )
        except Exception as e:
            print(e)
    
    @rx.background
    async def eliminar_estudiante(self, id: int):
        async with self: 
            try:
                servicio_eliminar_estudiante(id)
                await self.get_todos_estudiantes()
            except Exception as e:
                print(e)


# pagina que muestre el listado de estudiantes que estan en la base de datos.
@rx.page(route="/estudiantes", title="Lista de Estudiantes", on_load=EstudianteState.get_todos_estudiantes)
def estudiante_page() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.heading("Estudiantes", title="Estudiantes", size="5", center=True, style={"align": "center"}),
            background_color="var(--plum-2)",
            border_radius="10px",
            width="100%",
            margin="16px",
            padding="16px",
            justify="center",
            align="center",
        ),
        
        #tablita con todos os datos de Estudiantes
        rx.vstack(
            buscar_estudiante_cedula(),
            dialog_estudiante_form(),
            
            justify="center",
            style={"margin": "20px", 'width': "100%"},
        ),
        tabla_estudiantes(EstudianteState.estudiantes),
        
        direction="column",
        justify="center",
        style={"margin": "auto", 'width': "80%"},
    )

# crear el componen de tabla para lista de estudiantes
def tabla_estudiantes(lista_estudiantes: list[Estudiantes]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Cedula"),
                rx.table.column_header_cell("Nombres"),
                rx.table.column_header_cell("Apellidos"),
                rx.table.column_header_cell("Correo"),
                rx.table.column_header_cell("Celular"),
                rx.table.column_header_cell("Acciones"),
            )
        ),
        rx.table.body(
            rx.foreach(lista_estudiantes, row_table)
        ),
    )

def row_table(estudiante: Estudiantes) -> rx.Component:
    return rx.table.row(
        rx.table.cell(estudiante.cedula),
        rx.table.cell(estudiante.nombres),
        rx.table.cell(estudiante.apellidos),
        rx.table.cell(estudiante.correo),
        rx.table.cell(estudiante.celular),
        rx.table.cell(
            rx.hstack(
                rx.button("Eliminar", on_click=lambda: EstudianteState.eliminar_estudiante(estudiante.id)),
            )
        ),
    )

def buscar_estudiante_cedula() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="Cedula", on_change=EstudianteState.buscar_onchange),
        rx.button("Buscar estudiante", on_click=EstudianteState.get_estudiante_cedula)
    )

def dialog_estudiante_form() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button("Crear estudiante", variant="outline"),
        ),
        rx.dialog.content(
            rx.flex(
                rx.dialog.title("Crear estudiante"),
                crear_estudiante_form(),
                justify="center",
                align="center",
                direction="column",
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button("Cancelar", variant="soft", color_scheme="red"),
                ),
                spacing="2",
                justify="end",
                margin_top="10px",
            ),
            style={"width": "400px"},
            ),
        )
    


# a utiliza los componentes de un formulario
def crear_estudiante_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.input(placeholder="Nombres", name="nombres"),
            rx.input(placeholder="Apellidos", name="apellidos"),
            rx.input(placeholder="Cedula", name="cedula"),
            rx.input(placeholder="Correo Electronico", name="correo"),
            rx.input(placeholder="# Celular", name="celular"),
            rx.input(placeholder="Direccion", name="direccion"),
            rx.input(placeholder="Telefono Casa", name="fono", style={"width": "100%"}, max_length=10),

            rx.dialog.close(
                rx.button("Crear Estuiante", type="submit"),
            ),
        ),

        on_submit=EstudianteState.crear_estudiante,
    )
