FROM python
RUN python -m pip install --upgrade pip
WORKDIR /app
COPY ./testserver.py .
RUN pip install requests
CMD ["python", "testserver.py"]