# Security Measures needed to keep django app safe

---

## Using a basic '.env' file to store sensitive data

1. create a `.env` file in the base directory.(where manage.py lies), save the credential there(like `SECRET_KEY=XXXXX`)
2. Add that .env to the `.gitignore`.
3. Then using,

   ```python
   import os
   SECRET_KEY = os.environ['SECRET_KEY']
   ```

* Use this like to know how it is done when [deploying in heroku](https://stackoverflow.com/a/61437799/12167598).