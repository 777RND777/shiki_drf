from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def index(_):
    return Response("Main page")
