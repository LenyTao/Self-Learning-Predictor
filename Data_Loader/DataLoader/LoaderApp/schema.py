from pyspark.sql.types import StructType, StringType, IntegerType, StructField, DoubleType


def get_warehouse_schema() -> StructType:
    return StructType([
        StructField("id_event", StringType(), True),
        StructField("sex", DoubleType(), True),
        StructField("patient_type", DoubleType(), True),
        StructField("entry_date", StringType(), True),
        StructField("date_symptoms", StringType(), True),
        StructField("death", DoubleType(), True),
        StructField("intubed", DoubleType(), True),
        StructField("pneumonia", DoubleType(), True),
        StructField("age", DoubleType(), True),
        StructField("pregnancy", DoubleType(), True),
        StructField("diabetes", DoubleType(), True),
        StructField("copd", DoubleType(), True),
        StructField("asthma", DoubleType(), True),
        StructField("inmsupr", DoubleType(), True),
        StructField("hypertension", DoubleType(), True),
        StructField("other_disease", DoubleType(), True),
        StructField("cardiovascular", DoubleType(), True),
        StructField("obesity", DoubleType(), True),
        StructField("renal_chronic", DoubleType(), True),
        StructField("tobacco", DoubleType(), True),
        StructField("contact_other_covid", DoubleType(), True),
        StructField("covid_res", DoubleType(), True),
        StructField("icu", DoubleType(), True)
    ]
    )
