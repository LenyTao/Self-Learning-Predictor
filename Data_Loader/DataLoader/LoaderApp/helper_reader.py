from pyspark.sql import SparkSession

import ConfReader

config: dict = ConfReader.get_config_info("./")
spark: SparkSession = SparkSession \
    .builder \
    .appName("Reader") \
    .master("local[*]") \
    .getOrCreate()

spark.read.parquet(
    config["data_warehouse"]["training_data_path"]
).show()
