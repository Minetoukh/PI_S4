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
    numero = models.CharField(max_length=20)
    

    def _str_(self):
        return self.id
    




    




class grp(models.Model):
    idSimester = models.ForeignKey(Simester, on_delete=models.CASCADE )
    idEtud = models.ForeignKey(Etud, on_delete=models.CASCADE )

    class Meta:
        unique_together = ('idSimester', 'idEtud')

    libele = models.CharField(max_length=50)
    membres = models.CharField(max_length=50)

    def _str_(self):
        return self.id

class Stage(models.Model):
    titre = models.CharField(max_length=50)
    dattedebut = models.DateField(max_length=50)
    dattefin= models.DateField(max_length=50)
    datesoutenance = models.DateField(max_length=50)
    lieu = models.CharField(max_length=50)
    Annee = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    grp=models.ForeignKey(grp, on_delete=models.CASCADE, to_field='id' )
    def _str_(self):
        return self.id
    



class Encdprof(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField()
    numero= models.CharField(max_length=20)
    

    def _str_(self):
        return self.id
class Encadrer (models.Model):
    Stage=models.ForeignKey(Stage, on_delete=models.CASCADE)
    Encadrent=models.ForeignKey(Encadrent, on_delete=models.CASCADE)

    def _str_(self):
        return self.id


class contenir (models.Model):
    grp=models.ForeignKey(grp, on_delete=models.CASCADE, to_field='id' )
    Dep=models.ForeignKey(Dep, on_delete=models.CASCADE)

