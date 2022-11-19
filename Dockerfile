FROM python:3.8.2
ADD . /work
WORKDIR /work
RUN pip install -r requirements.txt
CMD ["python", "/work/run.py"]