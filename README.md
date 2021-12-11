# DJANGO API HW

Create a branch new folder for a branch new django project.

## Set Up

Fork/Clone the repo.

Change into the folder.

Install dependencies
```
pipenv shell
pipenv install django
pipenv install djangorestframework 
pipenv install psycopg2
pipenv install prytz
```

```
django-admin startproject harry_potter .
```

Create your app for this project which will be an API 
```
django-admin startapp api
```


Review the django crud lesson for the settings.py set up steps for psql and restframework https://git.generalassemb.ly/ga-wdi-boston/django-crud as well as for your guide to complete the following steps.

### V1: Schools

First add schools.  

- `School` with name, location, and owner
- Complete models, serializers, views, and urls files for CRUD on school.

### V2: Houses

- `House` with name, animal and slogan
- Complete models, serializers, views, and urls files for CRUD on house.

### V3: School has many Houses

- Add school foreign key to house model
- Update school serializer so a school returns its houses

### V4: Students

- `Student` has given name and family name
- Complete models, serializers, views, and urls files for CRUD on student.

### V5: House has many Students

- Add house foreign key to student model
- Update house serializer so a house returns its students


### Bonus Validations

- `School`
  - validates name includes word `School`, error should say “Name must include the phrase School”
  - validates name must be unique
  - validates all properties must be present

- `House`
  - validates animal excludes cat, dog, bird, error should say “Animal can not be cat, dog or bird”
  - validates name format is first word capitalized, error should say “Name must be capitalized”
  - validates name must be unique

- `Student`
  - validates given name and family name length between 2 and 20 characters
  - validates all properties must be present
