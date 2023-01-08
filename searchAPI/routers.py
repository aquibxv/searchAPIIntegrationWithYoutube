from rest_framework import routers
from searchAPI.views import YouTubeGetStoredVideosViewSet, SearchYoutubeVideosAPIViewSet

router = routers.DefaultRouter()
router.register('getStoredVediosData', YouTubeGetStoredVideosViewSet, basename='GetStoredVideos')
router.register('searchStoredVediosData', SearchYoutubeVideosAPIViewSet, basename='SearchStoredVideos')
urlpatterns = router.urls