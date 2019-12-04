import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View

from as_api.mixins import JsonResponseMixin
from .models import Update

# def detail_view(request):
# return render()  # return JSON data
# return HttpResponse(get_template().render({}))


def json_example_view(request):
    data = {"count": 100, "content": "Some new content"}
    json_data = json.dumps(data)
    # return JsonResponse(data)
    return HttpResponse(json_data, content_type="application/json")


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {"count": 100, "content": "Some new content"}
        return JsonResponse(data)


class JsonCBV2(View, JsonResponseMixin):
    def get(self, request, *args, **kwargs):
        data = {"count": 100, "content": "Some new content"}
        return self.render_to_json_response(data)
