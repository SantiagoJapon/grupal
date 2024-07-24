import reflex as rx

def header() -> rx.Component:
    return rx.grid(
        rx.center(
            rx.box(
                rx.heading("Portafolio Profesional 2024", size="4"),
                rx.heading("Desarrollador Python", size="3"),
                rx.button("Descargar CV", size="2", variant="outline", margin_top="3rem"),
            )
        ),
        rx.center(  
            rx.image(
                src="iconos/inicio.png",
                alt="Imagen del portAFOLIO",
                width="200px",
                height="auto",
                )
        ),
        columns="2",
        spacing="2",
        width="100%",
    )