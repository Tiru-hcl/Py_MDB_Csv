import csv
import pymongo
import json

class File_Handler:
    '''
    This class conatins methods for file handling
    '''

    @staticmethod
    def read_csv(file_path):
        '''
        To read csv file
        :param file_path: file location path
        :return: generator object
        '''
        with open(file_path, 'r') as a:
            cs_r = csv.DictReader(a)
            yield cs_r

    @staticmethod
    def json_file_read(file_location):
        '''
         Opening JSON file
        :param file_location:
        :return: json
        '''
        with open(file_location, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        return json_object

class MongoDb:
    '''
    This class havs methods from DB CRUD operations
    '''

    @staticmethod
    def db_details(host,port_number,db_name,collection_name):
        '''
        method to connect datbase
        :param host:db host
        :param port_number:db port_number
        :param db_name:database name
        :param collection_name:collection name
        :return:db driver
        '''
        mongo_client = pymongo.MongoClient(host, port_number)
        mongo_db = mongo_client[db_name]
        collection_name = collection_name
        db_connect = mongo_db[collection_name]
        return db_connect

    @staticmethod
    def insert_each_record(host, port_number, db_name, collection_name, path):
        '''
        Method to insert each record from generator object to mongodb
        '''
        for records in File_Handler.read_csv(path):
            for each_record in records:
                MongoDb.db_details(host, port_number, db_name, collection_name).insert(each_record)
            return True

    @staticmethod
    def sort_records_ascending(host,port_number,db_name,collection_name,field):
        '''
        To sort records
        :param field: sort based on which field
        :return:  return sorted records
        '''
        sorted_records = MongoDb.db_details(host,port_number,db_name,collection_name).find().sort('field',1)
        return sorted_records

    @staticmethod
    def delete_records(host,port_number,db_name,collection_name):
        '''
        To delete all records in collection
        '''
        MongoDb.db_details(host, port_number, db_name, collection_name).remove({})
        return 'all records removed from collection'

    @staticmethod
    def update_records(host,port_number,db_name,collection_name,query,value):
        '''
        to update records in db
        query : previous one   query = { "key": "Value" }
        value :updated one    value = { "$set": { "key": "updated value" } }
        '''
        MongoDb.db_details(host, port_number, db_name, collection_name).update(query,value)
        return 'records updated'












