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
		if sheet[row,0].value !=None and sheet[row,1].value !=None and sheet[row,3].value !=None:
 
			data = sheet[row,0].value+" "+sheet[row,1].value+" "+sheet[row,3].value
		
			searchterm  = encode(data)
			try :
				g = GoogleSearch(searchterm)
				g.results_per_page = 10
				results = g.get_results()
				i = 5
				for res in results[:10]:
					print res.url.encode("utf8")
					sheet2[row,i].set_value(res.url.encode("utf8"))
					i =+ 1
				spreadsheet2.save()
			except SearchError, e :
				with open("error.txt",'a') as f:
					f.write(data)


				
				
			# webpage = urllib2.urlopen(res.url.encode("utf8")).read()
			# if "Kharagpur" in webpage:
			# 	print "He is a Kgpian"
				
	

if __name__ == "__main__":
	search()
	spreadsheet2.save()