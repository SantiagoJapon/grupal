import reflex as rx
from grupal.modelos.asignaturas import Asignatura
from ..servicios.asignatura_servicio import servicio_listar_asignaturas

class AsignaturaPeriodoState(rx.State):
    asignaturas: list[Asignatura] = []

    @rx.background
    async def get_asignaturas(self):
        async with self:
            self.asignaturas = servicio_listar_asignaturas()

@rx.page(route="/asignatura_periodo", title="Asignatura Periodo", on_load=AsignaturaPeriodoState.get_asignaturas)
def asig_periodo_page() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.heading("Administración de Asignaturas", size="5", center=True, style={"align": "center"}),
            rx.input(placeholder="Buscar Asignatura", style={"margin": "10px"}),
            rx.button("Agregar Asignatura", variant="outline", style={"margin": "10px"}),
            background_color="var(--plum-2)",
            border_radius="10px",
            width="100%",
            margin="16px",
            padding="16px",
            justify="center",
            align="center",
        ),
        rx.hstack(
            *[rx.card(
                rx.vstack(
                    rx.image(src=asignatura.imagen_url, alt=f"Imagen de {asignatura.nombre}", width="100%"),
                    rx.text(asignatura.nombre, font_size="18px", font_weight="bold", margin_top="2"),
                    rx.text(f"Fecha de Inicio: {asignatura.fecha_inicio}", font_size="14px"),
                    rx.text(f"Paralelo: {asignatura.paralelo}", font_size="14px"),
                ),
                padding="4",
                shadow="sm",
                border_radius="md",
            ) for asignatura in AsignaturaPeriodoState.asignaturas],
            spacing="4",
            wrap="wrap",
            justify="center",
        ),
        direction="column",
        justify="center",
        style={"margin": "auto", 'width': "80%"},
    )
