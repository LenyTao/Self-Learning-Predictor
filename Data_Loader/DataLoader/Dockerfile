FROM adoptopenjdk/openjdk8

#Setup Minimal tool SET
RUN apt-get update && apt-get install -y curl vim wget nano
RUN echo exit 0 > /usr/sbin/policy-rc.d

#Add Dependencies for PySpark
RUN apt-get install -y python3 python3-pip 
RUN update-alternatives --install "/usr/bin/python" "python" "$(which python3)" 1

#Add Jars for Spark-Streamig and Kafka 
RUN wget -P ./usr/local/lib/python3.8/dist-packages/pyspark/jars https://repo1.maven.org/maven2/org/apache/commons/commons-pool2/2.11.1/commons-pool2-2.11.1.jar
RUN wget -P ./usr/local/lib/python3.8/dist-packages/pyspark/jars https://repo1.maven.org/maven2/org/apache/spark/spark-token-provider-kafka-0-10_2.12/3.0.3/spark-token-provider-kafka-0-10_2.12-3.0.3.jar
RUN wget -P ./usr/local/lib/python3.8/dist-packages/pyspark/jars https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/3.0.0/kafka-clients-3.0.0.jar
RUN wget -P ./usr/local/lib/python3.8/dist-packages/pyspark/jars https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.0.3/spark-sql-kafka-0-10_2.12-3.0.3.jar

#Create dir for App
RUN mkdir -p /usr/src/app

#Copy program to dir
COPY ./LoaderApp /usr/src/app

#Ser dir for Run
WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

#Run App
CMD ["python","app.py"]