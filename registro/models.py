from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import math
from django.core.exceptions import ValidationError
from django.contrib import messages

"""
Cada clase es el equivalente a una tabla en la base de datos

Cada objeto de una clase es el equivalente a un registro

Los elementos de la clase son los campos dentro de la base de datos

Tipos de campos:
	CharField: Texto en una linea
	EmailField: Correo
	URLField: Link
	TextField: Cuadro de texto sin limite especificado
	PositiveSmallInteger: Entero positivo pequeño

Atributos:
	primary_key: Define el campo como clave primaria (por defecto crea una id autoincrementable)
	max_length: longitud máxima de la cadena
	default: valor por defecto
	blank, null: Por defecto false, si se definen como True permiten valores nulos o vacios
	choices: lista de valores que el campo puede tomar
	ForeignKey(Clase_referencia, on_delete=models.PROTECT): el campo debe ser una llave foranea
		de la clase de refencia, on_delete=models.PROTECT impide borrar un registro si este es usado
		como clave foranea por otra clase
	validators=[MinValueValidator(A),MaxValueValidator(B)]: Rango de valores permitido

Métodos:
	__str__: el valor que retorne será el que aparezca en lugar de la id


"""
class Banner_items(models.Model):
	titulo=models.CharField(max_length=50)
	image = models.ImageField(upload_to='banner_gallery/')
	redirect_url=models.URLField(blank=True, default="")
	red_choices=(('Proyectos','Proyectos'),('Album','Album'), ('Empresas','Empresas'))
	redirect_page_section=models.CharField(null=True,blank=True, choices=red_choices, max_length=30)
	orden_aparicion=models.PositiveSmallIntegerField(unique=True)
	def __str__(self):
		return self.titulo
class Post(models.Model):
    titulo=models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images_gallery/', blank=True, null=True)
    alternative_url=models.URLField(blank=True, null=True)
    def __str__(self):
        return self.titulo
class solicitud_alumno(models.Model):
	s_no_control=models.CharField(max_length=9, primary_key=True)
	s_nombre=models.CharField(max_length=50)
	s_carrera=models.CharField(max_length=50)
	s_correo=models.EmailField()
	s_semestre=models.CharField(max_length=2)
	def __str__(self):
		return self.s_nombre

class Area(models.Model):
	nombre=models.CharField(max_length=30)
	descrip=models.TextField()
	def __str__(self):
		return self.nombre

class Alumno(models.Model):
	no_control=models.CharField(max_length=9, primary_key=True)
	nombre=models.CharField(max_length=50)
	carrera=models.CharField(max_length=50)
	semestre=models.CharField(max_length=2)
	#Black=True permite dejarlo en blanco, default es false
	edad=models.PositiveSmallIntegerField(default=18, validators=[MinValueValidator(18),MaxValueValidator(100)]) 
	sex_choices=(('H','Hombre'), ('M','Mujer') )
	sexo=models.CharField(blank=True, choices=sex_choices, max_length=1) #No obligatorio
	domicilio=models.TextField(blank=True, default="") #No obligatorio
	telefono=models.CharField(blank=True,default="", max_length=20) #No obligatorio
	correo=models.EmailField(blank=True, default="") #No obligatorio
	red_choices=(('Facebook','Facebook'),('Instagram','Instagram'), ('Twitter','Twitter'))
	red_social=models.CharField(blank=True, choices=red_choices, max_length=30) #No obligatorio
	red_social_url=models.URLField(blank=True, default="") #No obligatorio
	estado_actual=models.CharField(default="", blank=True,max_length=20) #No obligatorio
	def __str__(self):
		return self.nombre
	#Cada que se gurda un Alumno o actualice la información desde el panel admin de django
	def save(self, *args, **kwargs):
		#Se llama al constructor, ejecutando el método save original
		super(Alumno, self).save(*args, **kwargs)
		#Si no existe un usuario de tipo Alumno con el no_control de este, entonces se crea
		if User.objects.filter(username=self.no_control).exists()==False:
			#El usuario es la matricula del estudiante y su password a+matricula
			user = User.objects.create_user(self.no_control, '', ('a'+str(self.no_control)))
			my_group = Group.objects.get(name='Alumnos') 
			my_group.user_set.add(user)

