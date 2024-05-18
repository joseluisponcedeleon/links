import reflex as rx
import datetime
from Link_bio.styles.styles import Size as Size
from Link_bio.styles.colors import TextColor as TextColor
import Link_bio.views.constants as const

def footer() -> rx.Component:
    return rx.vstack(
       # rx.image(src= "favicon.ico", height=Size.BIG.Value, weight=Size.BIG.Value),
        rx.link(
            #f"2024-{datetime.date.today().year} Mi sitio Web", 
            "👨‍💻 Desarrollado por Luis Ponce de León utilizando Python y Reflex.", 
            href=const.TRANSFORMAINNOVA, 
            is_external= True, 
            font_size= Size.MEDIUM.value
        ),
        rx.text ("+598 91 476 004 - Montevideo - Uruguay", 
                 font_size= Size.MEDIUM.value, 
                 margin_top=Size.ZERO.value), 
        margin_bottom=Size.BIG.value, 
        padding_bottom=Size.BIG.value, 
        padding_x="1",
        spacing="0",
        color= TextColor.FOOTER.value
    )