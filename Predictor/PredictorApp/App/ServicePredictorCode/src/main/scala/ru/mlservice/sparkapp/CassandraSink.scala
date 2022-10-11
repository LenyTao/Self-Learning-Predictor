package ru.mlservice.sparkapp

import com.datastax.spark.connector.cql.CassandraConnector
import org.apache.spark.sql.{ForeachWriter, Row, SparkSession}
import ru.mlservice.confreader.ReaderModel.ConfigFile

class CassandraSink(spark: SparkSession, config: ConfigFile) extends ForeachWriter[org.apache.spark.sql.Row] {

  val connector: CassandraConnector = CassandraConnector(spark.sparkContext.getConf)

  override def open(partitionId: Long, epochId: Long): Boolean = {
    println(
      s"""
         |Cassandra connection on:
         |<${connector.conf.contactInfo.endPointStr().replaceAll("[{}]", "")}>
         |was OPEN
         |""".stripMargin
    )
    true
  }

  override def process(value: Row): Unit = {
    val event = EventModel(
      value.getString(0),
      value.getDouble(1),
      value.getDouble(2),
      value.getDouble(3),
      value.getDouble(4),
      value.getDouble(5),
      value.getDouble(6),
      value.getDouble(7),
      value.getDouble(8),
      value.getDouble(9),
      value.getDouble(10),
      value.getDouble(11),
      value.getDouble(12),
      value.getDouble(13),
      value.getDouble(14),
      value.getDouble(15),
      value.getDouble(16),
      value.getDouble(17),
      value.getDouble(18),
      value.getDouble(19),
      value.getString(20),
      value.getString(21),
      value.getString(22),
      value.getDouble(23),
      value.getDouble(24)
    )
    connector.withSessionDo { session =>
      session.execute(
        s"""
           |INSERT INTO ${config.cassandra.keyStore}.${config.cassandra.tableName}(
           |id_event ,
           |sex ,
           |patient_type ,
           |intubed ,
           |pneumonia ,
           |age ,
           |pregnancy ,
           |diabetes ,
           |copd ,
           |asthma ,
           |inmsupr ,
           |hypertension ,
           |other_disease ,
           |cardiovascular ,
           |obesity ,
           |renal_chronic ,
           |tobacco ,
           |contact_other_covid ,
           |covid_res ,
           |icu ,
           |entry_date ,
           |date_symptoms ,
           |name,
           |classifier_prediction ,
           |regression_prediction 
           |)
           |VALUES (
           |'${event.idEvent}',
           |${event.sex},
           |${event.patientType},
           |${event.intubed},
           |${event.pneumonia},
           |${event.age},
           |${event.pregnancy},
           |${event.diabetes},
           |${event.copd},
           |${event.asthma},
           |${event.inmsupr},
           |${event.hypertension},
           |${event.otherDisease},
           |${event.cardiovascular},
           |${event.obesity},
           |${event.renalChronic},
           |${event.tobacco},
           |${event.contactOtherCovid},
           |${event.covidRes},
           |${event.icu},
           |'${event.entryDate}',
           |'${event.dateSymptoms}',
           |'${event.name}',
           |${event.classifierPrediction},
           |${event.regressionPrediction}
           |);
           |""".stripMargin
      )
    }
    println("Data was send to Cassandra")
  }

  override def close(errorOrNull: Throwable): Unit =
    println(
      s"""
         |Cassandra connection on:
         |<${connector.conf.contactInfo.endPointStr().replaceAll("[{}]", "")}> 
         |was CLOSE
         |""".stripMargin
    )
}
