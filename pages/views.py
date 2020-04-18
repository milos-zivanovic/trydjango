from django.shortcuts import render


def home(request, *args, **kwargs):
    context = {
        'text': 'This is a homepage',
        'number': 123,
        'list': [1, 33, 42, 6, 90]
    }
    return render(request, 'home.html', context)


def contact(request, *args, **kwargs):
    return render(request, 'contact.html')


def about(request, *args, **kwargs):
    return render(request, 'about.html')
