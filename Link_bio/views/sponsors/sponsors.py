import reflex as rx
import Link_bio.views.constants as const
from Link_bio.components.title import title
from Link_bio.components.link_sponsor import link_sponsor
from Link_bio.styles.styles import Size, Spacing




def sponsors() -> rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.flex(
            link_sponsor(
                "/favicon.ico",
                const.LINKEDIN,
                "Logotipo de Elgato"
            ),
            link_sponsor(
                "/favicon.ico",
                const.LINKEDIN,
                "Logotipo de Microsoft MVP"
            ),
            link_sponsor(
                "/favicon.ico",
                const.LINKEDIN,
                "Logotipo de GitHub Star"
            ),
            spacing=Spacing.BIG.value,
            flex_direction=["column", "row"]
        ),
        width="100%",
        align_items="start",
        spacing=Spacing.DEFAULT.value
    )