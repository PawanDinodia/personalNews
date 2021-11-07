import sqlite3
import json

def getCats():
	conn1 = sqlite3.connect("webUpdates/webUpdates.db")
	crsr1 = conn1.cursor()
	query = "SELECT updateCatagory, updateCatagoryTitle, sum(markNew) FROM webUpdates GROUP BY updateCatagory;"
	cats=crsr1.execute(query).fetchall();
	conn1.close();
	return json.dumps(cats)

def getUpdate(cat_id):
	contents={"updateCatagoryTitle":"","sites":[],"subcats":[],"dat":[]}
	sites_list=[]
	subcats_list=[]
	total_dat={}

	conn1 = sqlite3.connect("webUpdates/webUpdates.db")
	crsr1 = conn1.cursor()

	query4 = "SELECT DISTINCT updateCatagoryTitle FROM webUpdates WHERE updateCatagory='"+cat_id+"';"
	catTitle=crsr1.execute(query4).fetchall()[0]
	
	query = "SELECT * FROM webUpdates WHERE updateCatagory='"+cat_id+"' AND delFlag!=1;"
	all_selected_update=crsr1.execute(query).fetchall();
	
	query1 = "SELECT DISTINCT updateUrl FROM webUpdates WHERE updateCatagory='"+cat_id+"' AND delFlag!=1;"
	sites=crsr1.execute(query1).fetchall()

	for site in sites:
		sites_list.append(site[0])
		query2 = "SELECT DISTINCT updateSubCatagory, updateSubUrl FROM webUpdates WHERE updateUrl='"+site[0]+"' AND delFlag!=1;"
		sub_cats=crsr1.execute(query2).fetchall()
		# print("__________________________________________________")
		# print(sub_cats[1])
		# print("__________________________________________________")
		for sub_cat in sub_cats:
			subcats_list.append([sub_cat[0],sub_cat[1]])
			query3 = "SELECT * FROM webUpdates WHERE updateSubCatagory = '"+sub_cat[0]+"' AND delFlag!=1;"
			dat=crsr1.execute(query3).fetchall()
			total_dat["{}".format(sub_cat[0])]=dat
	contents["updateCatagoryTitle"]=catTitle
	contents["sites"]=sites_list
	contents["subcats"]=subcats_list
	contents["dat"]=total_dat
	conn1.close();
	return json.dumps(contents)

def starrChange(status,updateId):
	conn1 = sqlite3.connect("webUpdates/webUpdates.db")
	crsr1 = conn1.cursor()
	query1 = "UPDATE webUpdates SET setImportant="+status+" WHERE updateId="+updateId+";"
	crsr1.execute(query1)
	conn1.commit()
	conn1.close()
	return json.dumps("oka")

def updateMark(status,updateId):
	conn1 = sqlite3.connect("webUpdates/webUpdates.db")
	crsr1 = conn1.cursor()
	query1 = "UPDATE webUpdates SET markNew="+status+" WHERE updateId="+updateId+";"
	crsr1.execute(query1)
	conn1.commit()
	conn1.close()
	return json.dumps("oka")
def delFlagOn(updateId):
	conn1 = sqlite3.connect("webUpdates/webUpdates.db")
	crsr1 = conn1.cursor()
	query1 = "UPDATE webUpdates SET delFlag=1, markNew=0, setImportant=0 WHERE updateId="+updateId+";"
	crsr1.execute(query1)
	conn1.commit()
	conn1.close()
	return json.dumps("oka")