class AsesoresInterno(models.Model):
	no_empleado=models.CharField(max_length=20, primary_key=True)
	nombre=models.CharField(max_length=100)
	departamento=models.ForeignKey(Area, on_delete=models.PROTECT)
	telefono=models.CharField(max_length=20, blank=True, default="") #No obligatorio
	correo=models.EmailField(default="", blank=True) #No obligatorio
	def __str__(self):
		return self.nombre
	#Cada que se gurda un Docente o actualice la información desde el panel admin de django
	def save(self, *args, **kwargs):
		#Se llama al constructor, ejecutando el método save original
		super(AsesoresInterno, self).save(*args, **kwargs)
		#Si no existe un usuario de tipo Asesor interno con el no_control de este, entonces se crea
		if User.objects.filter(username=self.no_empleado).exists()==False:	
			#El usuario el no_empleado  y su password a+no_empleado
			user = User.objects.create_user(self.no_empleado, '', ('a'+str(self.no_empleado)))
			my_group = Group.objects.get(name='Asesor interno') 
			my_group.user_set.add(user)	

class Empresa(models.Model):
	nombre=models.CharField(max_length=100)
	rfc_empresa=models.CharField(max_length=13, primary_key=True)
	den_social=models.TextField(blank=True, default="")
	giro=models.TextField(blank=True, default="") #No obligatorio
	responsable=models.CharField(max_length=60)
	convenio=models.CharField(max_length=30)
	domicio_fiscal=models.TextField()
	telefono=models.CharField(max_length=20, default="") #No obligatorio
	url_logo=models.URLField() 
	def __str__(self):
		return self.nombre

class AsesoresExterno(models.Model):
	no_empleado=models.CharField(max_length=20, primary_key=True)
	empresa_rfc=models.ForeignKey(Empresa, on_delete=models.PROTECT)
	nombre=models.CharField(max_length=100)
	telefono=models.CharField(default="", max_length=20, blank=True) #No obligatorio
	correo=models.EmailField(default="", blank=True) #No obligatorio
	def __str__(self):
		return self.nombre
	#Cada que se gurda un AsesorExterno o actualice la información desde el panel admin de django
	def save(self, *args, **kwargs):
		#Se llama al constructor, ejecutando el método save original
		super(AsesoresExterno, self).save(*args, **kwargs)
		#Si no existe un usuario de tipo Asesor externo con el no_control de este, entonces se crea
		if User.objects.filter(username=self.no_empleado).exists()==False:	
			#El usuario el no_empleado  y su password a+no_empleado
			user = User.objects.create_user(self.no_empleado, '', ('a'+str(self.no_empleado)))
			my_group = Group.objects.get(name='Asesor externo') 
			my_group.user_set.add(user)	

class Proyecto(models.Model):
	nombre=models.CharField(max_length=100)
	descripcion=models.TextField(blank=True,  default="")
	alumno=models.ForeignKey(Alumno, on_delete=models.PROTECT)
	empresa_rfc=models.ForeignKey(Empresa, on_delete=models.PROTECT)
	asesor_interno=models.ForeignKey(AsesoresInterno, on_delete=models.PROTECT)
	asesor_externo=models.ForeignKey(AsesoresExterno, on_delete=models.PROTECT)
	cal_final=models.PositiveSmallIntegerField(default=0, 
		validators=[MinValueValidator(0),MaxValueValidator(100)]) #No obligatorio
	area=models.ForeignKey(Area, on_delete=models.PROTECT)
	trabajo_posterior=models.CharField(max_length=8, choices=(('Si','Si'),('No','No'), ('En curso','En curso')))
	fecha_de_creacion=models.DateField(auto_now_add=True)
	finalizado=models.CharField(max_length=8, choices=(('Si','Si'),('No','No'), ('En curso','En curso')))
	tipo_proyecto=models.CharField(max_length=12, choices=(('Residencias','Residencias'),('Practicas','Practicas')))
	url_folder=models.URLField(blank=True, null=True) #No obligatorio
	def __str__(self):
		return self.nombre
	#Antes de guardar o actualizar desde el panel django de admin
	def save(self,direct=False, *args, **kwargs):
		super().save(*args, **kwargs)
		#Si no existe una boleta para el proyecto esta se crea
		if not Boleta.objects.filter(proyecto=self).exists():
			Boleta(proyecto=self, alumno=self.alumno).save()
		#Si el proyecto se marca como finalizado se calcula la calificación final
		#Este valor se guarda tanto en la boleta como el el proyecto
		#Esto solo sucede si no se llama directamente
		if not direct:
			if self.finalizado=="Si":
				b=Boleta.objects.get(proyecto=self, alumno=self.alumno)
				promedio= math.ceil( (b.docente_p1+b.docente_p2+b.docente_p3+b.asesor_p1+b.asesor_p2+b.asesort_p3)/6 )
				b.final=promedio
				b.save(True)
				self.cal_final=promedio
				super().save(*args, **kwargs)

