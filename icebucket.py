from bottle import route, run, static_file, template
import os

@route('/static/<filename:path>')
def server_static(filename):
	root_path = os.getcwd() + '/static'
	print root_path
	return static_file(filename, root=root_path)


@route('/')
def icebucket():
	return template('icebucket') 

run(host='localhost', port=8080, debug=True)
