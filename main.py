'''
Main module

'''
import csv
import run
from run import Operations
from util import File_Handle

if __name__ == '__main__':
    '''
    to call all CRUD operation methods 
    To see results print 
    For further process we can store in variable 
    '''
    Crud_Operation  = Operations()     # object creation

Crud_Operation.store_records()         #Method call to store records to db
Crud_Operation.get_records()        # method call to retrieve reords from db
Crud_Operation.record_deletion()       # Method call to delete records
Crud_Operation.sorting_records()       # mMethod call to sort records
Crud_Operation.updating_records()

