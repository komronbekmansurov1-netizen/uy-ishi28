from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Quiz
from .serializer import QuizSerizalizer
# Create your views here.

class QuizApiVIew(APIView):
    
    def get(self, request, pk=None):
        print(pk)
        if pk:
            try:
                quiz = Quiz.objects.get(id=pk)
                ser = QuizSerizalizer(quiz)
            except:
                return Response({
                    "message": "quiz not found"
                })
        else:
            quiz = Quiz.objects.all()
            ser = QuizSerizalizer(quiz, many=True)
        return Response(ser.data)
    
    def post(self, request):
        data = QuizSerizalizer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(data.errors)
        
    def put(self, request, pk=None):
        if pk:
            quiz = Quiz.objects.filter(id=pk).first()
            data = QuizSerizalizer(data=request.data)
            if data.is_valid():
                data.save()
                return Response(
                    {
                        'message': 'Quiz updated succesfully',
                        'data': data.data
                    }
                )
            else:
                return Response(data.errors)

        return Response(
            {
                'message': 'Quiz not found'
            }
        )


    def delete(self, request, pk=None):
        try:
            quiz = Quiz.objects.get(id=pk)
            quiz.delete()
            msg = 'quiz deleted succesfully'
        except:
            msg = 'quiz not found'
        return Response(
            {
                'message': msg
            }
        )
