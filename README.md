
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
