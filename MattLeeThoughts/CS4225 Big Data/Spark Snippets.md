#snippets 

Google Collab examples
 =
https://colab.research.google.com/drive/18vqsZcie3UdlLiw-UGXw_LHnZVCcw4et
https://colab.research.google.com/drive/1wU8YLVInZWbPXFV7ozXwEswpPojS-uGw#scrollTo=jXoaoWGq_6Km
https://colab.research.google.com/drive/12b4NY-3JNiJHNvM-Lf7DU_w-fl1YG62A#scrollTo=GTzBHgWwrCkI

Documentation
 = 
https://spark.apache.org/docs/2.2.0/sql-programming-guide.html

Setup Spark on Colab
 = 
```Python
#region SNIPPET
<snippet><content><![CDATA[
# Setup Spark
# ===============
# install java
!apt-get install openjdk-8-jdk-headless -qq > /dev/null

# install spark (change the version number if needed)
!wget -q https://archive.apache.org/dist/spark/spark-3.0.0/spark-3.0.0-bin-hadoop3.2.tgz

# unzip the spark file to the current folder
!tar xf spark-3.0.0-bin-hadoop3.2.tgz

# set your spark folder to your system path environment. 
import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-3.0.0-bin-hadoop3.2"

# install findspark using pip
!pip install -q findspark
import findspark
findspark.init()
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").getOrCreate()
]]></content><tabTrigger>spark-setup</tabTrigger>
<scope>source.python</scope></snippet>
#endregion
```

Reading a file
 = 
 `spark.read`. See https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html
 
Example:
```python
df = spark.read.option('header', True).csv("network.csv").repartition(5).cache()

pd = df.toPandas()
```
 
 Querying the Spark dataframe / dataset / RDD
  =
 You can call the Spark API to query the data (note the distinction between transformations and actions. See [[Resilient Distributed Datasets]])
```python
df.filter(~df.value.startswith('alpha>')) \
  .filter(~df.value.contains('beta')) \
  .filter(df.value.contains('Invalid user')) \
  .toPandas()
 ```

A concise example can be found at:
https://spark.apache.org/docs/2.2.0/sql-programming-guide.html#untyped-dataset-operations-aka-dataframe-operations

A complete list of API can be found at:
https://spark.apache.org/docs/2.2.0/api/scala/index.html#org.apache.spark.sql.Dataset

 You can also use SQL
 ```python
from pyspark.sql.functions import *
df.createOrReplaceTempView('dfview')

spark.sql("CREATE OR REPLACE TEMPORARY VIEW v1 AS SELECT DISTINCT dst FROM dfview WHERE int(day) % 7 != 0")

spark.sql("SELECT dst FROM dfview WHERE dst NOT IN (SELECT * FROM v1) GROUP BY dst HAVING COUNT(DISTINCT src) == 13").show()
```