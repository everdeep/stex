import sys
import re

from pyquery import PyQuery as pq
from lxml import etree

d = pq(url='http://www.asx.com.au/asx/statistics/prevBusDayAnns.do')
table = d('.contenttable')

if len(table) == 0:
	print 'Unable to find the table element'

with open('./assets/data/test.txt', mode='w+') as txtfile:
	temp = str(table)
	txtfile.write(temp)

with open('./assets/data/columns.txt', mode='w+') as txtfile:
	for column in d('tr th a'):
		txtfile.write(str(column.text) + ' ')

	txtfile.write('\n')

	for row in d('tr'):
		for column in d('tr td'):
			txtfile.write(str(d))
		txtfile.write('\n')



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
