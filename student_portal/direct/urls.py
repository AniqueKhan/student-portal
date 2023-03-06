from django.urls import path
from direct.views import *

urlpatterns = [
    path('', inbox, name='inbox'),
    path("direct/<username>",direct,name='direct'),
    path("send_direct",send_direct,name='send_direct'),
    path('start/', people_we_can_message, name='people-we-can-message'),
    path('broadcast/', broadcast, name='broadcast'),
    path('search/', search, name='search'),
    path("new_conversation/<username>",new_conversation,name='new-conversation'),

]