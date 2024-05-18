import reflex as rx

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

#Comun
preview="avatar.jpg"
_meta=[
    { "name":"og:type", "content":"website" },
    { "name":"og:image", "content":preview }
]

#Index
index_title="Luis Ponce de León | Especialista en Transformación Digital y Emprendedor Tecnológico"
index_description="Con más de 20 años de experiencia en informática, Luis Ponce de León es un experto en optimización de negocios a través de la tecnología. Fundador de Transforma Innova, una empresa dedicada a analizar empresas y crear planes tecnológicos personalizados, Luis ha ayudado a múltiples negocios a ser más eficientes y productivos. ¿Listo para transformar tu negocio? Contacta a Luis para llevar tu empresa al siguiente nivel."
index_meta=[
    { "name":"og:title", "content":index_title },
    { "name":"og:description", "content":index_description }
]
index_meta.extend(_meta)

#Cursos
courses_title="Luis Ponce de León "
courses_description="Con más de 20 años de experiencia en informática, Luis Ponce de León es un experto en optimización de negocios a través de la tecnología. Fundador de Transforma Innova, una empresa dedicada a analizar empresas y crear planes tecnológicos personalizados, Luis ha ayudado a múltiples negocios a ser más eficientes y productivos. ¿Listo para transformar tu negocio? Contacta a Luis para llevar tu empresa al siguiente nivel."
courses_meta=[
    { "name":"og:title", "content":courses_title },
    { "name":"og:description", "content":courses_description }
]
courses_meta.extend(_meta)





