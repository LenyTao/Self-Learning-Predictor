package ru.mlservice.sparkapp

import org.apache.spark.ml.PipelineModel
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions.{ col, from_json }
import ru.mlservice.confreader.ReaderModel.ConfigFile

object PipelineML {

  def run(config: ConfigFile): Unit = {

    val spark = SparkSession.builder
      .appName(config.spark.appName)
      .master(config.spark.master)
      .config("spark.cassandra.connection.host", config.cassandra.host)
      .config("spark.cassandra.connection.port", config.cassandra.port)
      .config("spark.cassandra.auth.username", config.cassandra.username)
      .config("spark.cassandra.auth.password", config.cassandra.password)
      .getOrCreate

    spark.sparkContext.hadoopConfiguration.set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    spark.sparkContext.hadoopConfiguration.set("fs.s3a.path.style.access", "true")
    spark.sparkContext.hadoopConfiguration.set("fs.s3a.endpoint", config.storeS3.endPoint)
    spark.sparkContext.hadoopConfiguration.set("fs.s3a.access.key", config.storeS3.accessKey)
    spark.sparkContext.hadoopConfiguration.set("fs.s3a.secret.key", config.storeS3.secretKey)

    val df = spark.readStream
      .format("kafka")
      .option("kafka.bootstrap.servers", s"${config.kafka.host}:${config.kafka.port}")
      .option("subscribe", config.kafka.topic)
      .load()

    val classifierModel: PipelineModel = PipelineModel.read.load(config.sparkML.classifierModelPath)
    val regressionModel: PipelineModel = PipelineModel.read.load(config.sparkML.regressionModelPath)

    val eventDF =
      df.select(from_json(col("value").cast("string"), SchemaML.eventSchema).alias("event"))
        .select("event.*")
        .select("*")

    val classifierDF =
      classifierModel
        .transform(eventDF)
        .withColumnRenamed("prediction", "classifier_prediction")

    val regressionDF = regressionModel
      .transform(
        classifierDF.select(
          "id_event",
          "sex",
          "patient_type",
          "intubed",
          "pneumonia",
          "age",
          "pregnancy",
          "diabetes",
          "copd",
          "asthma",
          "inmsupr",
          "hypertension",
          "other_disease",
          "cardiovascular",
          "obesity",
          "renal_chronic",
          "tobacco",
          "contact_other_covid",
          "covid_res",
          "icu",
          "entry_date",
          "date_symptoms",
          "name",
          "classifier_prediction"
        )
      )
      .withColumnRenamed("prediction", "regression_prediction")

    val resultDF = regressionDF
      .select(
        "id_event",
        "sex",
        "patient_type",
        "intubed",
        "pneumonia",
        "age",
        "pregnancy",
        "diabetes",
        "copd",
        "asthma",
        "inmsupr",
        "hypertension",
        "other_disease",
        "cardiovascular",
        "obesity",
        "renal_chronic",
        "tobacco",
        "contact_other_covid",
        "covid_res",
        "icu",
        "entry_date",
        "date_symptoms",
        "name",
        "classifier_prediction",
        "regression_prediction"
      )

    resultDF.writeStream
      .option("checkpointLocation", config.spark.checkpointLocation)
      .outputMode("append")
      .foreach(new CassandraSink(spark, config))
      .start()

    spark.streams.awaitAnyTermination()
  }
}
