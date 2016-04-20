'''
Created on 11-03-2016

@author: Pablo Cruz Navea
'''
import MySQLdb

class SQLDBService (object):
    @staticmethod
    def insertTemporaryEncounter(description, source):
        db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="moai",         # your username
                     passwd="moai1234",  # your password
                     db="moai_test")        # name of the data base

        # you must create a Cursor object. It will let
        #  you execute all the queries you need
        cur = db.cursor()
        
        insertEncounterSQL = "INSERT INTO encuentro_temporal (descripcion, fuente, fecha_obtencion, hora_obtencion) VALUES ('%s', '%s', CURDATE(), CURTIME())" % (description, source)

        # Use all the SQL you like
        try:
            cur.execute(insertEncounterSQL)
            db.commit()
        except:
            db.rollback()
        
        # print all the first cell of all the rows
#        for row in cur.fetchall():
#        print row[2]
    
        db.close()