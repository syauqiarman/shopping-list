from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Syauqi Armanaya Syaki',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)