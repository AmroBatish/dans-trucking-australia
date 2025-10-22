from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

   

class QuoteRequest(models.Model):
    location = models.CharField(max_length=200)
    person = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.person} ({self.contact})"

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services_images/', default='path/to/default_image.jpg')  # يمكن أن يكون اسم الأيقونة أو رابط للصورة
    status = models.CharField(max_length=50)  # مثال: "متاح" أو "غير متاح"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='equipments/', default='path/to/default_image.jpg')  # سيتم تخزين الصورة في مجلد `equipments`
    status = models.CharField(max_length=50)  # مثال: "متاح" أو "مشغول"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class NewsletterSubscription(models.Model):
    email = models.EmailField()
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
