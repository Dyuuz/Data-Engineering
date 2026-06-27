from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").getOrCreate()

data = [
    (1, "purchase", 100),
    (1, "purchase", 50),
    (2, "click", 0)
]

df = spark.createDataFrame(data, ["user_id", "event", "amount"])