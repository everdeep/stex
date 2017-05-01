import sys
import re
import psycopg2

from pyquery import PyQuery as pq
from lxml import etree

links = []

d = pq(url='http://www.asx.com.au/asx/statistics/prevBusDayAnns.do')
table = d('.contenttable')

if len(table) == 0:
	print 'Unable to find the table element'

# get all the announcement links
for column in d('td a'):
	a = pq(url='http://www.asx.com.au' + str(column.attrib['href']))
	count = 0
	for elem in a('form input'):
		if count == 2:
			links.append('http://www.asx.com.au' + elem.attrib['value'])
		count += 1

with open('./assets/data/prevAnnouncements.txt', mode='w+') as outfile:

	count = 0
	index = 0
	for column in d('td'):
		if count == 6:
			outfile.write('\n')
			count = 0

		if count == 5:
			outfile.write(links[index])
			count += 1
			index += 1
			continue

		try:
			temp = str(column.text)
			if temp == 'None':
				count += 1
				continue
			outfile.write(temp + '; ')
		except Exception:
			pass

		count += 1

# # Connect to an existing database
# conn = psycopg2.connect("dbname=stex user=Rush")
#
# # Open a cursor to perform database operations
# cur = conn.cursor()

with open('./assets/data/prevAnnouncements.txt') as infile, open('./sql/inserts.sql', mode='w+') as outfile:
	for line in infile:
		temp = line.split('; ')[2].replace("'", "''")

		outfile.write(
		'''INSERT INTO announcements (code, time_posted, headline, pages, pdf) VALUES ('%s', '%s', '%s', %s, '%s');\n''' %
		(line.split('; ')[0], line.split('; ')[1], temp, line.split('; ')[3], line.split('; ')[4].strip()))
#
# for row_elem in d('#pokedex tbody tr'):
# 	row = []
#
# 	for cell_elem in row_elem:
# 		row.append(re.sub(r'\s+', '', cell_elem.text_content()))
# 	rows.append(row)
#
# pokemons = []
#
# for row in rows:
# 	pokemon = {}
# 	for c, column in enumerate(columns):
# 		pokemon[column] = row[c]
# 	pokemons.append(pokemon)
#
# for dict_elem in pokemons:
# 	count = 0
# 	while count < len(pokemons):
# 		print (dict_elem['Name'])
# 		count += 1
#

# Read here about CSS selectors
# http://cheetyr.com/css-selectors
