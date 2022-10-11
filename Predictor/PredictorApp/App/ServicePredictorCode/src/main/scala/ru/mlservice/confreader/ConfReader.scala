package ru.mlservice.confreader

import ReaderModel._
import io.circe.Json
import io.circe.yaml.parser
import scala.io.Source

object ConfReader {

  def getConfigInfo(path: String): Option[ConfigFile] = {
    val buffer = Source.fromFile(path)
    val file   = buffer.mkString
    buffer.close()

    val jsonFile = parser.parse(file).toOption

    def extractValue(jsonOpt: Option[Json], value: String) =
      for {
        value <- jsonOpt.flatMap(json => json.findAllByKey(value).headOption)
      } yield value.asString.fold(value.toString)(identity)

    for {
      appName             <- extractValue(jsonFile, "app_name")
      master              <- extractValue(jsonFile, "master")
      checkpointLocation  <- extractValue(jsonFile, "checkpoint_location")
      kafkaHost           <- extractValue(jsonFile, "host")
      kafkaPort           <- extractValue(jsonFile, "port")
      kafkaTopic          <- extractValue(jsonFile, "topic")
      classifierModelPath <- extractValue(jsonFile, "classifier_model_path")
      regressionModelPath <- extractValue(jsonFile, "regression_model_path")
      dbHost              <- extractValue(jsonFile, "db_host")
      dbPort              <- extractValue(jsonFile, "db_port")
      dbUser              <- extractValue(jsonFile, "db_username")
      dbPassword          <- extractValue(jsonFile, "db_password")
      dbKeyStore          <- extractValue(jsonFile, "db_key_store")
      dbTableName         <- extractValue(jsonFile, "db_table_name")
      endPoint            <- extractValue(jsonFile, "end_point")
      accessKey           <- extractValue(jsonFile, "access_key")
      secretKey           <- extractValue(jsonFile, "secret_key")

    } yield ConfigFile(
      Spark(appName, master, checkpointLocation),
      Kafka(kafkaHost, kafkaPort, kafkaTopic),
      SparkML(classifierModelPath, regressionModelPath),
      Cassandra(dbHost, dbPort, dbUser, dbPassword, dbKeyStore, dbTableName),
      StoreS3(endPoint, accessKey, secretKey)
    )
  }
}
