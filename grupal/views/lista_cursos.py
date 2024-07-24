import reflex as rx
from grupal.modelos.cursos import ModeloCurso

def tarjeta_curso(curso: ModeloCurso) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.box(
                rx.center(
                    rx.text(
                        curso.nombre,
                        font_sixe="18px",
                        font_wight="bold",
                        margin_top="2",
                        ),
                        background_color="lightblue",
                        width="100%",
                        border_radius="10px",
                )
            ),
            rx.text(f"Responsable: { curso.responsable}", font_size="14px"),
            rx.text(f"Duracion: { curso.duracion}", font_size="14px"),
            rx.text(curso.descripcion, font_size="12px", margin_top="1"),
        ),
        padding="4",
        shadow="sm",
        border_radius="md",
    )


def  lista_cursos(cursos: list) -> rx.Component:
    return rx.hstack(
        *[ tarjeta_curso(curso) for curso in cursos ],
        spacing="4"
    )
