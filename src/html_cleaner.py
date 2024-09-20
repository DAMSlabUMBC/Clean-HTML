import logging
 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

try:
    from bs4 import BeautifulSoup, Comment
except:
    logger.error("could not import bs4 lib")

html_file = 'AmazonHTML0.html'
folder = 'html'

html_doc = None
html_doc_orig_len = 0
try:
    with open(f'../{folder}/{html_file}', 'r', encoding='utf-8') as html:
        logger.info('found html document')
        html_doc = html.read()
        html_doc_orig_len = len(html_doc)
        logger.info(f"original length of html document: {html_doc_orig_len}")
except:
    logger.error("could not find html document")


parser = BeautifulSoup(html_doc, 'html.parser')
scripts = parser.find_all("script")
unwanted_tags = [
    'meta', 'script', 'style', 'link', 'form', 'input', 
    'button','select', 'textarea', 'img', 'video', 'audio'
]

for unwanted_tag in unwanted_tags:
    logger.info(f"removing {unwanted_tag} tag")
    for tag in parser.find_all(unwanted_tag):
        tag.decompose()

logger.info(f'removing all attributes and comments')
for tag in parser.find_all(True):
    tag.attrs.clear()
for comment in parser.find_all(string=lambda text: isinstance(text, Comment)):
    comment.extract()

modified_html = parser.prettify()
try:
    with open(f'../{folder}/AmazonHTML0_cleaned.html', 'w', encoding='utf-8') as html_file:
        html_file.write(modified_html)
        logger.info("wrote html document to file")
except:
    logger.error("could not write reduced html document to file")
logger.info(f'original html document size: {html_doc_orig_len} tokens')
logger.info(f'modified html document size: {len(modified_html)} tokens')
logger.info(f'reduced html document size by {html_doc_orig_len - len(modified_html)} tokens')








