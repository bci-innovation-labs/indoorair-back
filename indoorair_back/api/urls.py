"""
api/urls.py
"""
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views


urlpatterns = [
    #---------------------------#
    # UNPROTECTED API ENDPOINTS #
    # --------------------------#

    # HOMEPAGE
    path('api/version', views.VersionAPI.as_view(), name='version_api'),

    # GATEWAY
    path('api/register', views.RegisterAPI.as_view(), name='register_api'),
    path('api/login', obtain_auth_token, name='api_token_auth'),
    path('api/logout', views.post_logout_api, name='logout_api'),

    #-------------------------#
    # PROTECTED API ENDPOINTS #
    #-------------------------#

    # DASHBOARD
    path('api/dashboard', views.DashboardAPI.as_view(), name='dashboard_api'),

    # INSTRUMENTS
    path('api/instruments', views.InstrumentListAPI.as_view(), name='instruments_list_api'),
    path('api/instrument/<int:id>', views.InstrumentRetrieveAPI.as_view(), name='instruments_retrieve_api'),
    path('api/instrument/<int:id>/update', views.InstrumentUpdateAPI.as_view(), name='instruments_update_api'),

    # REPORTS
    path('api/report/1', views.DownloadCSVReport01API.as_view(), name="download_csv_report_01_temperature_sensor_api")

]
