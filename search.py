import ezodf
from xgoogle.search import GoogleSearch, SearchError
import urllib2
import time

spreadsheet = ezodf.opendoc('probablementors.ods')
sheet = spreadsheet.sheets[0]
spreadsheet2 = ezodf.opendoc('probablementors2.ods')
sheet2 = spreadsheet2.sheets[0]
rows = sheet.nrows()
columns = sheet.ncols()

def encode(data):
	return data.encode('ascii','ignore')


def search():
	for row in range(1,rows):
		print row
		if sheet[row,0].value !=None or sheet[row,1].value !=None or sheet[row,3].value !=None:
		

			if type(sheet[row,0].value)!= unicode :
				sheet[row,0].set_value("")
			if type(sheet[row,1].value)!= unicode :
				sheet[row,1].set_value("")
			if type(sheet[row,3].value)!= unicode :
				sheet[row,3].set_value("")		 
 
			data = sheet[row,0].value+" "+sheet[row,1].value+" "+sheet[row,3].value
		
			searchterm  = encode(data)
			try :
				g = GoogleSearch(searchterm)
				g.results_per_page = 10
				results = g.get_results()
				i = 5
				for res in results[:2]:
					print res.url.encode("utf8")
					sheet2[row,i].set_value(res.url.encode("utf8"))
					i = i+1
				spreadsheet2.save()
			except SearchError, e :
				with open("error.txt",'a') as f:
					f.write(data + "\n")


				
				
			# webpage = urllib2.urlopen(res.url.encode("utf8")).read()
			# if "Kharagpur" in webpage:
			# 	print "He is a Kgpian"
				


def search_for_kgp():
	for row in range(1,rows):
		for i in range(2):
			url = sheet2[row,(i+5)].value
			print url 
			if url!= None:
				webpage = urllib2.urlopen(url).read()
				if "Kharagpur" in webpage:
					sheet[row,7].set_value("Kgpian")
					spreadsheet.save()
					print "Kgpian"
					break		

if __name__ == "__main__":
	# search()
	# spreadsheet2.save()
	search_for_kgp()