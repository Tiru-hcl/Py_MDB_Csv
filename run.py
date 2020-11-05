import util
import json
from util import File_Handler,MongoDb


class Data_operations:
    '''
    class contains all data operations
    '''

    def __init__(self,host,port,db_name,collection_name,path,field,query,value):
        self.path = path
        self.host = host
        self.port = port
        self.db_name = db_name
        self.collection_name = db_name
        self.field = field
        self.query = query
        self.value = value

    def sort_records(self):
        '''
        method call to sort records
        :return: sorted records obj
        '''
        sorted_records = MongoDb.sort_records_ascending(self.host,self.port,self.db_name,self.collection_name,self.field)
        return sorted_records

    def insert_records(self):
        '''
        method call to insert records
        '''
        records_inserted= MongoDb.insert_each_record(self.host,self.port, self.db_name, self.collection_name, self.path)
        return records_inserted

    def delete_records(self):
        '''
        method call to delete records
        '''
        records_delete = MongoDb.delete_records(self.host,self.port, self.db_name, self.collection_name)
        return records_delete

    def update_records(self):
        records_update=util.MongoDb.update_records(self.host,self.port, self.db_name, self.collection_name,self.query,self.value)
        return records_update

    def csv_reader(self):
        gen_csv_obj = util.File_Handler.read_csv(self.path)
        return gen_csv_obj

    def json_read(self):
        '''
        call json read method
        :return: return
        '''
        json_obj = util.File_Handler.json_file_read(self.path)
        return json_obj







