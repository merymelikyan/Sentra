from django.contrib import admin


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
 
admin.site.register(MainBlock) 
admin.site.register(HeaderText)
admin.site.register(FooterText)
admin.site.register(Socials)
admin.site.register(FeaturedPlaces)
admin.site.register(FeaturedBlocks)
admin.site.register(Recent)
admin.site.register(ProjectsBlocks)
admin.site.register(Videos)
admin.site.register(Entries)
admin.site.register(EntriesBlogs1)
admin.site.register(EntriesBlogs2)
admin.site.register(EntriesBlogs3)
admin.site.register(EntriesBlogs4)
admin.site.register(Contact)