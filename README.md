Demo Python Code someone might want to use as a starting point for interacting with the Beaconstac Forms API.


It is not a complete application in-and-of itself.  However you can post a dummy form to the API using this code.


----

The python code is written for Python 3.10.

- Create a virtual environment for Python 3.10
- Install the packages in the requirements.txt file
- Set the `BEACONSTAC_KEY` environment variable.


1.  `client_data.py` has some static, non-secret, values unique to your integration.
2.  `form_schema.py` is the data model for the form JSON (reversed engineered from examples pulled from their API).
3.  `hardcoded_form.py` generates a static (except for the title) test form for validating the API.
4.  `create_form.py` loads the hardcoded form into Beaconstac via the API.

5.  The bash scripts, `get_forms.bash` and `get_a_form.bash` use `httpie` to connect to the API and generate a list of forms, or download specific forms.  You will need to install `httpie` to run them.


