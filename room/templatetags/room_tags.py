from django import template
from django.conf import settings

register = template.Library()

@register.filter(name='get_room_images')
def get_room_images(room_image):
    """Retrieve image URLs from a RoomImage instance."""
    images = [getattr(room_image, f'image{i}') for i in range(1, 6)]
    return [img.url for img in images if img]
