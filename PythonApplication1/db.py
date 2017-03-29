import mysql.connector

class db:

    def __init__(self, query):
         try:
          cnx = mysql.connector.connect(user='root',
                                        password='',
                                        database='real link')
         except mysql.connector.Error as err:
             if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
             elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
             else:
                print(err)
         else:
            cursor = cnx.cursor()
            
            cursor.execute(query)
  
            for (id, jobID, sentence) in cursor:
                   print("{}, {}, {}".format(
                   jobID, id, sentence)) 

            cursor.close()
            cnx.close()