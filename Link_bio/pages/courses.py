import reflex as rx
import Link_bio.utils as utils
import Link_bio.views.constants as const
import Link_bio.styles.styles as styles
from Link_bio.routes import Route
from Link_bio.components.navbar import navbar
from Link_bio.components.footer import footer
from Link_bio.views.header.header import header
from Link_bio.views.links.courses_links import courses_links
from Link_bio.views.sponsors.sponsors import sponsors




@rx.page(
    route=Route.COURSES.value,
    title=utils.courses_title,
    description=utils.courses_description,
    image=utils.preview,
    meta=utils.courses_meta   
)

def courses() -> rx.Component:
    return  rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(details=False), 
                #rx.button("sdfasdfasdfasd "),
                courses_links(), 
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