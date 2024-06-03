from django.urls import path
from .views import login_view, home_view, upload_view, download_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('upload/', upload_view, name='upload'),
    path('download/', download_view, name='download'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)