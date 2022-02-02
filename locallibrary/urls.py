
from nturl2path import url2pathname
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static
# Импорт для статических файлов
# Только на период разработки

urlpatterns = [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
