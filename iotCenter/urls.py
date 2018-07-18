from django.conf.urls import url
from . import views

app_name = 'iotCenter'
urlpatterns = [
    url(r'^test$', views.test, name='test'),
    url(r'^test2$', views.test2, name='test2'),
    url(r'^neonlights$', views.neonlights, {'page': 'neonlights'}),
    url(r'^neonlights/shakeOn$', views.neonShakeOn, {'page': 'neonShakeOn'}),
    url(r'^neonlights/shakeOff$', views.neonShakeOff, {'page': 'neonShakeOff'}),
    url(r'^neonlights/swipeleftOn$', views.neonSwipeLeftOn, {'page': 'neonSwipeLeftOn'}),
    url(r'^neonlights/swipeleftOff$', views.neonSwipeLeftOff, {'page': 'neonSwipeLeftOff'}),
    url(r'^neonlights/swiperightOn$', views.neonSwipeRightOn, {'page': 'neonSwipeRightOn'}),
    url(r'^neonlights/swiperightOff$', views.neonSwipeRightOff, {'page': 'neonSwipeRightOff'}),
]
