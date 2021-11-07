# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class WebupdatesPipeline:
	def __init__(self):
		self.createConnection()

	def createConnection(self):
		self.conn = sqlite3.connect("webUpdates.db")
		self.crsr = self.conn.cursor()
		query='''CREATE TABLE IF NOT EXISTS webUpdates ('updateId' INTEGER,'updateUrl' TEXT,'updateCatagory' TEXT,'updateCatagoryTitle' TEXT,'updateTitle' TEXT,'updateFound' TEXT,'updateDates' TEXT,'updateSubCatagory' TEXT,'updateLink' TEXT,"markNew"	INTEGER,"setImportant" INTEGER,"delFlag" INTEGER ,"updateSubUrl" TEXT,PRIMARY KEY("updateId" autoincrement));'''
		self.crsr.execute(query)
		self.conn.commit();

	def process_item(self, item, spider):
		try:
			similar_updates=self.crsr.execute("SELECT * FROM webUpdates WHERE updateTitle=? and updateDates=? and updateLink=?;",(item["updateTitle"],item["updateDates"],item["updateLink"])).fetchall()
		except:
			print("error")
		if(not len(similar_updates)>0):
			self.crsr.execute("""INSERT INTO webUpdates (updateUrl,updateCatagory,updateCatagoryTitle,updateTitle,updateFound,updateDates,updateSubCatagory,updateLink,markNew,setImportant,delFlag,updateSubUrl) values (?,?,?,?,?,?,?,?,?,?,?,?);""",(item["updateUrl"], item["updateCatagory"], item["updateCatagoryTitle"], item["updateTitle"], item["updateFound"], item["updateDates"], item["updateSubCatagory"], item["updateLink"], item["markNew"], item["setImportant"],0, item["updateSubUrl"]));
			self.conn.commit()
		return item