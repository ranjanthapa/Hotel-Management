from typing import Any

from .models import HotelContactInfo, HotelShortIntro


def hotel_information(request) -> dict[str, Any]:
    hotel_contact_info = HotelContactInfo.objects.first()
    hotel_intro = HotelShortIntro.objects.first()
    data = {
        "hotel_contact_info": hotel_contact_info,
        'hotel_intro': hotel_intro
    }
    return data
