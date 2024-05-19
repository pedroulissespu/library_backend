from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter

from library.authors.api.views import AuthorViewSet
from library.books.api.views import BookViewSet

router = DefaultRouter()

router.register("books", BookViewSet, basename="books")
router.register("authors", AuthorViewSet, basename="authors")

permissions_classes = [AllowAny]
app_name = "api-root"
urlpatterns = router.urls
