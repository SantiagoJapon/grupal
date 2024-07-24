import reflex as rx

# vamos acrear un componente reutilizable con un constructos y parametros
def link_icon(image: str, url=str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width="40px",
            height="auto",
        ),
        href = url,
        is_external=True
    )


