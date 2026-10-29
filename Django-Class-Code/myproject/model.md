step1 :- create a class for model using which the table will be created
step2 :- create a migration file (python manage.py makemigrations)
step3 :- migrate the migration file (python manage.py migrate)

after all this , table will be created we will use sqlite (install extension SQLite viewr in vs code)









python manage.py shell

>>> from myapp.models import Emp
>>> Emp.objects.create(firstname='ashutosh', lastname='kumar',salary=56000,age=34)