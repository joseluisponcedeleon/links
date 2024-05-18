import reflex as rx
from Link_bio.components.link_icon import link_icon
from Link_bio.components.info_text import info_text
from Link_bio.styles.styles import Size as Size
from Link_bio.styles.colors import TextColor as TextColor
from Link_bio.styles.colors import Color as Color
import Link_bio.views.constants as const


def header(details=True) -> rx.Component:
        return rx.vstack(
                  rx.hstack(
                     rx.avatar(name="Luis", 
                               size="6", 
                               src="/avatar.jpg", 
                               radius="full",
                               color = TextColor.BODY.value,
                               bg=Color.CONTENT.value,
                               padding="2px",
                               border=f"2px solid {Color.PRIMARY.value}"
                               ), 
                     rx.vstack(
                        rx.heading("LUIS PONCE DE LEON", size="5", color=TextColor.BODY.value) , 
                        rx.text("Msc Transformación Digital | Project Manager & Scrum Master", 
                                margin_top=Size.ZERO.value, 
                                color=TextColor.BODY.value),
                        rx.hstack(
                           link_icon("/icons/linkedin.svg", const.LINKEDIN, "LinkedIn"),
                           link_icon("/icons/github.svg", const.GIT, "Github"),
                           #link_icon("icons/linkedin.svg", "https://www.linkedin.com/in/jponcedeleon/", "LinkedIn")
                        ) ,align_items="star", width="100%"
                     ), 
                     align_items="star", 
                     width="100%",
                     spacing="4"
                  ),
                  rx.cond(
                        details,  
                        rx.vstack(
                  rx.flex(
                       info_text("+20", "Años de experiencia"),
                       rx.spacer(),
                       info_text("Experto", "en Gestión de Proyectos y Transformación Digital"),
                       rx.spacer(),
                       info_text("+50", "Proyectos implementados"),
                       width= "100%"        
                  ),
               rx.text("""Hola, soy Luis Ponce de León. Con más de veinte años de experiencia, lidero iniciativas de transformación digital que no solo implementan tecnología, sino que también promueven cambios significativos en la cultura y los procesos organizacionales. Mi enfoque se centra en la innovación y la mejora continua, colaborando con organizaciones de diversos sectores y regiones para lograr una integración efectiva y sostenible de nuevas soluciones.""",
                     font_size=Size.MEDIUM.value,
                     color=TextColor.BODY.value
                      ),
                      width="100%",spacing="4"
                  ), 
               ),      
               spacing="4",
               align_items="star"
  
        )

