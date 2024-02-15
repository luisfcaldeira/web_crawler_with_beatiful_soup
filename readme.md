# web crawler 
I created this application to run on the website www.folha.com.br, so you may need make adjustments. 

## Where the heck are requirements.txt
You can run this project withot installing packages, because it'll install any dependence by itself. It's that why that I didn't have make any requirements.txt

## venv
It's strongly recomended you create a virtual enviroment

## rules
You can create rules in your code by passing a dictionary to the Scrapper object with the parameters 'contains' or 'pattern'. The 'pattern' parameter is used for regular expressions. See ```main.py``` for examples.