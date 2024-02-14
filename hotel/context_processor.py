from typing import Any

from .models import HotelContactInfo, HotelShortIntro, BannerImage

from django.db.models import ImageField


def hotel_information(request) -> dict[str, Any]:
    hotel_contact_info = HotelContactInfo.objects.first()
    hotel_intro = HotelShortIntro.objects.first()
    banner_image_instance = BannerImage.objects.first()
    if banner_image_instance:
        images = [getattr(banner_image_instance, field.name) for field in BannerImage._meta.fields if
                  isinstance(field, ImageField)]
    else:
        images = None

    # context['description'] = getattr(banner_image_instance, "description")
    description = getattr(banner_image_instance, "description")
    data = {
        "hotel_contact_info": hotel_contact_info,
        'hotel_intro': hotel_intro,
        'banner_images': images,
        'description': description,
    }
    return data
