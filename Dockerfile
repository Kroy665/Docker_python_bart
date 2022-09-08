FROM python:3.7.2

# Create app directory 
WORKDIR /usr/src/app 

COPY . .
ENV DATABASE_API=http://localhost:1337
RUN python -m pip install --upgrade pip


RUN pip install pipreqs
RUN pipreqs . --force
RUN sh install.sh
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 6000
CMD [ "python3", "./index.py" ]     