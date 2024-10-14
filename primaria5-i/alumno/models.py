from django.db import models

class alumno(models.Model):
    apaterno= models.CharField(max_length=50,verbose_name="Apellido paterno jaja")
    amaterno= models.CharField(max_length=50,verbose_name="Apellido materno")
    nombre= models.CharField(max_length=100,verbose_name="Nombre(s)")
    fecha_nac= models.DateField(verbose_name="Fecha de nacimiento",null=False,blank=False)
    fecha_ingreso= models.DateField(verbose_name="Fecha de ingreso",null=False,blank=False)

