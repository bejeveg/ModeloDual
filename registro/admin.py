from django.contrib import admin
from .models import Proyecto,Banner_items, solicitud_alumno,Post, Boleta, Alumno, AsesoresInterno, AsesoresExterno, Empresa, Area
#Aquí se añaden todos los modelos que se desee aparezcan o puedan aparecer en la interfaz admin django
admin.site.register(Alumno)
admin.site.register(Boleta)
admin.site.register(Proyecto)
admin.site.register(AsesoresInterno)
admin.site.register(AsesoresExterno)
admin.site.register(Area)
admin.site.register(Empresa)
admin.site.register(solicitud_alumno)
admin.site.register(Post)
admin.site.register(Banner_items)


