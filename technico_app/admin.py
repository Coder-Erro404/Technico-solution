from django.contrib import admin
from .models import Contact , project ,product ,blog , Document ,addnote,impotantImage


# Register your models here.
admin.site.register(Contact)
admin.site.register(project)
admin.site.register(blog)
admin.site.register(Document)
admin.site.register(addnote)
admin.site.register(impotantImage)
admin.site.register(product)

