from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User1
from .serializer import User1Serizalizer
# Create your views here.

class User1ApiVIew(APIView):
    
    def get(self, request, pk=None):
        print(pk)
        if pk:
            try:
                users = User1.objects.get(id=pk)
                ser = User1Serizalizer(users)
            except:
                return Response({
                    "message": "users not found"
                })
        else:
            results = User1.objects.all()
            ser = User1Serizalizer(results, many=True)
        return Response(ser.data)
    
    def post(self, request):
        data = User1Serizalizer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(data.errors)
        
    def put(self, request, pk=None):
        if pk:
            result = User1.objects.filter(id=pk).first()
            data = User1Serizalizer(data=request.data)
            if data.is_valid():
                data.save()
                return Response(
                    {
                        'message': 'Users updated succesfully',
                        'data': data.data
                    }
                )
            else:
                return Response(data.errors)

        return Response(
            {
                'message': 'Users not found'
            }
        )


    def delete(self, request, pk=None):
        try:
            result = User1.objects.get(id=pk)
            result.delete()
            msg = 'users deleted succesfully'
        except:
            msg = 'users not found'
        return Response(
            {
                'message': msg
            }
        )
