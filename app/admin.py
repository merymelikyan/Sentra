from django.contrib import admin


from .models import (
    HeaderText,
    FooterText,
    
    Socials
) 
 
admin.site.register(HeaderText)
admin.site.register(FooterText)
admin.site.register(Socials)