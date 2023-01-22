from quoteApp.views import displayQuote
from django.urls import path
urlpatterns=[
    path('quote/',displayQuote),
]
