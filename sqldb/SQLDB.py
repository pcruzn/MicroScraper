'''
Created on 11-03-2016

@author: Pablo Cruz Navea
'''
import MySQLdb

class SQLDBService (object):
    @staticmethod
    def storeTemporaryEncounter(description, source):
        db = MySQLdb.connect(host="localhost",
                     user="moai",
                     passwd="moai1234",
                     db="moai_test")


        cur = db.cursor()
        
        storeEncounterSQL = "INSERT INTO encuentro_temporal (descripcion, fuente, fecha_obtencion, hora_obtencion) VALUES ('%s', '%s', CURDATE(), CURTIME())" % (description, source)

        try:
            cur.execute(storeEncounterSQL)
            db.commit()
            db.close()
            status = 0
        except:
            db.rollback()
            db.close()
            status = 2

        return status