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

    # 6317333b268c7dc032748df4
RUN git clone https://github.com/Kroy665/Docker_python_bart.git
RUN cd Docker_python_bart;ls -al; mv * .* ../;ls -al;


RUN git clone http://20.237.181.230:7005/p-6317333b268c7dc032748df4.git
RUN cd p-6317333b268c7dc032748df4;ls -al; mv * .* ../modules;ls -al;
RUN python -m pip install --upgrade pip

RUN pip install pipreqs
RUN pipreqs . --force
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD [ "python3", "./index.py" ]            
                