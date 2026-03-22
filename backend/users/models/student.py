from django.db import models
from .user import CustomUser

class Student(CustomUser):
  """
  Student Class it's the representation of the students in the system, 
  that it's a sub-class of the custom user class.
  
  Atrributes:
    id (uuid4): The Iddentifier for the user in the database  
    first_name (str): The first name of the user
    last_name (str): The last name of the user  
    email (str): The email of the user
    password (str): The password of the user
    created_at (datetime): The timestamp that represent the day that the student was created
    updated_at (datetime): The timestamp to determine the last modification of the user

  Example:
    >>> student = Student.objects.create(
        first_name = "Lucas",
        last_name = "Moura",
        password = "asd",
        email = "lucas.moura@gmail.com",
      )
    >>> print(student.first_name)
    >>> 'Lucas'
  """
  
  
  class Meta:
    app_label="users"
    db_table="students"

if __name__ == "__main__":
  import doctest 
  doctest.testmod()