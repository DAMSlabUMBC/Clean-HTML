### Clean-HTML
Clean-HTML is a simple command-line utility to take in a source html document and remove unwanted contents from it.
For example, perhaps we want to remove each script tag from the document, or every img and style tag. By reducing its size,
we query LLMs with lower cost.

#### How to use
usage: `python html_cleaner.py [-h] [--configuration CONFIGURATION] html_file_folder clean_html_file_folder`
```
positional arguments:
  html_file_folder        filepath to html
  clean_html_file_folder  filepath to cleaned html

options:
  -h, --help                     show this help message and exit
  --configuration CONFIGURATION  path to json configuration file
```

Required packages in are requirements.txt

example usage with json configuration:
`python .\html_cleaner.py --configuration ../config/default.json C:\Users\srach\Projects\Clean-HTML\html\AmazonHTML0.html C:\Users\srach\Projects\Clean-HTML\html\AmazonHTML0_cleaned.html`

example usage without  json configuration:
`python .\html_cleaner.py C:\Users\srach\Projects\Clean-HTML\html\AmazonHTML0.html C:\Users\srach\Projects\Clean-HTML\html\AmazonHTML0_cleaned.html `



#### Attributes we supported so far 
In our json configuration, specifiy the following attributes.
1. remove_comments -> if True comments are removed 
2. remove_attributes -> if True the attributes of every tag are gone
3. unwanted_tags -> an array of html tags, every instance of a tag in this array will be removed from the html document

If these attributes are not specified, the program will give them default values

example json file:
{
    "remove_comments": "true",
    "remove_attributes": "true",
    "unwanted_tags": [
        "meta", "script", "style", "link", "form", "input", 
        "button","select", "textarea", "img", "video", "audio"
    ]
}

#### example program output
`python .\html_cleaner.py --configuration ../config/default.json C:\Users\srach\Projects\Clean-HTML\html\AmazonHTML0.html C:\Users\srach\Projects\Clean-HTML\html\AmazonHTML0_cleaned.html`

```
2024-09-20 18:15:58,767 - INFO - found html document
2024-09-20 18:15:59,170 - INFO - original length of html document: 1659897
2024-09-20 18:15:59,170 - INFO - removing meta tag
2024-09-20 18:15:59,170 - INFO - removing script tag
2024-09-20 18:15:59,180 - INFO - removing style tag
2024-09-20 18:15:59,180 - INFO - removing link tag
2024-09-20 18:15:59,188 - INFO - removing form tag
2024-09-20 18:15:59,195 - INFO - removing input tag
2024-09-20 18:15:59,197 - INFO - removing button tag
2024-09-20 18:15:59,197 - INFO - removing select tag
2024-09-20 18:15:59,203 - INFO - removing textarea tag
2024-09-20 18:15:59,204 - INFO - removing img tag
2024-09-20 18:15:59,204 - INFO - removing video tag
2024-09-20 18:15:59,204 - INFO - removing audio tag
2024-09-20 18:15:59,211 - INFO - removing all attributes
2024-09-20 18:15:59,221 - INFO - removing all comments
2024-09-20 18:15:59,286 - INFO - wrote html document to file
2024-09-20 18:15:59,286 - INFO - original html document size: 1659897 tokens
2024-09-20 18:15:59,286 - INFO - modified html document size: 222205 tokens
2024-09-20 18:15:59,286 - INFO - reduced html document size by 1437692 tokens
```