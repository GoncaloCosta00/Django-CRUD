from django.db import models

# Create your models here.

class Cargo(models.Model):
    title = models.CharField(max_length=50)

    #isto é usado para no formulário vermos os cargos em vez da posiçao dos objetos
    def __str__(self):
        return self.title 
        
class Employee(models.Model):
    nome = models.CharField(max_length=100)
    emp_codigo = models.CharField(max_length=5)
    telefone= models.CharField(max_length=13)
    cargo= models.ForeignKey(Cargo,on_delete=models.CASCADE)