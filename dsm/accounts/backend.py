from .models import customer
from .models import Teacher
class AuthBackend(object):
    def authenticate1(self,username=None, password=None):
        print("hdhsgdhg--->",username)
        try:
            user = customer.objects.get(name=username)
            if user:
                #if password==user.password_en:
                return user
        except customer.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return customer.objects.get(pk=user_id)
        except customer.DoesNotExist:
            return None

class Teacher_AuthBackend(object):
    def authenticate1(self,username=None, password=None):
        print("hdhsgdhg--->",username)
        try:
            user = Teacher.objects.get(name=username)
            if user:
                #if password==user.password_en:
                return user
        except customer.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Teacher.objects.get(pk=user_id)
        except customer.DoesNotExist:
            return None