from django.db import models

# Create your models here.

class Urun(models.Model):
    isim=models.CharField(max_length=150)
    fiyat=models.FloatField()
    aciklama=models.TextField()
    resim=models.ImageField(upload_to='images')
    tarih=models.DateTimeField(auto_now_add=True)
    kategoriler=[
        ("macpro","Mac Pro"),
        ("macstudio","Mac Studio"),
        ("macbookpro","Macbook Pro"),
        ("macbookair","Macbook Air"),
        ("imac","iMac")
        ]
    kategori=models.CharField(max_length=100,
                              choices=kategoriler,default="Mac Pro")

    def __str__(self):
        return self.isim