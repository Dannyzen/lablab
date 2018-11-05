from string import Template
from sys import argv

def echo_template(app):
    tempy = Template('From python:2-alpine \n RUN pip install flask requests \n ADD $app / \n ENTRYPOINT ["python", "/$app"]')
    return (tempy.substitute(app=app))
	
print(echo_template(argv[1]))
