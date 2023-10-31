import mindsdb_sdk

server = mindsdb_sdk.connect('http://127.0.0.1:47334')

project = server.get_project()

