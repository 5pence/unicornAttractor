from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('tickets/', include('tickets.urls')),
    path('users/', include('users.urls'))
]
