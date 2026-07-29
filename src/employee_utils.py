

from pyspark.sql.functions import col, upper

def clean_names(df):
    return df.withColumn(
        "EmployeeName",
        upper(col("EmployeeName"))
    )

def filter_salary(df):
    return df.filter(
        col("Salary") > 50000
    )

def calculate_bonus(df):
    return df.withColumn(
        "Bonus",
        col("Salary") * 0.10
    )
     