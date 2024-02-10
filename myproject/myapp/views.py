from django.shortcuts import render
from myapp.forms import MyForm



def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process the form data as needed
            form.save()
    else:
        form = MyForm()

    return render(request, 'myapp/my_template.html', {'form': form})
