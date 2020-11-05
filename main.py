'''
Main module
'''
import csv
import run
from run import Operations
from util import File_Handle

if __name__ == '__main__':
    Crud_Operation  = Operations()     # object creation

Crud_Operation.store_records()
Crud_Operation.get_records()
Crud_Operation.record_deletion()
Crud_Operation.get_records()
Crud_Operation.sorting_records()


