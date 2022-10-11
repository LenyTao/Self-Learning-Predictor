import math
import os
import shutil
from datetime import datetime

import mlflow
from pyspark.ml import Pipeline
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator, RegressionEvaluator
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler
from pyspark.ml.regression import DecisionTreeRegressor
from pyspark.sql import SparkSession

from config.reader.ConfigClass import ConfigFile


def run(config: ConfigFile):
    # Указываем расположение mlflow трекера
    mlflow.set_tracking_uri(config.ml_flow.tracking_uri)

    # Задаём имя эксперимента
    mlflow.set_experiment(config.ml_flow.experiment_name)

    currency_date = (str(datetime.now().strftime('%Y-%m-%d_%H%M%S')))

    model_name = f"{config.ml_flow.model_name}_{currency_date}"

    # Запускаем эксперимент
    with mlflow.start_run():
        spark: SparkSession = SparkSession \
            .builder \
            .appName(config.spark.app_name) \
            .master(config.spark.master) \
            .getOrCreate()

        raw_covid_df = \
            spark \
                .read \
                .parquet(config.spark_ml.training_data_path)

        clear_covid_df = raw_covid_df.drop("id", "entry_date", "date_symptoms")

        # Превращаем строки в числа
        indexer = StringIndexer(
            inputCols=[
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
                "icu"],
            outputCols=[
                "sexIndex",
                "patient_typeIndex",
                "intubedIndex",
                "pneumoniaIndex",
                "ageIndex",
                "pregnancyIndex",
                "diabetesIndex",
                "copdIndex",
                "asthmaIndex",
                "inmsuprIndex",
                "hypertensionIndex",
                "other_diseaseIndex",
                "cardiovascularIndex",
                "obesityIndex",
                "renal_chronicIndex",
                "tobaccoIndex",
                "contact_other_covidIndex",
                "covid_resIndex",
                "icuIndex"
            ]
        )

        # Энкодируем колонки в двоичные вектора
        encoder = OneHotEncoder(
            inputCols=indexer.getOutputCols(),
            outputCols=[
                "sexEnc",
                "patient_typeEnc",
                "intubedEnc",
                "pneumoniaEnc",
                "ageEnc",
                "pregnancyEnc",
                "diabetesEnc",
                "copdEnc",
                "asthmaEnc",
                "inmsuprEnc",
                "hypertensionEnc",
                "other_diseaseEnc",
                "cardiovascularEnc",
                "obesityEnc",
                "renal_chronicEnc",
                "tobaccoEnc",
                "contact_other_covidEnc",
                "covid_resEnc",
                "icuEnc"
            ]
        )

        # Создаём Feature вектор
        assembler = VectorAssembler(
            inputCols=encoder.getOutputCols(),
            outputCol="features")

        # Cоздаём тестовые данные

        test_data = clear_covid_df

        # Создаём тренера для Classifier Tree Model
        trainer_classifier = DecisionTreeClassifier().setLabelCol("death").setFeaturesCol("features")

        # Создаём тренера для Regression Tree Model
        trainer_regression = DecisionTreeRegressor().setLabelCol("death").setFeaturesCol("features")

        # Создаём 2 пайплайна обучения моделей

        learning_classifier_pipeline = Pipeline(stages=[indexer, encoder, assembler, trainer_classifier])
        learning_regression_pipeline = Pipeline(stages=[indexer, encoder, assembler, trainer_regression])

        # Получаем наши модели

        classifier_model = learning_classifier_pipeline.fit(clear_covid_df)
        regression_model = learning_regression_pipeline.fit(clear_covid_df)

        # Осуществляем тестовый прогон для определения точности

        classifier_prediction = classifier_model.transform(test_data)
        regression_prediction = regression_model.transform(test_data)

        # Создаём Оценщика Classifier Model
        classifier_evaluator = \
            MulticlassClassificationEvaluator() \
                .setLabelCol("death") \
                .setPredictionCol("prediction") \
                .setMetricName("accuracy")

        # Оцениваем Classifier Model
        accuracy = classifier_evaluator.evaluate(classifier_prediction)

        # Создаём Оценщика Regression Model
        regression_evaluator = \
            RegressionEvaluator() \
                .setLabelCol("death") \
                .setPredictionCol("prediction") \
                .setMetricName("rmse")

        # Оцениваем Regression Model

        rmse = regression_evaluator.evaluate(regression_prediction)

        # Наш эксперимент был осуществлён,
        # На основе его были созданы и оценены Regression Model и Classifier Model модели

        artifact_tmp_path = config.ml_flow.artifact_tmp_path

        classifier_tree_file_name = f"DecisionClassifierTree_{currency_date}.txt"

        regression_tree_file_name = f"DecisionRegressionTree_{currency_date}.txt"

        data_example_file_name = f'data_example_{currency_date}.csv'

        os.mkdir(f"{artifact_tmp_path}")

        # Создадим пример данных на которых мы обучались
        clear_covid_df.limit(20).toPandas().to_csv(
            os.path.join(artifact_tmp_path, data_example_file_name),
            header=True,
            index=None,
            sep='\t',
            mode='w')

        # Создадим дерево решений для Classifier Model
        with open(f"{os.path.join(artifact_tmp_path, classifier_tree_file_name)}", "w") as file:
            file.write(classifier_model.stages[3].toDebugString)

        # Создадим дерево решений для Regression Model
        with open(f"{os.path.join(artifact_tmp_path, regression_tree_file_name)}", "w") as file:
            file.write(regression_model.stages[3].toDebugString)

        # Зададим теги в mlflow для удобного поиска подобного рода экспериментов
        mlflow.set_tag("Learning Subject", "Covid")

        # Зададим параметры в mlflow для лучшего понимания результатов экспериментов
        mlflow.log_param('model_name', model_name)

        mlflow.log_param("Regression metrics", "rmse")
        mlflow.log_param("Classifier metrics", "accuracy,%")

        # Зададим метрики в mlflow по результатам нашего эксперимента
        mlflow.log_metric("accuracy", (math.ceil(accuracy * 100)))
        mlflow.log_metric("rmse", rmse)

        # Сохраним необходимые артефакты которые были созданы ранее в mlflow
        mlflow.log_artifact(os.path.join(artifact_tmp_path, classifier_tree_file_name))
        mlflow.log_artifact(os.path.join(artifact_tmp_path, regression_tree_file_name))
        mlflow.log_artifact(os.path.join(artifact_tmp_path, data_example_file_name))

        # Сохраним только что обученные модели в необходимое место для быстрого использования
        mlflow.spark.save_model(
            spark_model=classifier_model,
            path=f"{os.path.join(config.spark_ml.ready_models_path, f'classifier_tree_model_{currency_date}')}"
        )
        mlflow.spark.save_model(
            spark_model=regression_model,
            path=f"{os.path.join(config.spark_ml.ready_models_path, f'regression_tree_model_{currency_date}')}"
        )

        # Сохраним только что обученные модели в сам mlflow для дальнейшей работы с моделью внутри mlflow
        mlflow.spark.log_model(spark_model=classifier_model, artifact_path="my_classifier_model")
        mlflow.spark.log_model(spark_model=regression_model, artifact_path="my_regression_model")

        # Удаляем временную папку для артефактов
        shutil.rmtree(config.ml_flow.artifact_tmp_path)
