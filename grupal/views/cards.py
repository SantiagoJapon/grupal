import reflex as rx

def trabajos_card(titulo: str, descripcion: str, imagen_url:str) -> rx.Component:
    return rx.card(
        rx.hstack(
            rx.image(
                src=imagen_url,
                alt= f"Imagen de {titulo}",
                width="120px",
                height="auto",
            ),
            rx.vstack(
                rx.text(titulo, font_size="18px", font_weigth="bold", margin_top="2"),
                rx.text(titulo, font_size="14px", margin_top="1"),
            ),
        ),
        padding="4",
        shadow="sm",
        border_radius="md",
    )

def  lista_proyecto(trabajos: list) -> rx.Component:
    return rx.hstack(
        *[
            trabajos_card(trabajo['titulo'], trabajo['descripcion'], trabajo['imagen_url'])
            for trabajo in trabajos
        ],
        spacing="4"
    )