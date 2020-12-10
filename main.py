
from datetime import datetime
from bbdd import sql_connection, sql_table, sql_insert
from speed_test import speedTest

def main():

    con = sql_connection()
    sql_table(con)

    results_dict = speedTest()

    #print(results_dict)

    print("#"*50)
    print("Bajada: "+str(results_dict["download"]/1000000))
    print("Subida: "+str(results_dict["upload"]/1000000))
    print("Tiempo de ping: "+str(results_dict["ping"]))
    print("lat: "+str(results_dict["server"]["lat"]))
    print("lon: "+str(results_dict["server"]["lon"]))
    print("Ciudad: "+results_dict["server"]["name"])
    print("Pais: "+results_dict["server"]["country"])
    print("latencia: "+str(results_dict["server"]["latency"]))
    print("IP: "+results_dict["client"]["ip"])
    print("ISP: "+results_dict["client"]["isp"])
    print("#"*50)

    data = (results_dict["download"]/1000000,\
            results_dict["upload"]/1000000,\
            results_dict["ping"],\
            results_dict["server"]["lat"],\
            results_dict["server"]["lon"],\
            results_dict["server"]["name"],\
            results_dict["server"]["country"],\
            results_dict["server"]["latency"],\
            results_dict["client"]["ip"],\
            results_dict["client"]["isp"],\
            datetime.now())

    sql_insert(con, data)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("Error %s" % e)

#respuesta = json.dumps(results_dict)
#data = json.load(respuesta)
#print (data["download"])
