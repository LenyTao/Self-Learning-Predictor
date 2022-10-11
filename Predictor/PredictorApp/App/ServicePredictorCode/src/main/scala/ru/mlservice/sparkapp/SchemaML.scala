package ru.mlservice.sparkapp

import org.apache.spark.sql.types.{ DoubleType, StringType, StructType }

object SchemaML {
  val eventSchema: StructType = new StructType()
    .add("id_event", StringType)
    .add("sex", DoubleType)
    .add("patient_type", DoubleType)
    .add("intubed", DoubleType)
    .add("pneumonia", DoubleType)
    .add("age", DoubleType)
    .add("pregnancy", DoubleType)
    .add("diabetes", DoubleType)
    .add("copd", DoubleType)
    .add("asthma", DoubleType)
    .add("inmsupr", DoubleType)
    .add("hypertension", DoubleType)
    .add("other_disease", DoubleType)
    .add("cardiovascular", DoubleType)
    .add("obesity", DoubleType)
    .add("renal_chronic", DoubleType)
    .add("tobacco", DoubleType)
    .add("contact_other_covid", DoubleType)
    .add("covid_res", DoubleType)
    .add("icu", DoubleType)
    .add("entry_date", StringType)
    .add("date_symptoms", StringType)
    .add("name", StringType)
}
