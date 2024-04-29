from django.shortcuts import render,redirect

from .forms import SignupForm


from datetime import datetime

def index(request):
    return render(request, 'core/index.html')




def my_view(request):
    current_year = datetime.now().year
    context = {'current_year': current_year}
    return render(request, 'base.html', context)
    



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()    
        
    
    return render(request, 'core/signup.html',{
        'form': form
    })
    
