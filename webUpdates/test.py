import sqlite3

conn=sqlite3.connect("webUpdates.db")
crsr=conn.cursor()
query="SELECT * FROM webUpdates WHERE updateTitle='Medical Devices Alert on MiniMed 620G Insulin Pump/Pump Kits & MiniMed 640G Insulin Pump/Pump kit of India Medtronic Ltd' and updateDates='2021-Oct-11' and updateLink='https://cdsco.gov.in/opencms/opencms/system/modules/CDSCO.WEB/elements/download_file_division.jsp?num_id=Nzc3MA=='"
 # WHERE updateTitle='Medical Devices Alert on MiniMed 620G Insulin Pump/Pump Kits & MiniMed 640G Insulin Pump/Pump kit of India Medtronic Ltd' and updateDates='2021-Oct-11' and updateLink='https://cdsco.gov.in/opencms/opencms/system/modules/CDSCO.WEB/elements/download_file_division.jsp?num_id=Nzc3MA=='
results=crsr.execute(query).fetchall();
print(results[0][4])