from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class AllIncomeView(APIView):

    def get(self, request, *args, **kwargs):
        return Response("this all income view")

class AllOutcomeView(APIView):

    def get(self, request, *args, **kwargs):
        return Response("All Outcome view")