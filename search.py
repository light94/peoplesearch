import ezodf
from xgoogle.search import GoogleSearch, SearchError
from urllib2 import Request,urlopen,HTTPError,URLError
from socket import error as SocketError
import time
from httplib import IncompleteRead,BadStatusLine


spreadsheet = ezodf.opendoc('probablementors.ods')
sheet = spreadsheet.sheets[0]
spreadsheet2 = ezodf.opendoc('probablementors2.ods')
sheet2 = spreadsheet2.sheets[0]
rows = sheet.nrows()
columns = sheet.ncols()
last_searched = 1
with open('last_searched.txt','r') as f:
	
	last_searched = int(f.read())


	
row = 0

def encode(data):
	return data.encode('utf-8','ignore')
 

def search():
	for row in range(last_searched,rows):
		with open('last_searched.txt','w') as f:
			f.write(str(row))	
		print row
		if sheet[row,0].value !=None or sheet[row,1].value !=None or sheet[row,3].value !=None and she:
			if sheet[row,3].value in ["Alumni","Entrepreneurship","Spring","Kshitij","Gopali"] or sheet[row,4].value in ["Student","Core","Member","Team"]:
				print "Probably a Random Student"
				continue

			if type(sheet[row,0].value)!= unicode :
				sheet[row,0].set_value("")
			if type(sheet[row,1].value)!= unicode :
				sheet[row,1].set_value("")
			if type(sheet[row,3].value)!= unicode :
				sheet[row,3].set_value("")		 
 
			data = sheet[row,0].value+" "+sheet[row,1].value+" "+sheet[row,3].value
			print data
			searchterm1  = encode(data) + " IIT Kharagpur"
			searchterm2 = "Indian Institute"+ encode(data)
			searchterm2 = "Kharagpur" + encode(data) 
			try :
				g1 = GoogleSearch(searchterm1)
				
				#g3 = GoogleSearch(searchterm3)
				g1.results_per_page = 10
				
				#g3.results_per_page = 10
				results1 = g1.get_results()
				
				#results3 = g3.get_results()
				status = 0
				for res in results1[:2]:
					time.sleep(1)
					
					if True:#"linkedin" not in res.url.encode("utf8"): 
						answer = search_for_kgp(res.url.encode("utf8"))
						# sheet2[row,5].set_value("Kgpian")
						if answer == 1:
							print " Kgpian"
							status = 1
							sheet2[row,6].set_value(res.url.encode("utf8"))
							break
				if status==0:
					try:
						g2 = GoogleSearch(searchterm2)
						g2.results_per_page = 10
						results2 = g2.get_results()
						for res in results2[:2]:
							time.sleep(1)
							if True:#"linkedin" not in res.url.encode("utf8"): 
								answer = search_for_kgp(res.url.encode("utf8"))
					# sheet2[row,5].set_value("Kgpian")
								if answer == 1:
									print  " Kgpian"
									status = 1
									sheet2[row,6].set_value(res.url.encode("utf8"))
									break
					except SearchError, e :
						with open("error.txt",'a') as f:
							f.write(data + "\n")
					except HTTPError:
						print "Oops"
					except URLError:
						print "Start again"
						with open("error.txt",'a') as f:
							f.write(data + "\n")
					except SocketError:
						with open("error.txt",'a') as f:
							f.write(data + "\n")
					except ValueError:
						with open("error.txt",'a') as f:
							f.write(data + "\n")
					except IncompleteRead:
						with open("error.txt",'a') as f:
							f.write(data + "\n")
					except BadStatusLine:
						with open("error.txt",'a') as f:
							f.write(data + "\n")





							
				if status == 0:	
					print  " Probably Not Kgpian"
				spreadsheet2.save()
			except SearchError, e :
				with open("error.txt",'a') as f:
					f.write(data + "\n")
			except HTTPError:
				print "Oops"	
			except URLError:
				print "Start again"
				with open("error.txt",'a') as f:
					f.write(data + "\n")
			except SocketError:
				with open("error.txt",'a') as f:
					f.write(data + "\n")
			except ValueError:
				with open("error.txt",'a') as f:
					f.write(data + "\n")
			except IncompleteRead:
				with open("error.txt",'a') as f:
					f.write(data + "\n")
			except BadStatusLine:
				with open("error.txt",'a') as f:
					f.write(data + "\n")
		
				
				
			# webpage = urllib2.urlopen(res.url.encode("utf8")).read()
			# if "Kharagpur" in webpage:
			# 	print "He is a Kgpian"
				


def search_for_kgp(url):
	req = Request(url,headers = {'User-Agent': 'Mozilla/5.0'})
	webpage =  urlopen(req).read()
	if "Kharagpur" in webpage:
		
		return 1
	else:
		return 0





if __name__ == "__main__":
	search()

	spreadsheet2.save()
	#search_for_kgp()
