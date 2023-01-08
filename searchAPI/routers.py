from rest_framework import routers
from searchAPI.views import YouTubeGetStoredVideosViewSet

router = routers.DefaultRouter()
router.register('getStoredVediosData', YouTubeGetStoredVideosViewSet, basename='StoredVideosSearch')
urlpatterns = router.urls