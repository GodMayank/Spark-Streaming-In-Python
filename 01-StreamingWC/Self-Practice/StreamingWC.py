from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, expr

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .appName("StreamingWordCount") \
        .master("local[3]") \
        .config("spark.streaming.stopGracefullyOnShutdown", "true") \
        .config("spark.sql.shuffle.partitions", 3) \
        .getOrCreate()
    
    # Read
    lines_df = spark.readStream \
        .format("text") \
        .option("path", "file:///home/mayank612512/SparkStreaming/input_dir/") \
        .load()

    # Transform
    words_df = lines_df.select(expr("explode(split(value, ' ')) as word"))

    counts_df = words_df.groupBy("word").count()

    #Sink
    word_count_query = counts_df.writeStream \
        .format("console") \
        .outputMode("complete") \
        .option("checkpointLocation", "file:///home/mayank612512/SparkStreaming/check-point-dir") \
        .start()

    word_count_query.awaitTermination()

    spark.stop()