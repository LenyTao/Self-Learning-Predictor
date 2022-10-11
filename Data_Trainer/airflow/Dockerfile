FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev zsh curl git locales nano iputils-ping openjdk-8-jdk
RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV TZ=Europe/Samara

RUN apt-get install -y wget

COPY requirements.txt /root/requirements.txt
RUN python3 -m pip install -r /root/requirements.txt

#Add Jars for Spark
RUN wget -P ./usr/local/lib/python3.10/dist-packages/pyspark/jars https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.2.0/hadoop-aws-3.2.0.jar
RUN wget -P ./usr/local/lib/python3.10/dist-packages/pyspark/jars https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.11.375/aws-java-sdk-bundle-1.11.375.jar

COPY data_trainer_app /trainer_app

RUN airflow db init

RUN airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin

COPY airflow.cfg /root/airflow/airflow.cfg

CMD (airflow scheduler &) && airflow webserver


