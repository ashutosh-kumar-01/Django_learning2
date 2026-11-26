step1 :- create a class for model using which the table will be created
step2 :- create a migration file (python manage.py makemigrations)
step3 :- migrate the migration file (python manage.py migrate)

after all this , table will be created we will use sqlite (install extension SQLite viewr in vs code)







ashutoshkumar
Kumar@123

python manage.py shell

>>> from myapp.models import Emp
>>> Emp.objects.create(firstname='ashutosh', lastname='kumar',salary=56000,age=34)


<!-- for updation  -->
python manage.py shell
>>> from myapp.models import Emp
>>> e = Emp.objects.get(pk=2)
>>> e.salary = 69000
>>> e.save()
>>>



<!-- for deleation -->
python manage.py shell
python manage.py shell
>>> from myapp.models import Emp
>>> e = Emp.objects.get(pk=2)
>>> e.delete()
>>> 


Emp.objects.filter(pk=2).delete()










create user and activate it 1
$ python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.object.create_user(username='Ashutosh Kumar', email='babatilu075@gmail.com', password='Ashutoshkumar')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: type object 'User' has no attribute 'object'. Did you mean: 'objects'?
>>> User.object.create_user(username='Ashutosh', email='babatilu075@gmail.com', password='Ashutoshkumar')      
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: type object 'User' has no attribute 'object'. Did you mean: 'objects'?
>>> User.objects.create_user(username='Ashutosh', email='babatilu075@gmail.com', password='Ashutoshkumar')
<User: Ashutosh>
>>> user = User.objects.get(username="Ashutosh")
>>> user.is_staff = True
>>> user.save()
>>> 














>>> from django.contrib.auth.models import Permission, User
>>> from django.contrib.contenttypes.models import ContentType
>>> from myapp.models import Emp
>>> user = User.objects.get(username='Ashutosh')
>>> content_type = ContentType.objects.get_for_model(Emp)
>>> view_permission = Permission.objects.get(
... codename='view_emp',
... content_type=content_type,
... )
>>> user.user_permissions.add(view_permission)
>>> insert_permission = Permission.objects.get(codename='add_emp', content_type=content_type)
>>> user.user_permission.add(insert_permission)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'User' object has no attribute 'user_permission'. Did you mean: 'user_permissions'?
>>> user.user_permissions.add(insert_permission)
>>> 






>>> from django.contrib.auth.models import Group
>>> group = Group(name='newgroup')
>>> group.save()
>>> Group.objects.all()
<QuerySet [<Group: newgroup>]>
>>> 
