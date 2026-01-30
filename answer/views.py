from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Answer
from .serializer import AnswerSerizalizer
# Create your views here.

class AnswerApiVIew(APIView):
    
    def get(self, request, pk=None):
        print(pk)
        if pk:
            try:
                answer = Answer.objects.get(id=pk)
                ser = AnswerSerizalizer(answer)
            except:
                return Response({
                    "message": "answer not found"
                })
        else:
            answer = Answer.objects.all()
            ser = AnswerSerizalizer(answer, many=True)
        return Response(ser.data)
    
    def post(self, request):
        data = AnswerSerizalizer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(data.errors)
        
    def put(self, request, pk=None):
        if pk:
            answer = Answer.objects.filter(id=pk).first()
            data = AnswerSerizalizer(data=request.data)
            if data.is_valid():
                data.save()
                return Response(
                    {
                        'message': 'answer updated succesfully',
                        'data': data.data
                    }
                )
            else:
                return Response(data.errors)

        return Response(
            {
                'message': 'answer not found'
            }
        )


    def delete(self, request, pk=None):
        try:
            answer = Answer.objects.get(id=pk)
            answer.delete()
            msg = 'answer deleted succesfully'
        except:
            msg = 'answer not found'
        return Response(
            {
                'message': msg
            }
        )
