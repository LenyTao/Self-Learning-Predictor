package ru.mlservice

import ru.mlservice.confreader.ConfReader
import ru.mlservice.sparkapp.PipelineML

object PredictorApp {

  def main(args: Array[String]): Unit = {

    val config = args match {
      case _ if args.length != 0 => ConfReader.getConfigInfo(args.head)
      case _                     => ConfReader.getConfigInfo("./ml-service/src/main/resources/config.yaml")
    }

    PipelineML.run(config.get)

  }
}
