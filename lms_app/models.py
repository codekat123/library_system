from django.db import models
class category(models.Model):
      type = models.CharField(max_length=50)
      def __str__(self):
            return self.type
class Books(models.Model):
      status_book = [
            ('available','available'),
            ('rental','rental'),
            ('sold','sold')
      ]
      title = models.CharField(max_length=250)
      author = models.CharField(max_length=250, null=True,blank=True)
      book_photo = models.ImageField(upload_to='photo',null=True,blank=True)
      author_photo = models.ImageField(upload_to='photo',null=True,blank=True)
      pages = models.IntegerField(null=True,blank=True)
      price = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
      price_of_rent = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
      period_of_rent = models.IntegerField(null=True,blank=True)
      active = models.BooleanField(default=True)
      status = models.CharField(max_length=50,null=True,blank=True,choices=status_book)
      category = models.ForeignKey(category,on_delete=models.PROTECT,)
      def __str__(self):
            return self.title
