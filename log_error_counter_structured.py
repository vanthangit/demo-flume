from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, count

spark = SparkSession.builder \
    .appName("LogErrorCounterStructured") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Đọc stream từ Kafka
df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "log_topic") \
    .option("startingOffsets", "earliest") \
    .load()

# Lấy value và chuyển thành string
lines = df.select(col("value").cast("string"))

# Lọc lỗi 404
error_count = lines.filter(col("value").contains("404 Not Found")) \
    .agg(count("*").alias("count"))

query = error_count.writeStream \
    .outputMode("complete") \
    .format("console") \
    .trigger(processingTime="5 seconds") \
    .start()


query.awaitTermination()
