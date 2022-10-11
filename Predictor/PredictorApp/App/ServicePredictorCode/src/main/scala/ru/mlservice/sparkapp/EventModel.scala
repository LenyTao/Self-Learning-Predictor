package ru.mlservice.sparkapp

case class EventModel(
    idEvent: String,
    sex: Double,
    patientType: Double,
    intubed: Double,
    pneumonia: Double,
    age: Double,
    pregnancy: Double,
    diabetes: Double,
    copd: Double,
    asthma: Double,
    inmsupr: Double,
    hypertension: Double,
    otherDisease: Double,
    cardiovascular: Double,
    obesity: Double,
    renalChronic: Double,
    tobacco: Double,
    contactOtherCovid: Double,
    covidRes: Double,
    icu: Double,
    entryDate: String,
    dateSymptoms: String,
    name: String,
    classifierPrediction: Double,
    regressionPrediction: Double
)
