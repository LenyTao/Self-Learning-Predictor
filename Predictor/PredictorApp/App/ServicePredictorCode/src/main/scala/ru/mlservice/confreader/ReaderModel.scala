package ru.mlservice.confreader

object ReaderModel {

  case class Spark(appName: String, master: String, checkpointLocation: String)
  case class Kafka(host: String, port: String, topic: String)
  case class SparkML(classifierModelPath: String, regressionModelPath: String)
  case class Cassandra(
      host: String,
      port: String,
      username: String,
      password: String,
      keyStore: String,
      tableName: String
  )
  case class StoreS3(
      endPoint: String,
      accessKey: String,
      secretKey: String
  )

  case class ConfigFile(
      spark: Spark,
      kafka: Kafka,
      sparkML: SparkML,
      cassandra: Cassandra,
      storeS3: StoreS3
  )
}
