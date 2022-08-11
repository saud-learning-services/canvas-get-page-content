from helpers import create_instance
import os
from dotenv import load_dotenv
import sys
from util import shut_down

load_dotenv()

API_URL = os.getenv("API_INSTANCE")
API_KEY = os.getenv("API_TOKEN")


def get_course_id():
    try:
        if sys.argv[1]:
            course_id = sys.argv[1]
        else:
            course_id = os.getenv("COURSE_ID")
        print(f"Course ID: {course_id}")
        return course_id

    except Exception as e:
        shut_down(f"Enter a course id in .env or as argument!")


def main():
    canvas = create_instance(API_URL, API_KEY)
    course_id = get_course_id()
    course = canvas.get_course(course_id)

    pages = course.get_pages()
    print(pages[0])


if __name__ == "__main__":
    main()
