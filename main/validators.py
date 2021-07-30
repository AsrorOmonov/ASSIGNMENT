from django.core.exceptions import ValidationError


def image_dimensions(image):
    if image.height != image.width:
        raise ValidationError('Image is not a square')
