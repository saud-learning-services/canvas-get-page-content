
# Canvas Get Page Content
> WIP! Questions? Ask Alison - alison.myers@sauder.ubc.ca

## Summary
This script will extract Canvas page html, and module / item information associated with a given page (if any) for an entire Canvas course. The predicted read time of each page is also provided, using the [readtime](https://pypi.org/project/readtime/) project.

## Input

> Input is entered as terminal arguments: {COURSE_ID} {WPM}
- Canvas course id
- Optional: words per minute for the read time calculaton
  
## Output

### {COURSE_ID}_pageinfo.csv


Column | Description | Note
---------|----------|---------
 page_id | The Canvas Page ID | Not the same as module_item_id
 page_html_url | The full url to the given page | 
 page_url | The page url extension | In Canvas, this is designated by the title of the page (will change if page title changes)
 page_published | Boolean - whether the page is published |
 page_title | The page title |
 page_readtime | The estimated readtime of the page (rounded to minute, minimum 1 minute) | Calculation from [readtime](https://pypi.org/project/readtime/) with either default or given Words per Minute
 page_readtime_secs | The estimated readtime of the page in seconds | Calculation from [readtime](https://pypi.org/project/readtime/) with either default or given Words per Minute
 page_body | The html of the page |
 item_id | If the page is a Canvas item, the item id, otherwise empty | A Canvas item (module item) is a page that is part of a module
 item_title | If the page is a Canvas item, the title, otherwise empty | Should be the same as the page_title 
 item_url | If the page is a Canvas item, the url, otherwise empty |  The item_url uses the item_id in the url
 item_position | The position of the page within a module | 
 module_id | The module id of the associated module | Must be a Canvas item to have a module id
 module_published | Boolean - whether the module is published |
 module_position | The position of the module (relative to other modules) |

 > In Canvas a "page" can be associated with a module, when this is the case there are additional associations with the page - it is now also a module item and has module information. 

## Getting Started

#### First Time

1. Ensure you have [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) installed (Python 3.9 version)
2. Clone **{canvas-get-page-content}** repository
3. Import environment (once): `$ conda env create -f environment.yml`
4. Create .env file and include:

Note - anything in {SQUIGLY BRACES} means you must use your own values
```
API_TOKEN = {MY API TOKEN}
API_INSTANCE = {MY INSTANCE}
```

Example instance = 'https://ubc.instructure.com'

#### Every Time

1. Run:
   1. navigate to your directory `$ cd {YOUR_PATH}/canvas-get-page-content`
   1. activate the environment (see step 3 on first run) `$ conda activate canvas-get-page-content`
   1. run the script and follow prompts in terminal `$ python src/get_page_content.py {COURSE_ID} {WPM - optional}`
   
   > When you run the script, you need to enter the course id as an input, and you can enter a new words per minute (standard is set at 265) if desired.
   > -  i.e) if my course id is 99999, and I want to use a words per minute of 200
   >     - `$ python src/get_page_content.py 99999 200`
   > - i.e) if my course id is 900, but I want to use the default words per minute
   >     - `$ python src/get_page_content.py 900`

---

## ✨ Acknowledgements ✨

I want to thank and acknowledge the [contributors](https://github.com/alanhamlett/readtime/blob/master/AUTHORS) to [readtime](https://pypi.org/project/readtime/), which this project uses to calculate page read time! 
