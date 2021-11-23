from django.db      import models


product_category = [
    (1, 'Dama'),
    (2, 'Caballero'),
    (3, 'Niño'),
    (4, 'Niña')
]

'''------Modelo Producto----------'''

class Product(models.Model):
    id              = models.AutoField(primary_key=True) 
    productName     = models.CharField('Producto', max_length = 30)
    productType     = models.IntegerField('Categoria', null=False, blank = False, choices = product_category,
                                            default = 1)
    productPrice    = models.FloatField('Precio', null=False, blank = False, default = 000.00)
    productAmount   = models.IntegerField('Cantidad', null=False, blank = False, default = 1)
    description     = models.CharField('Descripción', max_length = 255)                    
    productImg      = models.ImageField(upload_to = "productos", null=True)
