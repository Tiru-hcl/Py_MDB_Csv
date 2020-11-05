'''
This module contains file handling methods and all db configuration, CRUD operation
'''
import json
import csv
import pymongo


class File_Handle:
    '''
     class have methods to handle csv files and json file
    '''
    @staticmethod
    def read_json():
        '''
        method to read json file to read json file
        :return: dict object
        '''
        with open('config.json') as config_file:
            data = json.load(config_file)
        return data

    @staticmethod
    def Csv_read(file_path):
        '''
        method to read csv file
        :param file_path:file location
        :return: list contains all dictionary data
        '''
        with open(file_path, 'r') as a:
            data_list = []
            cs_r = csv.DictReader(a)
            for each in cs_r:
                list.append(each)
        return data_list

class MongoDB:
    '''
    class have methods fo db_configuration and CRUD operations
    '''

    @staticmethod
    def db_config():
        '''
        method to configure db
        :return: db connection details
        '''
        json_data = File_Handle.read_json()
        mongo_client = pymongo.MongoClient(json_data['host'], json_data['port_number'])
        mongo_db = mongo_client[json_data['db_name']]
        collection_name = json_data['coll_name']
        db_connect = mongo_db[collection_name]
        return db_connect

    @staticmethod
    def count_records(db_details):
        '''
        method to count records in collection
        :param db_details: db connection details
        :return: record count
        '''
        record_count = db_details.find().count()
        return record_count

    @staticmethod
    def sort_records(db_details,field):
        '''
        method to sort records
        :param db_details: db_connection details
        :param field: field to sort
        :return:
        '''
        sorted_record = db_details.find().sort(field,1)
        return sorted_record

    @staticmethod
    def insert_record(record):
        '''
        method to insert record
        :param rec: which record to insert
        :return: return id obj
        '''
        record_insert = MongoDB.db_config().insert_one(record)
        return record_insert

    @staticmethod
    def delete_rec(db_details):
        '''
        method to delete all records
        :param db_details: db connection details
        :return: delete record obj
        '''
        delete_record = db_details.remove({})
        return delete_record

    @staticmethod
    def update_records(db_details,query,value):
        '''
        method to update record
        :param db_details: db connection
        :param query: previous value
        :param value: upadate value

        '''
        record_update = db_details.update_many(query, value)
        return record_update














