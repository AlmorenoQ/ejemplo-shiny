from shiny import reactive, render
from shiny.express import input, ui

CHOICES = {
    "frutas": ["manzana", "pera", "platano", "naranja"],
    "verduras": ["zanahoria", "lechuga", "tomate", "pepino"],
    "lacteos": ["leche", "queso", "yogurt", "mantequilla"]
}

# Interfaz de usuario
ui.input_select("categoria","Elige una categoría:", choices=list(CHOICES.keys()))
ui.input_select("producto","Elige un producto:", choices=CHOICES["frutas"])

# Actualización del segundo select
@reactive.effect
def _():
    choice = input.categoria()
    ui.update_selectize("producto", choices=CHOICES[choice])

# Mostrar el resultado
@render.text
def _resultado():
    return f"Categoría: {input.categoria()} - Producto: {input.producto()}"