import reflex as rx
import Link_bio.utils as utils
import Link_bio.views.constants as const
from Link_bio.components.navbar import navbar
from Link_bio.components.footer import footer
from Link_bio.views.header.header import header
from Link_bio.views.links.index_links import index_links
from Link_bio.views.sponsors.sponsors import sponsors
import Link_bio.styles.styles as styles

@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta   
)

def index() -> rx.Component:
    return  rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(), 
                #rx.button("sdfasdfasdfasd "),
                index_links(), 
                #sponsors(),
                max_width=styles.MAX_WIDTH, 
                width="100%", 
                margin_y=styles.Size.BIG.value,
                padding=styles.Size.BIG.value
            )
        ),
        rx.center(
        footer()
        )
    )

