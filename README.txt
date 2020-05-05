to run server:

	python manage.py runserver


To those who want to make changes:

  To add a new page to the website:
    1. add the html file within the "pages/templates" directory
    2. create a function with a return request of the new html file within "pages/views.py"
    3. import the new function within "runningclub/urls.py"
    4. set a new path in the "urlpatterns" section of "runningclub/urls.py"

  If making changes to the modules, make sure to run the following commands:

  	python manage.py makemigrations
  	python manage.py migrate



Directories explained:

  "assets" contains all static files for the site:
    including: pictures, css theme, js code

  "bucks" and "pages" are both applications created using the command
                      python manage.py startapp appname
    "bucks" allows user accounts and data to be stored
    "pages" provide html files for all pages of the website


Git Help:
  To Configure your git:
    git config --global user.name “[firstname lastname]”
    git config --global user.email “[valid-email]”
    
  To Initialize remote repository:
    git remote add origin https://github.com/ClemsonRunningClub/ClemsonRunning (only need once)

  To Pull:
    git pull   OR   git fetch [alias]

  To Commit:
    git add files.py (only files you want to add)
    git commit -m "whatever changes you add"
    git push origin master
    sign in and the repositiory will update
