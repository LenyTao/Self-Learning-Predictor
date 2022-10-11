import time
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json
from pyspark.sql import functions as spark_function

import ConfReader
import schema


def main():
    config: dict = ConfReader.get_config_info("./")
    time.sleep(30)

    kafka_host = config["kafka"]["host"]
    kafka_port = config["kafka"]["port"]
    kafka_end_point = f"{kafka_host}:{kafka_port}"

    spark: SparkSession = SparkSession \
        .builder \
        .appName(config["spark"]["app_name"]) \
        .master(config["spark"]["master"]) \
        .getOrCreate()

    df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", kafka_end_point) \
        .option("subscribe", config["kafka"]["topic"]) \
        .load()

    training_data_df = df.select(
        from_json(spark_function.col("value").cast("string"), schema.get_warehouse_schema()).alias("event")
    ).select("event.*")

    training_data_df.writeStream \
        .outputMode("append") \
        .format("parquet") \
        .partitionBy("entry_date") \
        .option("compression", "snappy") \
        .option("path", config["data_warehouse"]["training_data_path"]) \
        .option("checkpointLocation", config["checkpoint"]["path"]) \
        .start()

    spark.streams.awaitAnyTermination()


if __name__ == '__main__':
    main()
