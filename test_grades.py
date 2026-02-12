import os
from dotenv import load_dotenv
from grades import get_grades

from canvasapi import Canvas

load_dotenv()

API_URL = f"https://{os.environ['CANVAS_DOMAIN']}"
API_KEY = os.environ["CANVAS_TOKEN"]

mycanvas = Canvas(API_URL, API_KEY)



grades = get_grades(mycanvas)

for course in grades:
    print(f"{course['name']}:\n  Score: {course['score']}\n  Grade: {course['grade']}\n")