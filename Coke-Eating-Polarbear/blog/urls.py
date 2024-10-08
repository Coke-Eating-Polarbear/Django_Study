from django.urls import path
from . import views


urlpatterns = [
    # blog 앱 내부의 경로를 지정할 부분
    path('', views.main,name='main'), # 없는 경로를 호출하고 있음
    path('portfolio-details.html', views.portfolio_details, name='portfolio-details'), 
    path('service-details.html', views.service_details, name='service-details'), 
    path('traffic_recognize.html', views.traffic, name='traffic_recognize'), 
]