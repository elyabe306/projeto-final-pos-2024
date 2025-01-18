from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers

from api import views

router = routers.DefaultRouter()

router.register(r'users', views.UsersViewSet)

router.register(r'posts', views.PostsViewSet)
posts_router = routers.NestedDefaultRouter(router, r"posts", lookup="posts")
posts_router.register(r"comments", views.CommentsViewSet)

router.register(r'comments', views.CommentsViewSet)
router.register(r'albums', views.AlbumsViewSet)
router.register(r'photos', views.PhotosViewSet)
router.register(r'todos', views.TodosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
]

urlpatterns += router.urls

urlpatterns = router.urls + posts_router.urls