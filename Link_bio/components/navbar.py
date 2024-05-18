import reflex as rx
import Link_bio.views.constants as constants
import Link_bio.styles.styles as styles
from Link_bio.styles.styles import Size as Size
from Link_bio.styles.colors import Color as Color
from Link_bio.routes import Route
from Link_bio.components.ant_components import float_Button

def navbar() -> rx.Component:
    return  rx.hstack(
        rx.link(
            rx.box(
                rx.chakra.span("transforma", color=Color.PRIMARY.value),
                rx.chakra.span("Innova", color=Color.SECONDARY.value) ,
                style=styles.navbar_title_style
            ),
        href=Route.INDEX.value
        ),
        float_Button(
            icon= rx.image(src="/icons/whatsapp.svg"), 
            href= constants.MSGWATSAHPP
            ),
        position="sticky", # que no se mueva
        bg= Color.CONTENT.value,  # color fondo
        padding_x = Size.BIG.value, #esapacios hacia afuera 
        padding_y = Size.DEFAULT.value, 
        z_index="999", #para asegurarme qeu siempre estara en la parte superior
        top="0"
    ) 