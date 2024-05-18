import reflex as rx
from  Link_bio.routes import Route
import Link_bio.views.constants as const
from Link_bio.components.link_button import link_button
from Link_bio.components.title import title


def courses_links() -> rx.Component:
    return rx.vstack(
        title("Utilidades"), 
        link_button("Unir PDFs", 
                    "Cargue múltiples PDFs para fusionarlos en un único archivo",
                    "/icons/code.svg", 
                    const.UNIR_PDF
        ),
           link_button("Sacar Fondo de imagen", 
                    "Sube una imagen para eliminar su fondo",
                    "/icons/code.svg", 
                    const.SACAR_FONDO
        ),
           link_button("Generador de código QR", 
                    "Escriba una URL para generar el QR",
                    "/icons/code.svg", 
                    const.GENERADOR_QR
        ),
        
        width="100%", 
        spacing="2"
    )
    
    