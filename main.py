import run
import json




    
with open('conf.json') as config_file:
    data = json.load(config_file)

if __name__ == "__main__":
    CRUD_operations = run.Data_operations(data['host'],data['port_number'],data['db_name'],data['coll_name'],data['path'],
                                          data['field'],data['query'],data['value'])







