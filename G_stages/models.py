from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def _str_(self):
        return "User: "+self.username


class Dep(models.Model):
    
    libele = models.CharField(max_length=40,null=False)
     
    def _str_(self):
        return self.id
    
    
class Entre (models.Model):
    
    libele = models.CharField(max_length=40,null=False)
     
    def _str_(self):
        return self.id

 
    

class Etud (models.Model):
    matricule = models.IntegerField(max_length=40,null=False ) 
    Nom = models.CharField(max_length=40,null=False)
    prenom = models.CharField(max_length=40,null=False)
    Dep=models.ForeignKey(Dep, on_delete=models.CASCADE)
    
    
    
    def _str_(self):
        return self.id 
       
class Semestre(models.Model):
    libele = models.CharField(max_length=40,null=False)
    def _str_(self):
        return self.id
    
 
    
class Type_Encadrant(models.Model):
    type = models.CharField(max_length=40,null=False)
    
    def _str_(self):
        return self.id
    


     
    

class Simester(models.Model):
    libele = models.CharField(max_length=40,null=False)
    
    def _str_(self):
        return self.id
   

class Type_stage(models.Model):
    libele = models.CharField(max_length=40,null=False)
    
    def _str_(self):
        return self.id
    


class Encadrent(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField()
    numero= models.CharField(max_length=20)
    Type_Encadrant = models.ForeignKey(Type_Encadrant, on_delete=models.CASCADE)

    def _str_(self):
        return self.id