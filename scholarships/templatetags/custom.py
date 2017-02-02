from django.templatetags.static import register


@register.filter(name='iterations')
def times(number):
    return range(1, number + 1)