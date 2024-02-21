from django.db import models

class React(models.Model):
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.CharField(max_length=50,null=True,blank=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    fields =['desc','price']
 
    def __str__(self):
           return self.desc
