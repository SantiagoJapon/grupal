import reflex as rx

from ..modelos.estudiantes import *
from ..servicios.user_servicio import *

class PageState(rx.State):
    username:str = ""
    password:str = ""
    error_message:str =""

    def handle_submit(self, form_data: dict):
        if servicio_autentificacion(form_data["username"], form_data["password"]):
            return rx.redirect("/estudiantes")
        else:
            self.error_message = "Usuario o contraseña incorrectos"

    def clear_error(self, _=None):
        self.error_message = ""


@rx.page(route="/login")
def login_page()-> rx.Component:
    return rx.container(
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("Iniciar Sesion", value="login"),
                rx.tabs.trigger("Registrarse", value="signup"),
            ),
            rx.tabs.content(
                rx.form(
                    rx.vstack(
                        form_fields("Nombre del usuario", "Ingrese su usuario", "text", "username"),
                        form_fields("Contrasenia", "Ingrese su contrasenia", "password", "password"),
                        rx.button("Iniciar Sesion", type="submit",color_scheme="blue"),
                        rx.cond(
                            PageState.error_message !="",
                            rx.text(PageState.error_message, color="red", font_size="14px")
                        ),
                        spacing="2",

                    ),
                    on_submit=PageState.handle_submit,
                ),
                value="login"
            ),
            rx.tabs.content(
                rx.form(
                    rx.vstack(
                        form_fields("Nombre del usuario", "Ingrese su usuario", "text", "username"),
                        form_fields("Contrasenia", "Ingrese su contrasenia", "password", "password"),
                        form_fields("Nombre", "Ingrese su nombre", "text", "name"),
                        form_fields("Correo", "Ingrese su correo", "email", "email"),
                        rx.button("Registrarse", type="submit", color_scheme="red"),
                        spacing="2",
                    )
                ),
                value="signup"
            ),
            
        ),
        background="gray.800",
        padding="20px",
        border_radius="20px",
        box_shadow="rgba(0,0,0,0.25) 0px 3px 8px",
        width="500px",
        margin="auto",
        margin_top="100px",
        border="10ox solid gray",
    )


def form_fields(label:str, palceholder: str, type:str, name:str) -> rx.Component:
    return rx.form.field(
        rx.form.label(label),
        rx.input(
            palceholder=palceholder,
            type = type,
            name = name,
            # on_focus= LoginState.clear_error
        ),
        align_items="flex-start",
        width="100%"
    )