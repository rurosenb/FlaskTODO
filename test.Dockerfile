FROM python
RUN python -m pip install --upgrade pip
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN pip install requests
CMD ["python", "testserver.py"]