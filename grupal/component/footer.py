import reflex as rx
import datetime

def pie_de_pagina() -> rx.Component:
    return rx.vstack(
        rx.text(
            f"Todos los derechos reservados @ { datetime.datetime.now().year } / UIDE - app",
            font_size="14px",
            text_aling="center",
            padding="20px",
            width="100%",
            background_color="#f0f0f0",
        ),
        width="100%",
        border_radius="15px",
    )