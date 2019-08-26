from django import template

register = template.Library()

@register.simple_tag
def update_variable(value):
    """Permite actualizar la variable existente en la plantilla"""
    return value
