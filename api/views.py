from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    data = {'slackUsername': 'Muhammad Ademola', 'backend': True, 'age': 20, 'bio': 'A student at University of Lagos'}
    return Response(data)