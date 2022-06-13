from datetime import date
from django.contrib.auth.models import BaseUserManager
from typing import Optional

class UserManager(BaseUserManager):
    def create_user(self, username, email, password):

        if username is None:
            raise TypeError("User must have a username")
        
        if email is None:
            raise TypeError("User must have a email")
        
        if password is None:
            raise TypeError("User must have a password")

        data = self.model(username=username, email=email)
        data.set_password(password)
        data.save()

        return data 

    def create_superuser(self, username, email, password):

        data = self.create_user(username, email, password)
        data.is_superuser = True
        data.is_staff = True
        data.is_active = True
        data.save()
        
        return data
    
    def update_password(self, id, new_password):
        if id is None:
            raise TypeError("Your ID not found to our database")
        
        if new_password is None:
            raise TypeError("New password must be filled")

        check = self.model()
        check.password = new_password
        check.save()

        return check

class VerifyCodeManager(BaseUserManager):
    def create_code(self, user_id:Optional[str], code, created=None, updated=None):
        if code is None:
            raise TypeError("Code is important field")
        
        data = self.model(user_id=user_id, code=code, created=created)
        data.save()
    
class createProduct(BaseUserManager):
    def save_product(self, user_id:Optional[str], id_product,category, stock, height, width, depth, cost, material, price):
        if id_product is None:
            raise TypeError("Code is important field")

        data = self.model(user_id=user_id, id_product=id_product, category=category,stock=stock, height=height, width=width, depth=depth, cost=cost, material=material, price=price)
        data.save()

class stockOut(BaseUserManager):
    def save_dates(self, product_id,dates:Optional[date]):
        if dates is None:
            raise TypeError("Fill date when stock Out happened")
        
        data = self.model(product_id=product_id, date=dates)
        data.save()
