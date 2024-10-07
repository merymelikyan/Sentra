from django.db import models


class MainBlock(models.Model):
    link = models.CharField(max_length=55, blank=True, null=True)
    link_name = models.CharField(max_length=55, blank=True, null=True)
   
    def __str__(self):
        return f"{self.link} {self.link_name}"

    class Meta:
        verbose_name = "Main Block"
        verbose_name_plural = "Main Blocks" 


class HeaderText(models.Model):
    class_item = models.CharField(max_length=255, blank=True, null=True)
    class_img = models.CharField(max_length=255, blank=True, null=True)
    class_image = models.CharField(max_length=255, blank=True, null=True)
    title1 = models.CharField(max_length=255, blank=True, null=True)
    title2 = models.CharField(max_length=255, blank=True, null=True)
    description1 = models.TextField(max_length=255, blank=True, null=True)
    description2 = models.TextField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=55, blank=True, null=True)
    link_name = models.CharField(max_length=55, blank=True, null=True)
 
    def __str__(self):
        return f"{self.title1} {self.title2}"

    class Meta:
        verbose_name = "Header Text"
        verbose_name_plural = "Header Texts"



class FooterText(models.Model):
    text1 = models.CharField(max_length=255, blank=True, null=True)
    text2 = models.CharField(max_length=255, blank=True, null=True)
   
    def __str__(self):
        return f"{self.text1} {self.text2}"

    class Meta:
        verbose_name = "Footer Text"
        verbose_name_plural = "Footer Text"   


class Socials(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField(max_length=255, blank=True)
    html_class = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Socials"
        

class FeaturedPlaces(models.Model):
    tag = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description1 = models.TextField(max_length=255, blank=True, null=True)
    description2 = models.TextField(max_length=255, blank=True, null=True)
   
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Featured Places"
        verbose_name_plural = "Featured Places"


class FeaturedBlocks(models.Model):
    title = models.CharField(max_length=55)
    text = models.TextField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="featured_blocks")
 
 
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Featured Blocks"
        verbose_name_plural = "Featured Blocks"


class Recent(models.Model):
    tag = models.CharField(max_length=55)
    title = models.CharField(max_length=55)
    description1 = models.TextField(max_length=255, blank=True, null=True)
    description2 = models.TextField(max_length=255, blank=True, null=True)
   
    def __str__(self):
        return f"{self.tag} {self.title}"

    class Meta:
        verbose_name = "Recent"
        verbose_name_plural = "Recent"


class ProjectsBlocks(models.Model):
    link_name = models.CharField(max_length=200,  blank=True, null=True) 
    image = models.ImageField(upload_to="projects_blocks")
 
 
    def __str__(self):
         return str(self.image)

    class Meta:
        verbose_name = "Projects Blocks"
        verbose_name_plural = "Projects Blocks"


class Videos(models.Model):
    tag1 = models.TextField(max_length=55, blank=True, null=True)
    tag2 = models.TextField(max_length=55, blank=True, null=True)
    tag3 = models.TextField(max_length=55, blank=True, null=True)
    title = models.CharField(max_length=55)
    description = models.TextField(max_length=255)
    link_url1 = models.URLField(max_length=200, blank=True, null=True) 
    link_url2= models.URLField(max_length=200, blank=True, null=True) 

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Videos"
        verbose_name_plural = "Videos"


class Entries(models.Model):
    tag1 = models.TextField(max_length=55, blank=True, null=True)
    tag2 = models.TextField(max_length=55, blank=True, null=True)
    title = models.CharField(max_length=55)
    description = models.TextField(max_length=255, blank=True, null=True)
    url_tab1 = models.CharField(max_length=55, blank=True, null=True)
    url_tab2 = models.CharField(max_length=55, blank=True, null=True)
    url_tab3 = models.CharField(max_length=55, blank=True, null=True)
    url_tab4 = models.CharField(max_length=55, blank=True, null=True)
    name_tab1 = models.CharField(max_length=55, blank=True, null=True)
    name_tab2 = models.CharField(max_length=55, blank=True, null=True)
    name_tab3 = models.CharField(max_length=55, blank=True, null=True)
    name_tab4 = models.CharField(max_length=55, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Entries"
        verbose_name_plural = "Entries"


class EntriesBlogs1(models.Model):
    tag = models.TextField(max_length=55)
    title = models.CharField(max_length=55)
    description = models.TextField(max_length=255) 
    image = models.ImageField(upload_to="entries_blogs1")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Entries Blogs1"
        verbose_name_plural = "Entries Blogs1"



class EntriesBlogs2(models.Model):
    tag = models.TextField(max_length=55)
    title = models.CharField(max_length=55)
    description = models.TextField(max_length=255) 
    image = models.ImageField(upload_to="entries_blogs2")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Entries Blogs2"
        verbose_name_plural = "Entries Blogs2"




class EntriesBlogs3(models.Model):
    tag = models.TextField(max_length=55)
    title = models.CharField(max_length=55)
    description = models.TextField(max_length=255) 
    image = models.ImageField(upload_to="entries_blogs3")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Entries Blogs3"
        verbose_name_plural = "Entries Blogs3"



class EntriesBlogs4(models.Model):
    tag = models.TextField(max_length=55)
    title = models.CharField(max_length=55)
    description = models.TextField(max_length=255) 
    image = models.ImageField(upload_to="entries_blogs4")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Entries Blogs4"
        verbose_name_plural = "Entries Blogs4"



class Contact(models.Model):
    tag = models.CharField(max_length=55)
    title = models.CharField(max_length=55)
    description1 = models.TextField(max_length=255, blank=True, null=True)
    description2 = models.TextField(max_length=255, blank=True, null=True)
   
    def __str__(self):
        return self.tag
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
