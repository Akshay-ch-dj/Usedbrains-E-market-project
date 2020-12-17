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
13. memory - **STR** (default 2GB)
14. graphics_type - **STR** (integrated/dedicated) (dropdown)
15. GPU MODEL - **STR** (not necessary)
16. Screen Size - **INT** (in inches) (dropdown + text)
17. Other_specifications - **TEXT** (description - optional)
18. Condition(dropdown) - **STR** (dropdown) (Condition of the product)
19. Condition_description - **TEXT** (optional)
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

> #### Sort the items according to date and filtering out the unpublished
* Do it in the views with the data from the models, `Listing.objects.order_by('-list_date').filter(is_published=True)`

> #### Add Listings in the front page.(3 nos. latest)
* Do the same as for 3 listings (`[:3]`) in home page.
> #### About page contents
* (Find a way to count the number of listings per seller)
* About page sellers displayed with authentic badges and the seller of the month.

> ### Single Listing Page

---
* From the model grab the particular listing data, render back to html in listings/views.py.
* <u>Note:</u> When a page is requested, Django creates an HttpRequest object that contains metadata about the request. Then Django loads the appropriate view, passing the HttpRequest as the first argument to the view function. Each view is responsible for returning an HttpResponse object.(from [django documentation](https://docs.djangoproject.com/en/3.1/ref/request-response/).)
* Take look here for a refresher of how the [urlpatterns works](https://docs.djangoproject.com/en/3.1/intro/tutorial03/#:~:text=In%20Django%2C%20web%20pages%20and,URL%20after%20the%20domain%20name).
* Then go to the listings/listing view. when we get a url pattern with the id it calls the view with that
request and requested id, use the `get_object_or_404(Listing, pk=listing_id)` to get the specific listing, (displays a 404 page not found error when it absents.)
* Using separate if statements for checking the photo exists now, using [yesno](https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#yesno) for filtering True/False to Yes/No.
* Single listing page completed need, add more details and design features.

> ### Search Functionality
-------
* When made a search, first check that thing exists, then pull it out of the requests, put them in a variable, then using database filter queries filter out the matching results.
* Django filter function, used to [filter out](https://docs.djangoproject.com/en/3.1/topics/db/queries/#retrieving-all-objects) from the queryset[ORM]. Here using the filter with '[icontains](https://docs.djangoproject.com/en/3.1/topics/db/search/#a-database-s-more-advanced-comparison-functions)'
* The keyword search enabled (looking in listing description). For keyword search in the whole datatbase,
django got a [searchvector](https://docs.djangoproject.com/en/3.1/ref/contrib/postgres/search/) method for postgres only.
* But it can laggy on large databases, use GIN-(Generalized Inverted Index) feature of postgresql. First Go through [this](https://django.cowhite.com/blog/mastering-search-in-django-postgres/) to get the basics then [this one: by pauloX](https://www.paulox.net/2017/12/22/full-text-search-in-django-with-postgresql/#searchvector), and this [stackoverflow link](https://stackoverflow.com/questions/53799552/django-full-text-search-optimization-postgres).
* There is another handmade raw method to add search in a pythonish way, check out [Julian Phalip](https://www.julienphalip.com/blog/adding-search-to-a-django-site-in-a-snap/).[need to figure out its performance].
* For search items to stay on search bar.
    * Return the 'GET' values to the search page, then add them as value tag in the html input. `'values': request.GET`
    * ```html
      <input type="text" name="keywords" .... value="{{ values.keywords }}">
      ```
    * Also add this to other fields, for the dropdown, for one option to stay selected until next,
    need to add `selected` to an `<option>` in the list, but need a logic for to go correctly, for eg: for price
    ```html
    <option value="{{ key }}"
      {% if key == values.price %}
          selected
      {% endif %}
      >{{ value }}</option>
    ```
    * removed the disabled labels in the dropdown.

### Authentication and Messaging
---
* Accounts app creation. check the `auth_user` table in `app` database on postgres.
* **'is_staff'**: - Allow one to login to the backend/not. The “staff” flag controls whether the user is allowed to log in to the admin interface (i.e., whether that user is considered a “staff member” in your organization). Since this same user system can be used to control access to public (i.e., non-admin) sites, this flag differentiates between public users and administrators.(ie, Any user assigned the staff flag, can login to the contributed admin app. Beyond this, they have no other special privileges.)
* <u>'is_active'</u>: - Activation and deactivation of an account similar to the fb_deactivation,
  a non_active user does not mean they are not authorized to do anything. For example they are allowed to activate their account.(Only active users are allowed to login.)
* recommend that you set this('is_active') flag to False instead of deleting accounts; that way, if your applications have any foreign keys to users, the foreign keys won’t break.
* <u>“Normal” admin users</u> : – that is, active, non-superuser staff members – are granted admin access through assigned permissions. Each object editable through the admin interface has three permissions: a create permission, an edit permission and a delete permission for all the models you had created.

    Django’s admin site uses a permissions system that you can use to give specific users access only to the portions of the interface that they need. When you create a user, that user has no permissions, and it’s up to you to give the user specific permission
* **'is_superuser'**:- If logged in as a superuser, you have access to create, edit, and delete any object (models). A superuser is just a convenience method to create a user with all permissions. They are just normal users given staff and all permissions by default.
* There is only one superuser, ie- akshay, in the table.


    Create basic login, register templates route them in the urls.py.

* Created login, register, dashboard html files in the templates/account folder.
* Route the login, logout, register, dashboard urls.
* For a logged in user the `login` and `register` gets replace with `logout` and `dashboard`.(later)
Add the highlighting functionality to the links as before.
* Added static markups to the pages.
* The form in the `register.html` get posted to the accounts/views.py, direct the target(ie the `action` tag in the
form) to the register route.
    ```html
    <form action="{% url 'login' %}" method="POST">
    ```
* Forms don't work in django without the **csrf token** (by adding:- `{% csrf_token %}`  )*(to prevent cross site forgery)*, it just adds a hidden security token that protects the data passed. looks like,
    ```html
    <input type="hidden" name="csrfmiddlewaretoken" value="NrDh93tNHlDp5m1YwwFcjP0fBeF3wGdXXXyxeMwVOPzHMzE4fIdxXYXxxe0IpX1n">
    ```
* Just identify the request ie, get is http **POST** or **GET**, by testing in the views.py. ***Notice***:- Any
`print()` statements will print the result in the program running console.

#### Registration and server side validation of the form.

* Basic server side validation checks,
    * Check for password match.
    * Check the email and, user name are unique( not in database already).
* Need to Give a message(like the javascript alert message, "You are successfully registered".)
* Then login afterwards.

#### **Django messages framework**
***
* Django's way to display flash messages, comes inbuilt with a messaging app.
* Django provides full support for cookie- and session-based messaging, for both anonymous and authenticated users.
* The messages framework allows you to temporarily store messages in one request and retrieve them for display in a subsequent request (usually the next one). Every message is tagged with a specific level that determines its priority (e.g., info, warning, or error).
* Messages are implemented through a middleware class and corresponding context processor.
    * Check `django.contrib.messages` is in INSTALLED_APPS.
    * MIDDLEWARE contains `django.contrib.sessions.middleware.SessionMiddleware` and `django.contrib.messages.middleware.MessageMiddleware`.( SessionMiddleware must be enabled and appear before MessageMiddleware in MIDDLEWARE, cz The default storage backend relies on sessions.)
    * The 'context_processors' option of the DjangoTemplates backend defined in your TEMPLATES setting contains `django.contrib.messages.context_processors.messages`.

      [If you don’t want to use messages, you can remove 'django.contrib.messages' from your INSTALLED_APPS, the MessageMiddleware line from MIDDLEWARE, and the messages context processor from TEMPLATES.]
* Configure as per the instructions in the official [messaging documentation](https://docs.djangoproject.com/en/3.1/ref/contrib/messages/).
* `FallbackStorage` is the default storage class (class first uses CookieStorage, and falls back to using SessionStorage for the messages that could not fit in a single cookie.).
* There are DEBUG, INFO, SUCCESS, WARNING and ERROR message types with default message tags as its lowercase versions(Message tags are a string representation of the message level plus any extra tags that were added directly in the view, message tags are used as CSS classes to customize message style based on message type). Can customize the tags using,
```python
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    # For types
    messages.INFO: 'error',
    # For levels
    50: 'critical',
}
```
* Django's default message levels and string representations are defined in django/contrib/messages/constants.py:
```
DEBUG = 10
INFO = 20
SUCCESS = 25
WARNING = 30
ERROR = 40

DEFAULT_TAGS = {
    DEBUG: 'debug',
    INFO: 'info',
    SUCCESS: 'success',
    WARNING: 'warning',
    ERROR: 'error',
}

DEFAULT_LEVELS = {
    'DEBUG': DEBUG,
    'INFO': INFO,
    'SUCCESS': SUCCESS,
    'WARNING': WARNING,
    'ERROR': ERROR,
}
```
* When comparing with bootstrap, Django's most severe level is `error` whereas Bootstrap's is `danger`. To To make Django's error level messages display easily in Bootstrap's alert-danger class. change the DEFAULT_TAGS entry from ERROR: 'error' to ERROR: 'danger'
* Take a good read on messages [here:](https://django-advanced-training.readthedocs.io/en/latest/features/contrib.messages/#2-deep-dive-code-walk-through)

#### message implementation in the project

* Add the message tags to the settings file, to compliment with the bootstrap theme.
  ```python
  MESSAGE_TAGS = {
      messages.ERROR: 'danger'
  }
  ```
* For the message body create '_alerts.html' in partials.***(Snippet can be used for all bootstrap-django applications)***.
* Add the '_alerts.html' to both register and login htmls(where it is needed), check it using a sample
redirect in the views.(can style it more if needed)

* #### ***Adding some custom javascripts*** to the alerts
  * To dismiss the error on its own. add js in app/static/js/main.js
  * Using jquery to do the fadeout., run `collectstatic` django command to get that into main static.
    (remember to clear cache of the browser after js/css changes(`shift + F5`, or full cache with`ctrl + shift + Delete`))
  * Now the messages set up, all need to do is display the when some logic fails, for eg. if passwords don't match,
    just call,
    ```python
    messages.error(request, 'Password not matching')
    return redirect('register')
    ```

#### Adding User registration
***

* Check the passwords, Bring in the default Django User model for checking the users and add new users
#### **[Django User Model]()**
  * The User model default got, these basic attributes.(Use a custom user model for any further requirements)
  * **username** (Required. 150 characters or fewer)
  * **first_name** (Optional (blank=True). 150 char)
  * **last_name** (Optional (blank=True). 150 char)
  * **email** (Optional (blank=True))
  * **password** (Required. A hash of, and metadata about, the password. (Django doesn’t store the raw password.))
  * **groups** (Many-to-many relationship to Group)
  * **user_permissions** (Many-to-many relationship to Permission)
  * **is_staff** (Boolean. Designates whether this user can access the admin site.)
  * **is_active** (Boolean.) (check out how to give more permissions to inactive users on documentation)
  * **is_superuser** (Boolean.)
  * **last_login** (datetime of the user’s last login)
  * **date_joined** (datetime designating when the account was created. Is set to the current date/time by default when the account is create)
* Validate the data, for add new user to the model using `User.objects.create_user(username=username, ...)`,
* The user can be logged in directly after logging in, or can redirect them to the login page

    To login directly after registering(bring in 'auth' from django.contrib)
    ```python
    # Login after register
    auth.login(request, user)
    messages.success(request, 'Registration Completed and \
                     Successfully logged in')
    return redirect('index')
    ```
* Add the '_alert' to the index page too, `{% include 'partials/_alerts.html' %}`, to receive alerts on front
  pages(future)

#### Login Page Implementation
---
* Login page done with the `auth.login(request, user)`, redirecting to dash board

#### Dashboard Navbar implementation

* Use an `if-else` jinja logic to display the login register links only if the user is not logged in
  (`{% if user.is_authenticated %} {% else %}`).( there is access to user object within all templates.)
* If user is logged in need to display the 'logout' and 'dashboard' links instead of the above.
* For a `Logout`, It cant just be a link because, we need get a http POST request in the views to log out a
  user, therefore it must be a form with a `method=POST`.('Can use the javascript with a fetch API or AJAX, but going in a simple way.')
* Use javascript to fetch the form with 'POST' and submit the form( it will the submit the form to the `action` url in the form. which routed in the urls.py and to the views.py)
* In views.py, check for `request.POST`, and log out the user.
* Give the message alerts to 'dashboard' too.

#### Change the titles for each page.
---
* Adding another block, need "Usedbrains" main title on all pages with the individual subtitles
* In the 'base' template, `<title>Usedbrains {% block title %}{% endblock %}</title>`.
* Modify before the content block in every page, `{% block title %}{{ listing.title }}{% endblock %}`

### Adding The contacts app for inquires
---
* `startapp` contacts.
* Make a model: **Contact**
* Register it in the admin area.
* Auto filling the inquiry form with the user data.
    * Inquiry model is at listing page end.
    * If the user is logged in, his name, id, email all need to be auto submitted, use an "if-else"
    jinja logic to do that.
    * Put a hidden `<input>`, if the user is authenticated, to pass un `id`.
    * Add functionality to Sent seller an email, if an inquiry done, for that pass the `listing.seller.email` and `listing.id` back to the view.

* **Submitting the form**
    * First fetched the posted data from the form (user_id, seller_email, listing_id, listing_title_, name(user), email, phone, message)
    * Got a strange error, with no clue happened at line`listing_title = request.POST['listing_title']`, there is no much data in the error titled *"MultiValueDictKeyError at /contacts/contact"*, looking at the POSTed data, it is found that, the title is not getting posted (but it is in the form field, looking strange)
    * OOh, its because of the disabled(I found it and removed first, but not done a whole round refresh)
    * Another Error, now it cant fetch the page redirected `return redirect(f'/listing/{listing_id}')`, ie. to `http://127.0.0.1:8000/listing/3`. It is the url of the 'listing-3' but throwing a 404 error.
    * oh, its just a mis serach ie the url must be `/listings/{listing_id}` not `/listing/{listing_id}`. Its solved.
* Just make it so that you cannot spam the enquiry, ie one user can make only one active inquiry on an item,
done by filtering and checking whether an early contact exists in db.
* But this method works only for registered users, for unregistered users to prevent them from making multiple
inquiries, need ip tracking and stuffs(or it can be done simply with cross checking the phone number and email)
* Do that for unregistered users with an else, done checking email OR phone matches for an unregistered user,
it will not get recorded.
* The two systems only works if the inquires are read and cleared regularly.

### [Django Emails](https://docs.djangoproject.com/en/3.1/topics/email/)
---

* Django customized python "smtplib" module, import from django.core.mail module.
  ```python
  from django.core.mail import send_mail

  send_mail(
      'Subject here',
      'Here is the message.',
      'from@example.com',
      ['to@example.com'],
      fail_silently=False,
  )

  ```
  * Configure the host, port in `settings.py`
    * EMAIL_HOST = 'smtp.gmail.com'
    * <u>SMTP PORT</u>:- [SMTP](https://www.sparkpost.com/blog/what-smtp-port/) (Simple Mail Transfer Protocol) is the basic standard that mail servers use to send email to one another across the internet.
    * use the standard port 587.
    * Done but to work with gmail it needs [apppassword](https://support.google.com/accounts/answer/185833?p=InvalidSecondFactor&visit_id=637359524955227511-2281000066&rd=1).

### Making the dashboard dynamic
---
* Modify the dashboard views and the rendered html.


<br>

---
## The First basic working of the project completed..
---

1. ### UI clearing..
   * The base.html clearing
   * index.html clearing.
       1. Reduce the size of search.
2. ### Make scalable responsive templates.