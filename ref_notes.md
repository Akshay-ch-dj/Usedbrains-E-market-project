# Usedbrains: Used laptops selling website
---
Used laptops often comes to small repairing shops, or servicing centers, they pick the working laptops,
even repairable laptops just gets in to e-waste. Actual makers don't promote the reusability of a laptop,

Many companies replace their employees personal laptops, the old ones taken
down as e-waste, no one makes such interests in selling them because the market for used laptops
is low.
As COVID 19 changes many things, one of main thing is the education sector, In the forthcoming years, education
going to get more digital, any teacher can do classes from any where, and there is already that information explosion
happening,

But in a developing country like india, not every young minds got a chance to get a brand new laptop for
their learning, as even a running 10 year old laptop can be good at usual browsing, online classes and coding, a lot more people get benefitted. Usedbrains is made from that point of view to make that right connection happen,


This project is developed as a bridge between those sellers and those people who now can't afford
a new laptop or just need a secondary basic one.

Also,

As computers are customizable, A hard-drive missing computer can be benefitted to one who got a portable
hard-drive, A display broken one can be benefitted to one who got a old monitor lying around, A lap with
keyboard complaint can be benefitted to a user who does not needs portability. As so and so many hacks and
use cases lying around, just getting of that old lap as e waste in this time is not a very smart idea anytime..
As any good component is worth selling.

In Usedbrains, buyers can contact to seller inquire about the working of laptop, find their best buy,
Authentic sellers can pick the good laptops repair the minor damages, replace the hard-drives(data-security)
and sell through Usedbrains that can help some one somewhere go digital and to access the endless possibilities
of education, someone who wishes to reuse components,

reduce e-waste, bring up a smile :).

### Working Strategy

Sellers can register in Usedbrains by filling the details, and post their listings on the
site, whole registered users can browse, inquire about the product and contact the seller and can make a deal
UB provides a platform for it(the service can be scaled down to be used for single merchant.)


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
---

### LISTING (Storing Info on a listing on the page)

1. id - auto increment id for the listings table
   * Data type "int".
   * id - **INT** (serial int later if needed into other more secure uuid or something)

    (Django creates an id field automatically)
2. Need to connect sellers to listings - A seller is one who posting the listings
   * listing and seller table can be connected using a **FOREIGN KEY**
   * seller **INT** (**FOREIGN KEY** [From seller table])

   (The entire seller  is connected to the listing- can attach name, details,
   image from seller table/db to the listings.)
3. title - **STR** (MODEL-PRICE)
<br>
(*address - **STR** (Can be connected to seller foreign key)* *city - **STR*** *state - **STR***
*pincode - **STR*** *phone number- **STR***)
<br>

4.  description - **TEXT**
5.  price - **INT**  (req)
6.  type - **STR**  (Dropdown laptop/tablet/desktop/parts UI element(admin))
7.  Model - **STR** (Model of item)
8.  Year - **STR**  (Year of buying)
9.  Spec - **TEXT** (not necessary)
10. in_warranty - **BOOL** (default: False)
11. processor - **STR** (Add a dropdown later (UI element))
12. ram - **STR** (str) (dropdown UI)
13. graphics_type - **STR** (integrated/dedicated) (dropdown)
14. GPU MODEL - **STR** (not necessary)
15. Screen Size - **INT** (in inches) (dropdown + text)
16. Other_specifications - **TEXT** (description - optional)
17. Condition(dropdown) - **STR** (dropdown) (Condition of the product)
18. Condition_description - **TEXT** (optional)
20. Listing Date(list_date) - **DATE** (auto fetch)
21. is_published - **BOOL** (def: True) (the produced set to be published by default)


    *Main Image*
22. Product Image - **STR** (required) (db storing the location of the image: so STR)

    *six sub-images* (not necessary)
23. photo_1: **STR**
24. photo_2: **STR**
25. photo_3: **STR**
26. photo_4: **STR**
27. photo_5: **STR**
28. photo_6: **STR**


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
12. is_mvp: **BOOL** (to declare the top sellers)
11. is_authentic: **BOOL** ( A seller can be set authenticate in the admin panel,
give em a badge or something in the sellers page)



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


