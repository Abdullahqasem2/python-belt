from django.db import models
import re
class UserModels(models.Manager):
    def register_validator(self, postData):
        errors = {}

        if len(postData['first_name']) < 2 or not postData['first_name'].isalpha():
            errors["first_name"] = "first name should be at least 2 characters and contains only characters"
        if len(postData['last_name']) < 2 or not postData['last_name'].isalpha():
            errors["last_name"] = "last name should be at least 2 characters and contains only characters"
        if len(postData['password']) < 8:
            errors["password"] = "password should be more than 8 characters atleast"
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        return errors

    def login_validator(self, postData):
        errors = {}
        email = postData['email']
        if len(postData['password']) < 8:
            errors["password"] = "password should be more than 8 characters atleast"
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if not EMAIL_REGEX.match(email):
            errors["email"] = "Email isn't in database"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserModels()
    
    

    
    
class Post(models.Model):
    post = models.CharField(max_length=45)
    users = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(User,related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

