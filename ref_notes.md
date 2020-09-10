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


# MODEL/DB FIELDS

## LISTING (Storing Info on a listing on the page)

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


## SELLER DB (contains information about a seller/user)
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


## CONTACT SELLER

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

* Any inquiries made to the contact
