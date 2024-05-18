import reflex as rx
from Link_bio.styles.colors import Color

class FloatButton(rx.Component):
    library = "antd"
    tag ="FloatButton"
    icon: rx.Var[rx.el.Img]
    href: rx.Var[str]
    target = "_blank"
    badge =  {"dot": True, "color": "green" }
 

float_Button = FloatButton.create

