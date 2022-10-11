FROM adoptopenjdk/openjdk8

#Setup Minimal tool SET
RUN apt-get update && apt-get install -y curl vim wget nano
RUN echo exit 0 > /usr/sbin/policy-rc.d

#Add Dependencies for PySpark
RUN apt-get install -y python3 python3-pip 
RUN update-alternatives --install "/usr/bin/python" "python" "$(which python3)" 1

#Create dir for App
RUN mkdir -p /usr/src/app

#Copy program to dir
COPY ./FlaskApp /usr/src/app

#Ser dir for Run
WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt


#Run App
CMD ["python","app.py"]