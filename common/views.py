


def handler403(request, exception):
    return render(request, '403.html', locals())

def handler404(request, exception):
    return render(request, '404.html', locals())

def handler500(request, exception):
    return render(request, '500.html', locals())
