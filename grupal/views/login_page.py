import reflex as rx

from ..modelos.estudiantes import *
from ..servicios.user_service import *
from ..servicios.estudiante_servicio import *

class PageState(rx.State):
    uswrname: str = ""
    password: str = ""
    error_message: str = ""

    def handle_submit(self, form_data: dict):
        if servicio_autentificacion(form_data["username"], form_data["password"]):
            return rx.redirect("/estudiantes")
        else:
            self.error_message = "Credenciales incorrectas"

    def clear_error(self, _=None):
        self.error_message = ""
    
    @rx.background
    async def registrar_cuenta(self, form_data: dict):
        async with self:
            try:
                # Primero, verificar si el estudiante ya existe
                estudiante_existente = servicio_consultar_cedula(form_data["cedula"])
                if estudiante_existente:
                    self.error_message = "El estudiante ya existe en el sistema"
                    return
                
                # Crear el estudiante
                resultado_estudiante = servicio_crear_estudiante(
                    nombres=form_data["nombres"],
                    apellidos=form_data["apellidos"],
                    cedula=form_data["cedula"],
                    correo=form_data["correo"],
                    celular=form_data["celular"],
                    direccion=form_data["direccion"],
                    fono=form_data["fono"]
                )
                
                if isinstance(resultado_estudiante, str):
                    self.error_message = resultado_estudiante
                    return
                
                # Obtener el estudiante recién creado
                estudiante = servicio_consultar_cedula(form_data["cedula"])
                if estudiante and len(estudiante) > 0:
                    estudiante = estudiante[0]  # Tomar el primer estudiante de la lista
                    
                    # Crear el usuario
                    resultado_usuario = servicio_crear_user(
                        username=form_data["username"],
                        password=form_data["password"],
                        estudiante_id=estudiante.id
                    )
                    if resultado_usuario == "El usuario se ha creado exitosamente":
                        return rx.redirect("/login")
                    else:
                        self.error_message = resultado_usuario
                else:
                    self.error_message = "Error al crear el estudiante"
            except Exception as e:
                self.error_message = f"Error: {str(e)}"

@rx.page(route="/login")
def login_page() -> rx.Component:
    return rx.container(
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("Iniciar Sesion", value="login"),
                rx.tabs.trigger("Registrarse", value="signup"),
            ),
            rx.tabs.content(
                rx.form(
                    rx.vstack(
                        form_fields("Nombre de usuario","Ingrese su usuario","text","username"),
                        form_fields("Contraseña","Ingrese su contraseña","password","password"),
                        rx.button("Iniciar Sesion", type="submit", color_scheme="blue"),
                        # condicional
                        rx.cond(
                            PageState.error_message != "",
                            rx.text(PageState.error_message, color="red", font_size="14px"),
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
                        form_fields("Email","Ingrese su email","text","correo"),
                        form_fields("Nombre de usuario","Ingrese el usuario","text","username"),
                        form_fields("Ingrese el password","Ingrese el password","password","password"),
                        form_fields("Nombres", "Ingrese sus nombres", "text", "nombres"),
                        form_fields("Apellidos", "Ingrese sus apellidos", "text", "apellidos"),
                        form_fields("Cédula", "Ingrese su número de cédula", "text", "cedula"),
                        form_fields("Celular", "Ingrese su número de celular", "tel", "celular"),
                        form_fields("Dirección", "Ingrese su dirección", "text", "direccion"),
                        form_fields("Teléfono fijo", "Ingrese su teléfono fijo", "tel", "fono"),
                        rx.button("Registrarse", type="submit", color_scheme="blue"),
                        spacing="2",
                    ),
                    on_submit=PageState.registrar_cuenta,
                ),
                value="signup"
            ),
            background="gray.800",
            padding="20px",
            border_radius="20px",
            box_shadow="rgba(0,0,0,0.25) 0px 3px 8px",
            width="500px",
            margin="auto",
            margin_top="100px",
            border="2px solid gray",
           
        )
    )

def form_fields(label: str, placeholder: str, type: str, name:str) -> rx.Component:
    return rx.form.field(
        rx.form.label(label),
        rx.input(
            placeholder=placeholder,
            type = type,
            name = name,
            #on_focus = LoginState.clear_error,
            ),
            align_items="flex-start",
            width="100%",
    )