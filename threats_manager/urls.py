from django.urls import path
from threats_manager import views

urlpatterns = [
    path('', views.threats_manager_home, name='thmg_home'),
    path('ajax-new-allowedip', views.ajax_create_allowedip, name='thmg_ajax_new_allowedip'),
    path('ajax-get-last-allowedips', views.ajax_get_last_allowedips, name='thmg_ajax_get_last_allowedips'),
]