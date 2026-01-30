from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Result
from .serializer import ResultSerizalizer
# Create your views here.

class ResultApiVIew(APIView):
    
    def get(self, request, pk=None):
        print(pk)
        if pk:
            try:
                result = Result.objects.get(id=pk)
                ser = ResultSerizalizer(result)
            except:
                return Response({
                    "message": "result not found"
                })
        else:
            results = Result.objects.all()
            ser = ResultSerizalizer(results, many=True)
        return Response(ser.data)
    
    def post(self, request):
        data = ResultSerizalizer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(data.errors)
        
    def put(self, request, pk=None):
        if pk:
            result = Result.objects.filter(id=pk).first()
            data = ResultSerizalizer(data=request.data)
            if data.is_valid():
                data.save()
                return Response(
                    {
                        'message': 'Result updated succesfully',
                        'data': data.data
                    }
                )
            else:
                return Response(data.errors)

        return Response(
            {
                'message': 'Result not found'
            }
        )


    def delete(self, request, pk=None):
        try:
            result = Result.objects.get(id=pk)
            result.delete()
            msg = 'result deleted succesfully'
        except:
            msg = 'result not found'
        return Response(
            {
                'message': msg
            }
        )
