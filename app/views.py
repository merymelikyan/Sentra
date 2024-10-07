from django.shortcuts import render

from .models import (
    MainBlock,
    HeaderText,
    FooterText, 
    Socials,
    FeaturedPlaces,
    FeaturedBlocks,
    Recent,
    ProjectsBlocks,
    Videos,
    Entries,
    EntriesBlogs1,
    EntriesBlogs2,
    EntriesBlogs3,
    EntriesBlogs4,
    Contact

)    
 
def index(request):
    context = {
          "main_block": MainBlock.objects.all(),
          "header_text": HeaderText.objects.all(),
          "footer_text": FooterText.objects.all().first(),
          "socials": Socials.objects.all(),
          "featured_places": FeaturedPlaces.objects.all().first(),
          "featured_blocks": FeaturedBlocks.objects.all(),
          "recent": Recent.objects.all().first(),
          "projects_blocks": ProjectsBlocks.objects.all(),
          "videos": Videos.objects.all().first(),
          "entries": Entries.objects.all().first(),
          "entries_blogs1": EntriesBlogs1.objects.all(),
          "entries_blogs2": EntriesBlogs2.objects.all(),
          "entries_blogs3": EntriesBlogs3.objects.all(),
          "entries_blogs4": EntriesBlogs4.objects.all(),
          "contact": Contact.objects.all().first()
      }      

    return render(request,"base.html" , context)