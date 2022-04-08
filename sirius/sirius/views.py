from django.shortcuts import render, redirect

def landing(request):
    if request.user:
        return redirect('user:dashboard', u_pk=request.user.pk)
    return render(request, 'landing.html', {})