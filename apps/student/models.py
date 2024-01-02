from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager



class UserManager(BaseUserManager):
    def _create_user(self, login,password=None, **extra_fields):
        user = self.model(login=self.normalize_email(login),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,login, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(login, password, **extra_fields)

    def create_superuser(self,login, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        return self._create_user(login, password, **extra_fields)


class User(AbstractUser):
    username = None
    full_name = models.CharField(max_length=50, null=True, blank=True)
    student_class = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    login = models.CharField(max_length=100, unique=True)  # Ensure unique
    password = models.CharField(max_length=128, null=True, blank=True)
    photo = models.ImageField(upload_to='images', blank=True, null=True)
    parents_number = models.CharField(max_length=20, null=True, blank=True)
    parents_name = models.CharField(max_length=255, null=True, blank=True)
    tariff = models.ForeignKey('Tariff', on_delete=models.CASCADE,related_name='tariff', null=True)
    tariff_price = models.PositiveBigIntegerField(default=0)
    balance = models.PositiveIntegerField(default=0)


    objects = UserManager()
    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    class Meta:
         verbose_name = 'Пользователь'
         verbose_name_plural = 'Пользователи'
    
    def __str__(self):
        return f"{self.full_name}"

    def save(self,*args, **kwargs):
        self.tariff_price = self.tariff.price
        return super().save(*args, **kwargs)



class Tariff(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.PositiveBigIntegerField(default=0)

    def __str__(self) -> str:
        return self.name








