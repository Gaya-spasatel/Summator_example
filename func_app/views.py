from django.http import HttpResponse
import summary


# Create your views here.

def index(request, a, b):
    return HttpResponse(f"Сумма чисел {a}+{b} равна {summary.summary(a, b)}")
