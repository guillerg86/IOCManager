from django.urls import path
from threats_manager import views

urlpatterns = [
    path('', views.threats_manager_home, name='thmg_home'),
    path('ipaddr/blocked/', views.BlockedIPListView.as_view(), name='thmg_ipaddr_blocked_listview'),
    path('ipaddr/allowed/', views.AllowedIPListview.as_view(), name='thmg_ipaddr_allowed_listview'),
    path('ipaddr/allowed/view/<int:pk>', views.AllowedIPDetailView.as_view(), name='thmg_ipaddr_allowed_detailview'),


    path('ajax-new-allowedip', views.ajax_create_allowedip, name='thmg_ajax_new_allowedip'),
    path('ajax-get-last-allowedips', views.ajax_get_last_allowedips, name='thmg_ajax_get_last_allowedips'),
]