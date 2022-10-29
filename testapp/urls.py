from django.urls import path
from . import views

app_name    = "testapp"
urlpatterns = [ 
    path('', views.index, name="index"),
    path('upload_ajax', views.index_ajax, name="index_ajax"),
    path('upload_ajax/<int:pk>/', views.index_ajax, name="single_ajax"), # 削除ボタン
    path('editorjs_plugin', views.editorjs_plugin, name="editorjs_plugin"),
]
