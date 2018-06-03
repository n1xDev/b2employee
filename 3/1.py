import json, pg
from urllib.request import urlopen

def DoScan(user_1id, user_2id, second):
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
		except:
			excepts += 1
	print("coincidence: " + str(coincidence) + " (from: " + user_1id + ")")
	print("coincidence name: " + str(coincidence_str))
	print("excepts: " + str(excepts))
	if second == "0":
		Scanner(user_2id, user_1id, "1")

def DoSort():
	connection = pg.connect(dbname='info_db', host='localhost', user='postgres', passwd='givemehack')
	res = connection.query("SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';").getresult()
	i = 0
	for i in range(0, len(res)):
		print(str(res[i][1]))

def Main():
	#Scanner("1", "1092", "0")
	"""connection = pg.connect(dbname='info_db', host='localhost', user='postgres', passwd='givemehack')
	found_id = -1
	try:
		while i < 20000: 
		vals = connection.query("select * from ").getresult()
	except:
		print("table with user(" + str(found_id) + ") is not found")
	Scanner("107394388", "210064990", "0")"""
	DoSort()
	print("Done.")

Main()