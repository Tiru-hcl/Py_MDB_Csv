'''
module to do all data operations
'''
import util
from util import MongoDB,File_Handle
class Operations:
    '''
    class contains all data operation methods
    '''

    def __init__(self):
        self.db_config = MongoDB.db_config()

    def get_records(self):
        '''
        dta op method to record count
        '''
        record_count = MongoDB.db_config().find().count()
        return record_count

    def store_records(self):
        '''
        method to store each record into mongodb
        :return:
        '''
        json_data = File_Handle.read_json()
        csv_rec = File_Handle.Csv_read(json_data['path'])
        for each_record in csv_rec:
            if each_record not in self.db_config.find(json_data['order_ID']):
                MongoDB.insert_record( each_record)
        return 'records inserted successfully'

    def record_deletion(self):
        '''
        data op method to delete records
        '''
        deleted_records= MongoDB.delete_rec(self.db_config)
        return deleted_records

    def updating_records(self):
        '''
        data operation method to update records
        '''
        json_data = File_Handle.read_json()
        update_result = MongoDB.update_records(self.db_config,json_data['query'],json_data['value'])
        return update_result

    def sorting_records(self):
        '''
        method to sort record
        '''
        json_data = File_Handle.read_json()
        sorting_ascending_order = MongoDB.sort(self.db_config,json_data['field'])
        return sorting_ascending_order








