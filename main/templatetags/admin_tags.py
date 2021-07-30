from django.template import Library

register = Library()


@register.filter  # using filters, we can use only one arg "{{ }}"
def cut(text: str, n: int) -> str:
    return text[:n]


@register.simple_tag # using simple_tag, we can take multiple args {%  %}
def cut_string(text, n):
    return text[:n]


