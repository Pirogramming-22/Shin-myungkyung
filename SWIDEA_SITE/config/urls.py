from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # 관리자 URL
    path('', include('apps.idea.urls')),  # 기본 루트 URL -> apps.idea.urls
    path('tool/', include('apps.tool.urls')),  # tool 앱의 URL을 명확히 구분
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)