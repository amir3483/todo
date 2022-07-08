from django.contrib import admin

from todo_api.models import Roles
from todo_api.models import Persions
from todo_api.models import Report1
from todo_api.models import Report2
from todo_api.models import Stations
from todo_api.models import Users
from todo_api.models import Location
from todo_api.models import form1
from todo_api.models import form2
from todo_api.models import NonConfirmation
admin.site.register(Roles)
admin.site.register(Persions)
admin.site.register(Report1)
admin.site.register(Report2)
admin.site.register(Stations)
admin.site.register(Users)
admin.site.register(Location)
admin.site.register(form1)
admin.site.register(form2)
admin.site.register(NonConfirmation)
# Register your models here.
