# phonebook
a Django web app for study

version： django 1.9
          python 3.5.0 

Quick start：
          
          1.   Add phonebook to your INSTALLED_APPS setting like this::
             INSTALLED_APPS = (
                ...
                'phonebook',
              )
          2.  Include the phonebook URLconf in your project urls.py like this::

              url(r'^phonebook/', include('phonebook.urls')),
              Run python manage.py syncdb to create the phonebook models.

          3.  Start the development server and visit http://127.0.0.1:8000/phonebook/ to start phonebook.

If you're lazy, just use pycharm to open the project, It's OK~
What's more:
          The superuser name: "leiger" password: "bupt1112" 
                                                                                          
                                                                                          
                                                                                                    writing by leiger
                                                                                                    2015.12.14
          
