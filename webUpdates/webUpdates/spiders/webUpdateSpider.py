import scrapy
from ..items import WebupdatesItem
from datetime import datetime

class WebUpdateSpider(scrapy.Spider):
	name="webUpdates"
	start_urls=["https://cdsco.gov.in/opencms/opencms/en/Medical-Device-Diagnostics/Medical-Device-Diagnostics/","https://nehu.ac.in/announcement","https://nehu.ac.in/event","https://nehu.ac.in/news-archive","https://nehu.ac.in/vacancy","https://recruitment.nhsrcindia.org/my/job"]
	# start_urls=["https://nehu.ac.in/vacancy","https://recruitment.nhsrcindia.org/my/job"]


#updateSubCatagory should be unique within catagory------without_spaces
#updateCatagory should be unique within catagory------without_spaces
#updateCatagoryTitle Try to keep it unique
	def parse(self, response):
		items=WebupdatesItem()
		# updates from cdsco website
		items["updateUrl"]=response.url.split("/")[2]
		if (items["updateUrl"]=="cdsco.gov.in"):
			items["updateSubUrl"]=response.url
			items["updateFound"]=datetime.today().strftime("%d-%b-%Y")
			items["markNew"]=1
			items["setImportant"]=0
			items["updateCatagory"]="medical_device_cdsco"
			items["updateCatagoryTitle"]="Medical devices (cdsco.gov.in)"
			tabs=response.css("div.tab-content")
			tab1_rows=tabs.css("#tab1 table tbody tr")
			for rw in tab1_rows:
				items["updateTitle"]=rw.css("td::text").extract()[1]
				items["updateDates"]=rw.css("td::text").extract()[2]
				items["updateSubCatagory"]="medical_device_alerts"
				items["updateLink"]="https://{}{}".format(items["updateUrl"],rw.css("td")[3].css("a::attr(href)").extract()[0])
				yield items
			tab2_rows=tabs.css("#tab2 table tbody tr")
			for rw in tab2_rows:
				items["updateTitle"]=rw.css("td::text").extract()[1]
				items["updateDates"]=rw.css("td::text").extract()[2]
				items["updateSubCatagory"]="medical_device_news_cdsco"
				items["updateLink"]="https://{}{}".format(items["updateUrl"],rw.css("td")[3].css("a::attr(href)").extract()[0])
				yield items
			tab3_rows=tabs.css("#tab3 table tbody tr")
			for rw in tab3_rows:
				items["updateTitle"]=rw.css("td::text").extract()[1]
				items["updateDates"]=rw.css("td::text").extract()[2]
				items["updateSubCatagory"]="cdsco_public_notice"
				items["updateLink"]="https://{}{}".format(items["updateUrl"],rw.css("td")[3].css("a::attr(href)").extract()[0])
				yield items
			tab4_rows=tabs.css("#tab4 table tbody tr")
			for rw in tab4_rows:
				items["updateTitle"]=rw.css("td::text").extract()[1]
				items["updateDates"]=rw.css("td::text").extract()[2]
				items["updateSubCatagory"]="cdsco_gazette_notification"
				items["updateLink"]="https://{}{}".format(items["updateUrl"],rw.css("td")[3].css("a::attr(href)").extract()[0])
				yield items
		elif (items["updateUrl"]=="nehu.ac.in"):
			items["updateSubUrl"]=response.url
			items["updateFound"]=datetime.today().strftime("%d-%b-%Y")
			items["markNew"]=1
			items["setImportant"]=0
			items["updateCatagory"]="university_updates"
			items["updateCatagoryTitle"]="University (nehu.ac.in)"
			if(response.url.split("/")[3]=="announcement"):
				announcements=response.css(".right-divider ol li");
				for announcement in announcements:
					items["updateTitle"]=announcement.css("a::text").extract()[0]
					items["updateDates"]=announcement.css("span::text").extract()[0]
					items["updateSubCatagory"]="nehu_announcements"
					items["updateLink"]=announcement.css("a::attr(href)").extract()[0]
					yield items
			elif(response.url.split("/")[3]=="event"):
				dates=response.css(".clearfix .col-md-9 h4::text").extract()
				cur_event=0;
				for date in dates:
					events=response.css(".clearfix .col-md-9 table")[cur_event].css("tr");
					for event in events:
						items["updateTitle"]=event.css("td")[1].css("a::text").extract()[0]
						items["updateDates"]="{} {}".format(event.css("td")[0].css("span b::text").extract()[0],date)
						items["updateSubCatagory"]="nehu_events"
						items["updateLink"]=event.css("td")[1].css("a::attr(href)").extract()[0]
						yield items
					cur_event=cur_event+1;
			elif(response.url.split("/")[3]=="news-archive"):
				news=response.css(".right-divider h3");
				dates=response.css(".right-divider p");
				cur_event=0
				for news_update in news:
					items["updateTitle"]=news_update.css("a::text").extract()[0]
					items["updateDates"]=dates[cur_event*3].css(".news-pubdate::text").extract()[0]
					items["updateSubCatagory"]="news_update"
					items["updateLink"]=news_update.css("a::attr(href)").extract()[0]
					cur_event=cur_event+1
					yield items
			elif(response.url.split("/")[3]=="vacancy"):
				items["updateSubUrl"]=response.url
				items["updateFound"]=datetime.today().strftime("%d-%b-%Y")
				items["markNew"]=1
				items["setImportant"]=0
				items["updateCatagory"]="jobs"
				items["updateCatagoryTitle"]="Jobs"
				vacancies=response.css(".right-divider ol li");
				for vacancy in vacancies:
					items["updateTitle"]=vacancy.css("a::text").extract()[0]
					items["updateDates"]=vacancy.css("code::text").extract()[0]
					items["updateSubCatagory"]="nehu_jobs"
					items["updateLink"]=vacancy.css("a::attr(href)").extract()[0]
					# print("----------------------------------------------------")
					# print(items)
					# print("----------------------------------------------------")
					yield items
		elif (items["updateUrl"]=="recruitment.nhsrcindia.org"):
			items["updateSubUrl"]=response.url
			items["updateFound"]=datetime.today().strftime("%d-%b-%Y")
			items["markNew"]=1
			items["setImportant"]=0
			items["updateCatagory"]="jobs"
			items["updateCatagoryTitle"]="Jobs"
			vacancies=response.css("table.table tbody tr");
			for vacancy in vacancies:
				print("----------------------------------------------------")
				print(vacancy.css("td").extract())
				print("----------------------------------------------------")
				items["updateTitle"]=vacancy.css("td")[1].css("span::text").extract()[0]
				items["updateDates"]=vacancy.css("td")[2].css("span::text").extract()[0]
				items["updateSubCatagory"]="nhsrc_jobs"
				items["updateLink"]="{}{}".format(response.url,vacancy.css("td")[4].css("a::attr(href)").extract()[0])
				yield items