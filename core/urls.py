from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('hotel.urls')),
                  path('account/', include('account.urls')),
                  path('room/', include('room.urls')),
                  path('payment/', include('payment.urls')),
                  path('events/', include('event.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
