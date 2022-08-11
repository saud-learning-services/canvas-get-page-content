from helpers import create_instance
import os
from dotenv import load_dotenv
import sys
from util import shut_down
import pandas as pd
import readtime

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

def create_page_readtime_df(canvas, course_id, WPM):
    """ Creates a dataframe that includes page, 
        module_item, module info and readtime
    """
    
    course = canvas.get_course(course_id)
    
    pages_df, pages_list = _get_page_info_rt(course, WPM)
    pages_info_df, pages_info_list = _get_page_item_details(course)
    
    df = pages_df.merge(pages_info_df, on='page_url', how='left')
    return(df)

def __get_item_detail(item):
    """ Extracts module item information if is a page
    """
    
    item_type = item.get('type')
    
    if item_type == 'Page':
        item_id = item.get('id')
        item_title = item.get('title')
        item_url = item.get('html_url')
        page_url = item.get('page_url')
        item_position = item.get('position')
        
        return({'item_id': item_id,
               'item_title': item_title,
               'page_url': page_url,
               'item_url': item_url,
               'item_position': item_position})

def _get_page_item_details(course): 
    """ Iterating through all modules and module items gets
        page info of module item
    """
    
    modules = course.get_modules(include='items')
    page_info_list = []

    for i in modules:

        mod = i.__dict__
        module_info = {'module_id': mod.get('id'),
                      'module_name': mod.get('name'),
                      'module_published': mod.get('published'),
                      'module_position': mod.get('position')}

        module_items = mod.get('items')

        if module_items:

            for j in module_items:

                page_detail = __get_item_detail(j)

                if page_detail:
                    page_detail.update(module_info)
                    page_info_list.append(page_detail)
        
    return(pd.DataFrame(page_info_list), page_info_list)
        
def _get_page_info_rt(course, WPM=None):
    """ Gets information from all pages in Canvas course and 
        calculated readtime.
        
        Optional - WPM (if none, uses package standard of 265 WPM)
    """
     
    pages = course.get_pages()
    page_ids = [i.__dict__.get('page_id') for i in pages]

    page_dicts = []

    for i in page_ids:
        page = course.get_page(i).__dict__
        page_body = page.get('body')
        
        if page_body:

            try:
                page_readtime = readtime.of_html(page_body, wpm=WPM)
                page_readtime_secs = page_readtime.seconds

            except Exception as e:
                page_readtime = None
                page_readtime_secs = None

            new_dict = {'page_id': i,
                        'page_html_url': page.get('html_url'),
                        'page_url': page.get('url'),
                        'page_published': page.get('published'),
                        'page_title': page.get('title'),
                        'page_readtime': page_readtime,
                        'page_readtime_secs': page_readtime_secs,
                        'page_body': page.get('body')}

            page_dicts.append(new_dict)
        
    return(pd.DataFrame(page_dicts), page_dicts)

def main():
    canvas = create_instance(API_URL, API_KEY)
    course_id = get_course_id()

    WPM = 200
    df = create_page_readtime_df(canvas, course_id, WPM)
    df.to_csv(f"{course_id}_pageinfo.csv", index=False)

    


if __name__ == "__main__":
    main()
