import json, pg
from urllib.request import urlopen

f = open("coincidence.txt", "w")

def DoScan(user_1id, user_2id, second):
	if user_1id == user_2id:
		return
	connection = pg.connect(dbname='info_db', host='localhost', user='postgres', passwd='givemehack')
	res1, res2 = "", ""
	try:
		#res1 = connection.query("select * from u" + str(user_1id)).getresult()
		res1 = connection.query("select * from " + str(user_1id)).getresult()
		res2 = connection.query("select * from " + str(user_2id)).getresult()
	except:
		print("one of these peoples is not found in database...")
	coincidence = 0
	coincidence_str = []
	excepts = 0
	i = 0
	for i in range(0, len(res1)):
		try:
			for j in range(0, len(res2)):
				if res1[i][0] == res2[j][0]:
					coincidence += 1
					coincidence_str.append(str(res1[i][1]))
					f.write(user_1id + " - " + user_2id + "\n")
		except:
			excepts += 1
	print("coincidence: " + str(coincidence) + " (" + user_1id + " and " + user_2id + ")")
	print("coincidence name: " + str(coincidence_str))
	print("excepts: " + str(excepts))
	if second == "0":
		DoScan(user_2id, user_1id, "1")

def DoSort():
	connection = pg.connect(dbname='info_db', host='localhost', user='postgres', passwd='givemehack')
	res = connection.query("SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';").getresult()
	i = 0
	j = 0
	for i in range(0, len(res)):
		#print(str(res[i][1]))
		while j < len(res):
			DoScan(str(res[i][1]), str(res[j][1]), "0")
			i += 1

def Main():
	DoSort()
	print("Done.")
	f.close()

Main()