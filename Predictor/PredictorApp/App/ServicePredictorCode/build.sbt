name := "ServicePredictor"

version := "0.1"

scalaVersion := "2.12.12"

val spark              = "3.0.3"
val log4j              = "1.7.30"
val kafkaClient        = "3.0.0"
val commonsPool        = "2.11.1"
val circe              = "0.14.1"
val cassandraConnector = "3.0.0"
val javaAws            = "1.11.375"
val hadoopAws          = "3.2.0"

libraryDependencies += "org.apache.spark"   %% "spark-core"                      % spark % "provided"
libraryDependencies += "org.apache.spark"   %% "spark-sql"                       % spark % "provided"
libraryDependencies += "org.apache.spark"   %% "spark-streaming"                 % spark % "provided"
libraryDependencies += "org.apache.spark"   %% "spark-mllib"                     % spark % "provided"
libraryDependencies += "org.apache.kafka"   % "kafka-clients"                    % kafkaClient
libraryDependencies += "org.apache.commons" % "commons-pool2"                    % commonsPool
libraryDependencies += "org.apache.spark"   %% "spark-sql-kafka-0-10"            % spark % "provided"
libraryDependencies += "org.apache.spark"   %% "spark-token-provider-kafka-0-10" % spark % "provided"
libraryDependencies += "com.datastax.spark" %% "spark-cassandra-connector"       % cassandraConnector
libraryDependencies += "io.circe"           %% "circe-yaml"                      % circe
libraryDependencies += "org.slf4j"          % "slf4j-log4j12"                    % log4j
libraryDependencies += "com.amazonaws"      % "aws-java-sdk-bundle"              % javaAws
libraryDependencies += "org.apache.hadoop"  % "hadoop-aws"                       % hadoopAws
