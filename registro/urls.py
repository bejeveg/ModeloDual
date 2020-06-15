from django.urls import path
from . import views as v
from django.conf.urls import include
from django.contrib.auth import views
"""
	Cada path es una ruta especifica con una estructura:
		path(url_escrita, view_que_manda_a_llamar, nombre_del_path)
	
	La view que se manda a llamar es un método que debe existir en el archivo views.py
	
	La variable name le da un nombre a cada urlpattern que permite llamarla desde un 
	archivo html de la forma:
		 "{% url 'name' %}"
"""
urlpatterns = [
	path('', v.principal, name='principal'),

	path('login/', v.login_general, name='login'),

	path('logout/', v.logout_user, name='logout'),

	#path('alumno/login/', v.login_alumno, name='login_alumno'),
	path('alumno/', v.alumno, name='alumno'),
	
	#path('asesoresExt/login/', v.login_asesoresExt, name='login_asesoresExt'),
	path('asesoresExt/', v.asesor_externo, name='asesor_externo'),
	
	#path('docentes/login/', v.login_docentes, name='login_docentes'),
	path('docentes/', v.docente, name='docente'),

	path('empresas/', v.Empresas, name='empresas'),

	path('editar_alumno/', v.editar_alumno, name='editar_alumno'),
	path('editar_asesor_interno/', v.editar_asesor_int, name='editar_asesor_interno'),
	path('editar_asesor_externo/', v.editar_asesor_ext, name='editar_asesor_externo'),

	path('proyectos/', v.proyectos, name='proyectos'),

	path('administrator/', v.administrator, name='administrator'),
	path('administrator/<int:value>/', v.administrator, name='administrator'),

	path('reportes_administrador/', v.reportes_administrador, name='reportes_administrador'),

	path('boleta/', v.boleta, name='boleta'),

	path('reportes_asesores/', v.reportes_asesores, name='reportes_asesores'),

	path('reporte_personal/', v.reporte_personal, name='reporte_personal'),

	path('carpeta_reportes/', v.carpeta_reportes, name='carpeta_reportes'),

	path('album_fotos/', v.album_fotos, name='album_fotos'),

]