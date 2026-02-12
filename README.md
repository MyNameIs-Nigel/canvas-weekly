# canvas-weekly
Integrates Canvas API with Python to retrieve a list of relative information for the student, including Assignment Due Dates.

## Pre-Requisites
The following is required to run this program:
- Python
- Python `dotenv`
    - This can be installed with: `pip install python-dotenv`
- Python `dateutil`
- Python `canvasapi` 
    - This can be installed with: `pip install canvasapi`
- **Your API key for Canvas** and your organization's domain for canvas. 

> A common example of your domain could be: `yourorg.instructure.com`

### Obtaining an API Key in Canvas
*to-do*

---

## Weekly Assignment Usage

### Setting the Variables
To run, you need to first set the environment variables. My program uses `dotenv` to load and set variables so you can run this in an IDE like VScode.
1. Open the `generate_env.py`
2. Replace the values in the `env_content` dictionary with YOUR api key and domain.

> Include **ONLY** the subdomain and domain in the `CANVAS_DOMAIN` variable. *e.g. yourorg.instructure.com* NOT *https://yourorg.instructure.com/*
> Do **NOT** include the forward-slash at the end. 

### Running the Program
As of right now, I only have basic code to check the assignments due by the end of that current week, and save it as a json file. Soon I will integrate it with Power Automate to automatically import your assignments into the Microsoft tenant of your choice. That way you can use tools like **To-Do** to monitor your tasks.

Here is how you would run the program *after* changing your environment values in the `generate_env.py`:
1. In the root folder where you cloned the repo, run `generate_env.py`
2. Run the desired program *in this case, we will make a CSV of our assignments*: `assignments_weekly.py`
3. Verify nothing is missed

---

# Grades Usage
`grades.py` is a file that currently contains the following functions:
- get_grades(): returns a list of dictionaries that include relevant course info and grades.

### get_grades() Usage
To use get_grades() after importing it from grades, you need to use it with your `Canvas()` variable. 
> The structure of your canvas variable should be `Canvas(API_URL, API_KEY)` replacing your API_URL with `"https://yourorg.instructure.com"` and API_KEY with your API key generated from Canvas
Once you have declared a variable to be `get_grades(**your_canvas_variable_here**)` you can get the individual course info by iterating through the list and selecting from the dictionary values:
- `'id'` returns the course code (ex: 123456)
- `'name'` returns the course name (ex: Intro to Linux)
- `'score'` returns the current score in the course (ex: 89.23)
- `'grade'` returns a letter grade (ex: B+)

> Included in the files is a test_grades.py which uses that same `.env` file to return a formatted list of your courses and their grades. 