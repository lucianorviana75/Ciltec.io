from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    celular = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')
    telefone_fixo = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone fixo')
    nomeId = models.CharField(max_length=500, blank=True, null=True, verbose_name='Nº id')

    def _srt_(self) -> str:
        return self.nome
    
    
class Servicos(models.Model):
    cliente = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    servicos =  models.CharField(max_length=100) 
    nomeID = models.CharField(max_length=500,blank=True, null=True, verbose_name='Nº ID')
    computador = models.CharField(max_length=100,blank=True, null=True)
    
     
    def _srt_(self) -> str:
        return self.servicos
    
    

    
class Area(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,null=True, blank=True) #Como o atributo cliente é uma ForeignKey e não é obrigatório, você pode defini-lo como nulo.
    servico = models.ForeignKey(Servicos, on_delete=models.CASCADE,null=True, blank=True) #Como o atributo cliente é uma ForeignKey e não é obrigatório, você pode defini-lo como nulo.
   
    class Meta:
        db_table = 'Area'
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'
        
        
        def _srt_(self) -> str:
            return self.id
   
        
        
     
     
     
