from bottle import route, run, static_file, template
import os
import pymongo
import json
import random

@route('/static/<filename:path>')
def server_static(filename):
	root_path = os.getcwd() + '/static'
	print root_path
	return static_file(filename, root=root_path)


@route('/')
def icebucket():
	return template('icebucket') 

@route('/get_graph_data')
def get_graph_data():
	connection = pymongo.Connection("mongodb://localhost", safe=True)
	db=connection.icebucket
	nodes = db.nodes
	edges = db.edges
	
	node_list = []
	for n in nodes.find():
		n['id'] = n['_id']
		n['label'] = n['name']
		n['x'] = random.randint(0,100)
		n['y'] = random.randint(0,100)
		n['size'] = 5
		n['color'] = '#666'

		node_list.append(n)

	edge_list = []
	for e in edges.find():
		e['id'] = e['_id']
		e['size'] = 3
		e['color'] = '#ccc'
		edge_list.append(e)
	
	data = {"nodes": node_list, "edges": edge_list}
	return json.dumps(data)	


run(host='localhost', port=8080, debug=True)
