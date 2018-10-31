From python:2-alpine

RUN pip install flask requests
ADD calcPrice.py / 
ENTRYPOINT [python /calcPrice.py]
