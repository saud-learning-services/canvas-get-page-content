from canvasapi import Canvas
import util
import sys
import requests
import json


def create_instance(API_URL, API_KEY):
    try:
        canvas = Canvas(API_URL, API_KEY)
        util.print_success("Token Valid: {}".format(str(canvas.get_user("self"))))
        return canvas
    except Exception as e:
        util.print_error("\nInvalid Token: {}\n{}".format(API_KEY, str(e)))
        sys.exit(1)
        # raise


def _get_course(canvas_obj, course_id):
    """
    Get Canvas course using canvas object from canvasapi
    Parameters:
        course (Canvas): canvasapi instance
        course_id (int): Canvas course ID
    Returns:
        canvasapi.course.Course object
    """
    try:
        course = canvas_obj.get_course(course_id)
        util.print_success(f"Entered id: {course_id}, Course: {course.name}.")
    except Exception:
        util.shut_down(
            f"ERROR: Could not find course [ID: {course_id}]. Please check course id."
        )

    return course

def _get_request(AUTH_HEADER, API_URL, URL_REQUEST, JSON_FIELD):
    """ Gets Canvas data using standard request call (instead of 
        canvasapi call, when not available). Handles pagination. Returns json.
    """


    results = []

    try:     
        url = "{}/api/v1/{}".format(API_URL, URL_REQUEST)
        print(url)
        response = requests.get(url, headers=AUTH_HEADER, params={'per_page':50})
        
        data = json.loads(response.text).get(JSON_FIELD)
        for i in data:
            results.append(i)
                
        while response.links["current"]["url"] != response.links["last"]["url"]:
            response = requests.get(response.links["next"]["url"], headers=AUTH_HEADER, params={'per_page':50})
                
            data = json.loads(response.text).get(JSON_FIELD)
            for i in data:
                results.append(i)
        
        return(results)
        
    except Exception as se:
        print(f'error {se}')