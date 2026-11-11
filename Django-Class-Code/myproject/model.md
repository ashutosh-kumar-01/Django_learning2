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