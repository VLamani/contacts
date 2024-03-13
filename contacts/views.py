from django.shortcuts import render

# Create your views here.
# contacts/views.py
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
import csv

def contact_list(request):
    contacts = Contact.objects.all().order_by('name')
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

# Other view functions like add_contact, export_contacts_csv, import_contacts_csv, etc.

