import reflex as rx
from  Link_bio.routes import Route
import Link_bio.views.constants as const
from Link_bio.components.link_button import link_button
from Link_bio.components.title import title


def index_links() -> rx.Component:
    return rx.vstack(
        title("Transforma Innova"), 
        link_button("TransformaInnova","Tu Puerta de Entrada a la Transformación Digital", "/icons/web.svg",  const.TRANSFORMAINNOVA),
        link_button("Portafolio Transforma Innova","Proyectos más recientes","/icons/news.svg",   const.PORTAFOLIO),
        link_button("Utilidades", "Herramientas para facilitar tu día a día","/icons/code.svg", Route.COURSES.value, is_external=False ),
       
        title("Sobre Mí"), 
        link_button("LinkedIn", "Conéctate para explorar mi trayectoria y red profesional.","/icons/linkedin.svg", const.LINKEDIN),
        link_button("Blog", "Explorando el Horizonte de la Tecnología y la Innovación","/icons/blog.svg",  const.BLOG),
     
        title("Contacto"), 
        link_button("Email", const.MAIL,"/icons/linkedin.svg", f"mailto:{const.MAIL}"),    
        width="100%", 
        spacing="2"
    )
    
    