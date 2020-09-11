# Usedbrains: Used laptops selling website

---

## Project plan

1. Creating Basic Models
    * Creating the listings model
    * seller model
    * register models
2. Addition of Data
    * Adding data basic
    * Adding media data
3. Adding the Admin Page
    * Customizing admin page logo and CSS
    * Adding extra elements in admin area
4. Display listings
    * Pulling data from listing model
    * Creating templates, adding data to the template
    * Pagination
    * Dynamic contents
5. Search and Filtering options
    * search form creation
    * Filtering items
6. Managing Accounts
7. User registration login and logout
    * templates for user registration and login
    * message alerts
8. Nav bar links, dynamic page links
9.  Managing contacts
    * For contacting b/w seller and user
    * contact form
    * Checking inquires in admin panel sending emails
10. Deployment


## MODEL/DB FIELDS

### LISTING (Storing Info on a listing on the page)

1. id - auto increment id for the listings table
   * Data type "int".
   * id - **INT**
2. Need to connect sellers to listings - A seller is one who posting the listings
   * listing and seller table can be connected using a **FOREIGN KEY**
   * seller **INT** (**FOREIGN KEY** [From seller table])

   (Simply the entire seller is connected to the listing- can attach name, details,
   image from seller table/db to the listings.)
3. title - **STR** (MODEL-PRICE)

    <br>
4. *address - **STR** (Can be connected to seller foreign key)*
5. *city - **STR***
6. *state - **STR***
7. *pincode - **STR***
8. *phone number- **STR***

    <br>
9.  description - **TEXT**
10. price - **INT**  (req)
11. type - **STR**  (Dropdown laptop/tablet/desktop/parts)
13. Model - **STR** (Model of item)
14. Year - **STR**  (Year of buying)
15. Spec - **TEXT** (not necessory)
16. processor - **STR** (Add a dropdown later)
17. GPU - **BOOL** (yes/no) (default: NO)
18. GPU MODEL - **STR** (not necessory)
19. Screen Size - **INT** (in inches)
20. Condition(dropdown) - **STR** (dropdown) (Condition of the product)
21. condition - **TEXT** (description - optional)
22. Listing Date(list_date) - **DATE** (auto fetch)
23. is_published - **BOOL** (def: True) (the produced set to be published by default)

    *Main Image*
24. Product Image - **STR** (optional) (not sharing an actual image, storing the location of the image)

    *6 sub-images*
25. photo_1: **STR**
26. photo_2: **STR**
27. photo_3: **STR**
28. photo_4: **STR**
29. photo_5: **STR**
30. photo_6: **STR**


### SELLER DB (contains information about a seller/user)
1. Id - **INT**
2. name - **STR**
3. address - **STR**
4. city - **STR**
5. state - **STR**
6. pincode - **STR**
7. phone number- **STR**
8. photo - **STR**
9. description - **TEXT**
10. email - **STR**
11. join_date - **DATE** (Date they joined)


### CONTACT SELLER

Inquires that sent to the seller
1. id: **INT**
2. user_id: **INT**
3. listing: **INT** (connected to the title of the listing)
4. listing_id: **INT** (id of the listing)
5. name: **STR**
6. email: **STR**
7. phone: **STR**
8. message: **TEXT**
9. contact_date: **DATE**
10. is_authentic: **BOOL** ( A seller can be set authenticate in the admin panel,
    give em a badge or something in the sellers page)

* Any inquiries made to the contact


> #### Adding The Models

In django models.ImageField(), define where the files get uploaded(db stores the
address of that location), -- Set that `upload_to='photos/%Y/%m/%d/'` giving the
photos a date folder structure (year/month/date/<here_the_photo>)

On the admin page one can select a main field to be to be set as the display
field for models, on the listing model set it to the *title* field.

To validate some fields like a phone number the django regex validators can be used
like

```python
from django.core.validators import RegexValidator

class PhoneModel(models.Model):
    ...
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
```

To see the actual SQL queries a migrations make use the `python manage.py sqlmigrate listings 0001` where 'listings'
is the app name and '0001' is the migration file created when `python manage.py makemigrations` run.

* Add the `python manage.py migrate` command to docker-compose.
* Connect the running docker db service container using `docker exec -it <container name/id> bash` to interact with the container using a bash terminal, to check the added tables in the db named 'app'(which is set as project db).
* Can log in to postgres using `psql -U postgres` (postgres is the default user(and our user)), enter the password in
the docker-compose(not asked usually),
* switch to db 'app' using `\c app` (in postgres), to show tables use `\d` to see a particular table types
use `\d listings_listing` (listings_listing is the table name),
* use `SELECT * FROM listings_listing` to see the contents.
* in tables, can use *uuid* for better security and non colliding identifiers, google postgres uuids,

#### Setup Admin area

* Create a superuser (`python manage.py createsuperuser` --> `username: akshay`, `email: akshaych.dev@gmail.com`,
`password: UBadmin123`)
* Django admin staff status indicates a user is admin/not.(admin area is staff only). Check or uncheck the staff
  status in the user lists.
* Edit the `admin.py` in the listings and sellers app to get them up on the admin page. Register the models
* Add media root and url (Tells django where to look and store media).`MEDIA_ROOT = os.path.join(BASE_DIR, 'media')`
`MEDIA_URL = '/media/'`
* Also, in main `project.urls.py` add `[...] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`
* 