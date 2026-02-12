# grades.py
# canvas value should be Canvas() object from canvasapi, and must include the API key and URL
def get_grades(canvas):
    # Get current user and their active student enrollments
    user = canvas.get_current_user()
    enrollments = user.get_enrollments(type=['StudentEnrollment'], state=['active'])
    
    grades_list = []    

    # Collect grade information for each enrolled course
    for enrollment in enrollments:
        course_id = enrollment.course_id
        grades = getattr(enrollment, "grades", {})
        course_name = canvas.get_course(course_id).name
        current_score = grades.get("current_score")
        current_grade = grades.get("current_grade")

        grade_info = {}


        # Checks for the presence of a score, if there is none, it returns the "No Score information available"
        if current_score:
            grade_info = {
                "id": course_id,
                "name": course_name,
                "score": current_score,
                "grade": current_grade
            }
        else:
            grade_info = {
                "id": course_id,
                "name": course_name,
                "score": "No score information available",
                "grade":"No grade information available"
            }

        # Appends the grade information to the grades list
        grades_list.append(grade_info)

    # Returns the list of grade information for all courses
    return grades_list