> ### Adding The Models
***

&emsp; In django models.ImageField(), define where the files get uploaded(db stores the
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
#### Setup media paths
* Add media root and url (Tells django where to look and store media).`MEDIA_ROOT = os.path.join(BASE_DIR, 'media')`
`MEDIA_URL = '/media/'`
* Also, in main `project.urls.py` add `[...] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`
#### Setup static paths (already set up; documenting)
* The static files are in folder(added early): `app/app/static/`(all css, js, img files or the proj. resources) - it is specified in the `STATICFILES_DIRS`.
* It is added to main static (`STATIC_ROOT = os.path.join(BASE_DIR, 'static')`) using the collectstatic management command(`python manage.py collectstatic`),
-which collects static from all the folders, in the STATICFILES_DIRS, in the project the it is tha same as specified
above
```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'app/static')
]
```
* Then combines all the admin static files with it then copy them to STATIC_ROOT(`static` folder in the main directoty), the app takes all static files from here.

#### Adding data

The sellers are  added by admins through admin area in the first version(need to update, that a user can be
registered as a seller(connecting a user with seller table)).

#### Customizing Django Admin

* Changing the company name and logo
    inside templates create admin section, extend the admin template with `{% extends 'admin/base.html' %} {% load static %}` and cadd a block `{% block branding %} {% endblock %}`, then change "h1" and other tags.
    (add a logo as img(`{% static 'img/logo.png' %}`) and other html elements in here.)

    For adding the css,
    ```html
    {% block extrastyle %}
    <link rel="stylesheet" href="{% static 'css/admin.css' %}">
    {% endblock %}
    ```
    (add the css file in the target static/css folder,)
    Style the elements overriding the default class Use the chrome inspect tools to identify the classes

* Customizing the admin panel tables
    Add the custom class to modify the admin panel in the `admin.py` of both seller and listing pages.
    in the django documentation explore all cool things one can do [Django admin listings](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display).

---
> ### Fetching and displaying data
***

* The key idea is to loop through the all the listings and displaying the template
html with the data fetched.(template html is in the listings.html)
* Use django template logic for that. grab one template loop through the listings
replace the data.(on the UI front need to rearrange the icons create more of em
use fontawsome old cdn for that icons style it matching the theme)
* Remember to add photos using jinja, add a `.url` with the src. as
`src="{{ listing.photo_main.url }}"`, to fetch from the media path specified in
the main `urls.py`.
* To add comma separation to the price fields
    - Use some ext app like "humanize" to get the functionality, use the method
    intComma(with a pipe character, `{{ listing.price | intcomma }}`), to get the separation. here, in the [documentation](https://docs.djangoproject.com/en/3.1/ref/contrib/humanize/), can find more about the "django.contrib.humanize"

        (lets go with that way now, but can an always add a script that does the same in the views.py- modify the listing then pass that one to the renderer.)
        Added custom filter in the `listings/templatetags/my_listings.py` to convert indian currency format
* To enter the foreign key attributes in the listing template, just use this `{{ listing.seller.<attribute> }}`
* to limit characters in the template for nice viewing can use a filter custom.
* The "humanize" `timesince` filter does a nice job in filtering the dates.
* Reduced the font size of time displayed, (make sure `shift+ctrl+Delete` on chrome).
* Correct the urls in the more info button (href="{% url 'listing' listing.id %}"), also add the 'listing_id'
in views.py.


Linter tweaking in vs code: Go to settings-> Python linting > "--errors-only"

> #### Using pagination in Django

* The [official documentation](https://docs.djangoproject.com/en/3.1/topics/pagination/).
* To get the exact styled pagination, compare the django pagination with the bootstrap pagination.
* The logic is 6 pages per page,(3 for testing) if there is only 6 need no pagination.
  (done with the django jinja logic)

> #### Sort the items according to date