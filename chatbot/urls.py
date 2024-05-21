from django.urls import path
from .views import chatbot, chat_view
from chatbot.views import chatbot
urlpatterns = [
    path('chat/', chatbot, name='chatbot'),
    path('', chat_view, name='chat_view'),
]
