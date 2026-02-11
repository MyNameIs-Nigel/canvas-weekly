# Dependency imports
from datetime import datetime, timezone, timedelta, time
import os
import csv
from zoneinfo import ZoneInfo
from dateutil import parser
from dotenv import load_dotenv

# Canvas API imports
from canvasapi import Canvas

# Load environment variables from .env file
load_dotenv()

API_URL = f"https://{os.environ['CANVAS_DOMAIN']}"
API_KEY = os.environ["CANVAS_TOKEN"]

# Assign Canvas API client
canvas = Canvas(API_URL, API_KEY)

# ---- Time window: now -> end of this week (Sunday 11:59 PM local) ----
LOCAL_TZ = ZoneInfo("America/Denver")  # Mountain Time

now_local = datetime.now(LOCAL_TZ)

# Python weekday(): Mon=0 ... Sun=6
days_until_sunday = (6 - now_local.weekday()) % 7
sunday_date = (now_local + timedelta(days=days_until_sunday)).date()

end_of_week_local = datetime.combine(sunday_date, time(23, 59, 0), tzinfo=LOCAL_TZ)
# if you want 11:59:59 PM exactly, use time(23, 59, 59)

# Convert bounds to UTC for safe comparison with Canvas timestamps
start_utc = now_local.astimezone(timezone.utc)
end_utc = end_of_week_local.astimezone(timezone.utc)

# ---- Collect assignments due in range ----
rows = []

user = canvas.get_current_user()
courses = user.get_courses(enrollment_state="active")  # filter to active enrollments [1](https://canvasapi.readthedocs.io/en/stable/examples.html)

for course in courses:
    course_name = getattr(course, "name", "")
    course_id = getattr(course, "id", "")

    try:
        # CanvasAPI supports course.get_assignments() (see examples) [1](https://canvasapi.readthedocs.io/en/stable/examples.html)
        for a in course.get_assignments():
            due_at = getattr(a, "due_at", None)
            if not due_at:
                continue

            # due_at is an ISO-8601 timestamp string per API docs [2](https://www.canvas.instructure.com/doc/api/assignments.html)[3](http://www.humandesigncollege.org/doc/api/assignments.html)
            due_dt_utc = parser.isoparse(due_at).astimezone(timezone.utc)

            if start_utc <= due_dt_utc <= end_utc:
                due_local_str = due_dt_utc.astimezone(LOCAL_TZ).strftime("%Y-%m-%d %I:%M %p %Z")

                rows.append({
                    "assignment_name": getattr(a, "name", ""),
                    "course_name": course_name,
                    "course_id": course_id,
                    "due_date_local": due_local_str,
                    "due_date_utc": due_dt_utc.isoformat()
                })

    except Exception as e:
        # Some courses may be restricted or archived in odd ways; skip gracefully
        print(f"Skipping course {course_name} ({course_id}): {e}")

# Sort by due date (UTC)
rows.sort(key=lambda r: r["due_date_utc"])

# ---- Write CSV ----
output_file = f"output/assignments_due_week-{now_local.strftime('%Y-%m-%d')}.csv"
fieldnames = ["assignment_name", "course_name", "course_id", "due_date_local", "due_date_utc"]

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {len(rows)} assignments to {output_file}")
print(f"Range: {now_local.strftime('%Y-%m-%d %I:%M %p %Z')} -> {end_of_week_local.strftime('%Y-%m-%d %I:%M %p %Z')}")
