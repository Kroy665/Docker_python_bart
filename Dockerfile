# FROM python:3.7.2

# WORKDIR /usr/src/app
# RUN pip install pipreqs
# RUN pipreqs . --force
# # COPY requirements.txt ./
# RUN python -m pip install --upgrade pip
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .
# EXPOSE 5000
# CMD [ "python3", "./index.py" ]


FROM python:3.7.2

# Create app directory 
WORKDIR /usr/src/app 

    
RUN git clone https://github.com/Kroy665/Docker_python_bart.git
RUN cd Docker_python_bart;ls -al; mv * .* ../;ls -al;

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD [ "python3", "./index.py" ]            
                