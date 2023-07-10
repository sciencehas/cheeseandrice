```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('list/', views.list_documents, name='list_documents'),
    path('detail/<int:doc_id>/', views.detail, name='detail'),
    path('edit/<int:doc_id>/', views.edit, name='edit'),
]
```