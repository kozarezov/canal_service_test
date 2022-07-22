from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('datas.urls', namespace='datas')),
]

""" handler404 = 'views.page_not_found'
handler500 = 'views.internal_server_error'
handler403 = 'views.permission_denied' """
