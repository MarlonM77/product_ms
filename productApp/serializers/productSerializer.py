from rest_framework             import serializers
from productApp.models.product  import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'productName', 'productType', 'productPrice', 'productAmount', 'description', 'productImg']
    
    def to_representation(self, obj):
        product = Product.objects.get(id = obj.id)
        return{
            'id'              : 'product.id',
            'ProductName'     : 'product.productName',
            'ProductType'     : 'product.productType',
            'ProductPrice'    : 'product.productPrice',
            'ProductAmount'   : 'product.productAmount',
            'Description'     : 'product.description',
            'ProductImg'      : 'product.productImg',
        }
        