import reflex as rx
from grupal.styles.colors import Color
from grupal.component.link_icon import link_icon

def navbar()-> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src = "favicon.ico",
                alt="Imagen del portafolio personal",
                width=100,
                height=100,
                border_radius="15px 50px",
                border="5px solid #555"
            ),
            rx.text(
                "Portafolio Profesional 2024",
                font_size="2em",
                padding_y="0.75em",
                padding_x="0.2em",
            ),
            rx.spacer(),
            link_icon(
                "iconos/inicio.png",
                "https://miltonpalacios.es",
            ),
            link_icon(
                "iconos/youtube.png",
                "https://youtube.com",
            ),
            link_icon(
                "iconos/youtube.png",
                "https://x.com",
            ),
            rx.menu.root(
                rx.menu.trigger(
                    rx.button("Menu"),
                ),
                rx.menu.content(
                    rx.menu.item("Home"),
                    rx.menu.separator(),
                    rx.menu.item("Trabajos Realizados"),
                    rx.menu.item("Contacto"),
                ),
                
            ),
        ),
        background_color=Color.BACKGROUND.value,
        position="sticky",
        border_botton=f"0.25em solid {Color.SECONDARY.value}",
        padding="10px",
        z_index="999",
        top="0",
        width="100%",
    ) 


