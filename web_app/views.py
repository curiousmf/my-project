from django.shortcuts import render
from web_app.models import Medicines

# Create your views here.
def show_start_page(request):
    context = {'medicines' : Medicines.objects.all()
    }
    return render(request,
                  'index.html',
                  context=context)

def show_medicine(request, medicine_id):
    context = {'medicine':Medicines.objects.get(pk = medicine_id)}
    return render(request,
                  'medicine.html',
                  context=context)