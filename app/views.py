from django.shortcuts import render

from .models import (
    HeaderText,
    FooterText, 
    Socials

)    
 
def index(request):
    context = {
          "header_text": HeaderText.objects.all(),
          "footer_text": FooterText.objects.all().first(),
          "socials": Socials.objects.all()
          
      }      

    return render(request,"base.html" , context)