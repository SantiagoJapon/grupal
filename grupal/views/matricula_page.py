import reflex as rx
from grupal.modelos.estudiantes import Matricula
from ..servicios.matricula_servicio import *
from ..servicios.estudiante_servicio import servicio_consultar_cedula
from .estudiante_page import EstudianteState

class MatriculaState(rx.State):
    matriculas : list[Matricula]
    buscar_codigo : str = ""

    @rx.background
    async def get_todos_matriculas(self):
        async with self:
            self.matriculas = servicio_matricula_all()

    @rx.background
    async def get_matricula_codigo(self):
        async with self:
            self.matriculas = servicio_consultar_codigo(self.buscar_codigo)
    
    def buscar_onchange(self, value:str):
        self.buscar_codigo = value

    # crear el metodo para guardar un registro en la bd
    @rx.background
    async def crear_matricula(self, data:dict):
        async with self:
            try:
                estudiante = self.servicio_consultar_cedula(data.get('cedula'))
                if not estudiante:
                    raise ValueError("El estudiante no existe")
                self.matriculas = servicio_crear_matricula(data)
            except Exception as e:
                print(e)
    
    @rx.background
    async def eliminar_matricula(self, id: int):
        async with self: 
            try:
                servicio_eliminar_matricula(id)
                await self.get_todos_matriculas()
            except Exception as e:
                print(e)


# pagina que muestre el listado de estudiantes que estan en la base de datos.
@rx.page(route="/matriculas", title="Lista de Matriculas", on_load=MatriculaState.get_todos_matriculas)
def estudiante_page() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.heading("Matriculas", title="Matriculas", size="5", center=True, style={"align": "center"}),
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
            buscar_matricula_codigo(),
            dialog_matricula_form(),
            
            justify="center",
            style={"margin": "20px", 'width': "100%"},
        ),
        tabla_matriculas(MatriculaState.matriculas),
        
        direction="column",
        justify="center",
        style={"margin": "auto", 'width': "80%"},
    )

# crear el componen de tabla para lista de estudiantes
def tabla_matriculas(lista_matriculas: list[Matricula]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("ID"),
                rx.table.column_header_cell("Codigo"),
                rx.table.column_header_cell("Fecha de Matricula"),
                rx.table.column_header_cell("Estado"),
                rx.table.column_header_cell("Pago de matricula"),
                rx.table.column_header_cell("Fecha de pago"),
                rx.table.column_header_cell("Estudiante"),
                rx.table.column_header_cell("Acciones"),
            )
        ),
        rx.table.body(
            rx.foreach(lista_matriculas, row_table)
        ),
    )

def row_table(matricula: Matricula) -> rx.Component:
    return rx.table.row(
        rx.table.cell(matricula.id),
        rx.table.cell(matricula.codigo),
        rx.table.cell(matricula.fechaMatricula),
        rx.table.cell(matricula.estado),
        rx.table.cell(matricula.pagoMatricula),
        rx.table.cell(matricula.fechaPago),
        rx.table.cell( f"{matricula.estudiante.nombres} {matricula.estudiante.apellidos}" ),
        rx.table.cell(
            rx.hstack(
                rx.button("Eliminar", on_click=lambda: MatriculaState.eliminar_matricula(matricula.id)),
            )
        ),
    )

def buscar_matricula_codigo() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="codigo", on_change=MatriculaState.buscar_onchange),
        rx.button("Buscar Matricula", on_click=MatriculaState.get_matricula_codigo)
    )

def dialog_matricula_form() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button("Crear Matricula", variant="outline"),
        ),
        rx.dialog.content(
            rx.flex(
                rx.dialog.title("Crear matricula"),
                crear_matricula_form(),
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
def crear_matricula_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.input(placeholder="Codigo", name="codigo", style={"width": "100px"}, max_length=5 ),
            rx.input(placeholder="Fecha de matricula", name="fechaMatricula", type="date"),
            rx.input(['Registrado','Pagado','Matriculado','Cancelado','Borrado'],placeholder="Estado de la matricula", name="estado", max_length=11),
            rx.input(placeholder="valor de pago", name="pagoMatricula", type="number"),
            rx.input(placeholder="Fecha de pago", name="fechaPago", type="date"),
  
            rx.dialog.close(
                rx.button("Crear Matricula", type="submit"),
            ),
        ),

        on_submit=MatriculaState.crear_matricula,
    )
