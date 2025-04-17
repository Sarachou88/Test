# Import packages
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Retreives the existing session called "InterviewExample" or create a new session if not found
spark = SparkSession.builder.appName("InterviewExample").getOrCreate()

# Define the data
data = [
    ("Alice", 28),
    ("Bob", 35),
    ("Cathy", 22)
]

# Transform the data into a Dataframe
df = spark.createDataFrame(data, ["name", "age"])

# Filter users older than 25
filtered_df = df.filter(col("age") > 30)

# Print the output of the filtered table 
# --> Lazy evaluation (only apply filter if .show() or .collect())
filtered_df.show()
