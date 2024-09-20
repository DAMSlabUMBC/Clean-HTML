import logging
import argparse
import os
import sys
import json

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

try:
    from bs4 import BeautifulSoup, Comment
except:
    logger.error("could not import bs4 lib")

absolute_path = os.path.abspath(sys.argv[0]) ### idk might be useful later
argument_parser = argparse.ArgumentParser(description="cli to clean unwanted information from html files")
argument_parser.add_argument('html_file_folder', type=str, help='path to html')
argument_parser.add_argument('clean_html_file_folder', type=str, help='path to cleaned html')
argument_parser.add_argument(
    '--configuration', type=str, help='path to json configuration file', default=f''
)
args = argument_parser.parse_args()

### extracted arguments
html_file_path = args.html_file_folder
cleaned_html_file_path = args.clean_html_file_folder
json_configuration_file = args.configuration

### attributes defined in our json configuration files
### below are default values
unwanted_tags = []
remove_comments = True
remove_attrs = True

### non-empty file, then set the attributes based on value in json config 
if json_configuration_file != '':
    json_config = None
    try:
        with open(json_configuration_file, 'r', encoding='utf-8') as file:
            json_config = json.load(file)
            if 'remove_comments' in json_config:
                if json_config['remove_comments'] == "true":
                    remove_comments = True
                else:
                    remove_comments = False
            if 'remove_attributes' in json_config:
                if json_config['remove_attributes'] == "true":
                    remove_attrs = True
                else:
                    remove_attrs = False            
            if 'unwanted_tags' in json_config:
                unwanted_tags = json_config['unwanted_tags']
    except:
        logger.error("json configuration file could not be loaded")
        sys.exit(1)

html_doc = None
html_doc_orig_len = 0
try:
    ### read in entire html document
    with open(html_file_path, 'r', encoding='utf-8') as html:
        logger.info('found html document')
        html_doc = html.read()
        
except:
    logger.error("could not find html document")
    sys.exit(1)

parser = BeautifulSoup(html_doc, 'html.parser')
html_doc_orig_len = len(parser.prettify())
### store the original length of the document
logger.info(f"original length of html document: {html_doc_orig_len}")

### This portion of the code actually modifies our html document
if len(unwanted_tags):
    for unwanted_tag in unwanted_tags:
        logger.info(f"removing {unwanted_tag} tag")
        for tag in parser.find_all(unwanted_tag):
            tag.decompose()

if remove_attrs:
    logger.info(f'removing all attributes')
    ### erase every tags attributes
    for tag in parser.find_all(True):
        tag.attrs.clear()

if remove_comments:
    logger.info(f'removing all comments')
    ### removes comments, not sure how the lambda works, I found it on stackoverflow
    for comment in parser.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()


### read in the reduced html document and write to a file
modified_html = parser.prettify()
try:
    with open(cleaned_html_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(modified_html)
        logger.info("wrote html document to file")
except:
    logger.error("could not write reduced html document to file")
    sys.exit(1)
logger.info(f'original html document size: {html_doc_orig_len} tokens')
logger.info(f'modified html document size: {len(modified_html)} tokens')
logger.info(f'reduced html document size by {html_doc_orig_len - len(modified_html)} tokens')








