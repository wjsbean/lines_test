from django.shortcuts import render


def standard(request):
    return render(request, 'summary/trait_standard.html', locals())