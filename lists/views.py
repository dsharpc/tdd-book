from django.shortcuts import render

# Create your iews here.
def home_page(request):
    return render(request, 'home.html')