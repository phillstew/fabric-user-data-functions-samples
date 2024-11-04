# This sample allows you to read data from Azure SQL database 
# Complete these steps before testing this funtion 
#   1. Select Manage connections to connect to Azure SQL database 
#   2. Copy the Alias name and replace it in line 6 

@app.connection("sqlDB",alias="<alias for azure sql database>")
@app.function("read_from_azure_sql_db")
def read_from_azure_sql_db(sqlDB: udf.FabricSqlConnection)->str:
    # Replace with the query you want to run
      query = "SELECT * FROM (VALUES ('John Smith', 31), ('Kayla Jones', 33)) AS Employee(EmpName, DepID);"
  
      # Establish a connection to the SQL database
      connection = sqlDB.connect(connection_string)
      cursor = connection.cursor()
  
      # Execute the query
      cursor.execute(query)
  
      # Fetch all results
      results = []
      for row in cursor.fetchall():
          results.append(row)
  
      # Close the connection
      cursor.close()
      connection.close()  
      resultsJSON = json.dumps({"values": results})          
      return results
  

