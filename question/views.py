from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question
from .serializer import QuestionSerizalizer
# Create your views here.

class QuestionApiVIew(APIView):
    
    def get(self, request, pk=None):
        print(pk)
        if pk:
            try:
                question = Question.objects.get(id=pk)
                ser = QuestionSerizalizer(question)
            except:
                return Response({
                    "message": "question not found"
                })
        else:
            question = Question.objects.all()
            ser = QuestionSerizalizer(question, many=True)
        return Response(ser.data)
    
    def post(self, request):
        data = QuestionSerizalizer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(data.errors)
        
    def put(self, request, pk=None):
        if pk:
            question = Question.objects.filter(id=pk).first()
            data = QuestionSerizalizer(data=request.data)
            if data.is_valid():
                data.save()
                return Response(
                    {
                        'message': 'question updated succesfully',
                        'data': data.data
                    }
                )
            else:
                return Response(data.errors)

        return Response(
            {
                'message': 'question not found'
            }
        )


    def delete(self, request, pk=None):
        try:
            question = Question.objects.get(id=pk)
            question.delete()
            msg = 'question deleted succesfully'
        except:
            msg = 'question not found'
        return Response(
            {
                'message': msg
            }
        )
