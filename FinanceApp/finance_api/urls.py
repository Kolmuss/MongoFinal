from .views import *
from django.urls import path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Financial API')
app_name = 'api'
urlpatterns = [
    path('currencies/', CurrencyRecordView.as_view(), name='currencies'),
    path('categories/', CategoryRecordView.as_view(), name='categories'),
    path('accounts/', AccountRecordView.as_view(), name='accounts'),
    path('transactions/', TransactionRecordView.as_view(), name='transactions'),
    path('profiles/', ProfileRecordView.as_view(), name='profiles'),
    path('api-docs/', schema_view),

]
