# canvas-weekly
---
Integrates Canvas API with Python to retrieve a list of relative information for the student, including Assignment Due Dates.

## Pre-Requisites
The following is required to run this program:
- Python
- Python `dotenv`
    - This can be installed typically by typing `pip install python-dotenv`
- Python `dateutil`
- Python `canvasapi`
- **Your API key for Canvas** and your organization's domain for canvas. 

> A common example of your domain could be: `yourorg.instructure.com`

### Obtaining an API Key in Canvas


## Usage

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