# Databricks notebook source
#read file from DBFS folder
df = spark.read.csv("/FileStore/tables/1800.csv").toDF("a","b","c","d","e","f","g","h")
df.show()

# COMMAND ----------

