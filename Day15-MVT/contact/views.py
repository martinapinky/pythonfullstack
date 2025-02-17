from django.shortcuts import render
from .forms import ContactForm
from .models import Contact

# Create your views here.

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  # Create a form instance with POST data
        if form.is_valid():
            # Process the data, for now, let's just print it
            print(form.cleaned_data)  # Print the data (you can save it to the database or send an email)
            form.save()
            # Redirect to a success page or display a success message
            return render(request, 'contact_success.html')  # You can create a success template
 
    else:
        form = ContactForm()  # Create an empty form when the page is first loaded
 
    return render(request, 'contact.html', {'form': form})  # Render the form on the contact page