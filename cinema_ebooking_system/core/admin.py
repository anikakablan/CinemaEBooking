from core.models import User
from django.contrib import admin

# Register your models here.
from core.models import User 

admin.site.site_header = 'Bookflx Admin'

admin.site.register(User)

