FROM adoptopenjdk/openjdk8

#Setup Minimal tool SET
RUN apt-get update && apt-get install -y curl vim wget nano
RUN echo exit 0 > /usr/sbin/policy-rc.d

#Setup Python
RUN apt-get install -y python3 python3-pip python-dev postgresql-server-dev-all
RUN update-alternatives --install "/usr/bin/python" "python" "$(which python3)" 1

#Create dir for App
RUN mkdir -p /usr/src/app

RUN mkdir -p /usr/src/app/mlflow

#Copy program to dir
COPY . /usr/src/app

#Set dir for Run
WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

#Run App
CMD ["bash","run_mlflow.sh"]