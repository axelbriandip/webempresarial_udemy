from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse # Funcionaría como el template tag 'url'
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data = request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            email = EmailMessage(
                'La caffetiera: Nuevo mensaje de contacto', # asunto
                'De {} <{}>\n\nEscribió:\n\n{}'.format(name, email, content), # mensaje
                'no-contestar@inbox.mailtrap.io', # email origen
                ['axelbriandip.rg@gmail.com'], # email destino (pueden ser más de uno)
                reply_to=[email] # reenviar al email del cliente
            )
            try:
                # Si todo fue bien, redireccionamos a OK..
                email.send()
                return redirect(reverse('contact')+'?ok')
            except:
                # Si hubo algún error, redireccionamos a FAIL..
                return redirect(reverse('contact')+'?fail')

    return render(request, 'contact/contact.html', {'form':contact_form})