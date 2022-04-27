

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

if __name__ == "__main__":

    sc = SparkContext(appName="PythonStreamingNetworkWordCount")
    sc.setLogLevel("ERROR")
    ssc = StreamingContext(sc, 1)

    lines = ssc.socketTextStream("localhost", 9008)
    lines.pprint()
    counts = lines.flatMap(lambda line: line.split(" "))\
                  .map(lambda word: (word, 1))\
                  .reduceByKey(lambda a, b: a+b)
    # counts.pprint()

    ssc.start()
    ssc.awaitTermination()
