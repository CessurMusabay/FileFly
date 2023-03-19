from django.contrib import admin
from django.urls import path
from Transfer.views import upload, download, get_transfer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', upload),
    path('download/<int:id>/', download),
    path('transfer/<int:id>/', get_transfer)
]
