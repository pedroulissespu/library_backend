from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.urls import NoReverseMatch, get_resolver, get_script_prefix


class APIRootView(APIView):

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        api_urls = {}
        namespace = None
        prefix = get_script_prefix()
        resolver = get_resolver()

        for urlpattern in resolver.url_patterns:
            try:
                url_name = urlpattern.name
                if url_name:
                    api_urls[url_name] = request.build_absolute_uri(reverse(url_name))
            except NoReverseMatch:
                continue

        return Response(api_urls)