class Boleta(models.Model):
	proyecto=models.ForeignKey(Proyecto, on_delete=models.PROTECT)
	alumno=models.ForeignKey(Alumno, on_delete=models.PROTECT)
	docente_p1=models.PositiveSmallIntegerField(default=0, 
		validators=[MinValueValidator(0),MaxValueValidator(100)]) 
	asesor_p1=models.PositiveSmallIntegerField(default=0, 
		validators=[MinValueValidator(0),MaxValueValidator(100)]) 
	docente_p2=models.PositiveSmallIntegerField(default=0, 
		validators=[MinValueValidator(0),MaxValueValidator(100)]) 
	asesor_p2=models.PositiveSmallIntegerField(default=0, 
		validators=[MinValueValidator(0),MaxValueValidator(100)]) 
	docente_p3=models.PositiveSmallIntegerField(default=0, 
		validators=[MinValueValidator(0),MaxValueValidator(100)]) 
	asesort_p3=models.PositiveSmallIntegerField(default=0, 
		validators=[MinValueValidator(0),MaxValueValidator(100)])
	final=models.PositiveSmallIntegerField(default=0, 
		validators=[MinValueValidator(0),MaxValueValidator(100)]) 
	comentarios=models.TextField(blank=True, default="")
	def __str__(self):
		return self.proyecto.nombre
	def save(self,direct=False, *args, **kwargs):
		#Si el método save se llama directamente de otro metodo
		if direct:
			super().save(*args, **kwargs)
		#Si el metodo save se llama desde admin django o similar
		else:
			proyecto_this=Proyecto.objects.get(id=self.proyecto.id)
			if proyecto_this.finalizado=="Si":
				promedio= math.ceil((self.docente_p1+self.docente_p2+self.docente_p3
					+self.asesor_p1+self.asesor_p2+self.asesort_p3)/6 )
				proyecto_this.cal_final=promedio
				proyecto_this.save(True)
				self.final=promedio
			super().save(*args, **kwargs)

		
	"""
	def clean(self, *args, **kwargs):
		if Boleta.objects.filter(proyecto=self.proyecto, alumno=self.alumno).exists():
			raise ValidationError('Ya existe una boleta registrada con el alumno y proyecto mencionados.')
	"""
#Cada que se intente eliminar un alumno, asesor o docente, previo a su eliminación
#Se llama a su respectivo pre_delete que elimina el usuario que coincide con su
#no_control o no_empleado
@receiver(pre_delete, sender=Alumno)
def delete_alumno(sender, instance, **kwargs):
	try:
		u = User.objects.get(username = instance.no_control)
		u.delete()
	except:
		a=1

@receiver(pre_delete, sender=AsesoresInterno)
def delete_ai(sender, instance, **kwargs):
	try:
		u = User.objects.get(username = instance.no_empleado)
		u.delete()
	except:
		a=1   
@receiver(pre_delete, sender=AsesoresExterno)
def delete_ae(sender, instance, **kwargs):
	try:
		u = User.objects.get(username = instance.no_empleado)
		u.delete()
	except:
		a=1   