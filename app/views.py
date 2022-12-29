from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html', {})

def ecommerce_report_page(request):
   return render(request, 'retail_report.html', {})


def marketing_report_page(request):
   return render(request, 'marketing_report.html', {})