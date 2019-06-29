from django.contrib import admin
from django.urls import path, include
import blogA.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogA.views.home, name="home"),
    path('blog/', include('blogA.urls')),\
    path('accounts/', include('accounts.urls')),
]
