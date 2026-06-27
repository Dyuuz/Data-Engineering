from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").getOrCreate()

data = [
    (1, "purchase", 100),
    (1, "purchase", 50),
    (2, "click", 0)
]

df = spark.createDataFrame(data, ["user_id", "event", "amount"])

# Action: show dataframe
df.show()

# Transformation: filter purchases
purchases = df.filter(df.event == "purchase")

# Transformation: aggregate revenue
result = purchases.groupBy("user_id").sum("amount")