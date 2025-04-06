from django.shortcuts import render

# Create your views here.
def index_view(request):

        data = {
                "name":"Amin",
                "surename":"Delvarani",
                "description":"Software Architect",
                "age":42,
        }

        return render(request,'cv/index.html',data)