import reflex as rx
import Link_bio.styles.styles as styles
from Link_bio.styles.styles import Size as Size
from Link_bio.styles.colors import TextColor as TextColor
from Link_bio.styles.colors import Color as Color


def info_text(title: str, body:str) -> rx.Component:
    return rx.box(
        rx.chakra.span(
            title, 
            font_weight="bold", 
            color=Color.PRIMARY.value
        ),
        f" {body}", font_size=Size.MEDIUM.value, 
        color = TextColor.BODY.value
    )