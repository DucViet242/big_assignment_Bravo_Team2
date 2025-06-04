import csv 
from Variable.constants import * 

'''Đọc file metadata'''
def read_metadata ( ):
    try:
        with open ( METADATA_FILE, 'r', encoding = 'utf-8') as M:
            file = csv. reader( M)
            next ( file)
            dataset = list ( file)
        return True, f' Đọc file thành công', dataset  
    except FileNotFoundError as file_errol:
        return False, f' Không tồn tài file { file_errol}', None 

'''Ghi dữ liệu vào file metadata. csv '''  
def write_metadata( dataset):
    try:
        with open ( METADATA_FILE, 'w', encoding = 'utf-8') as M: 
            file = csv. writer ( M)
            file. writerow( METADATA_header)
            file. writerows( dataset)
        return True, f' Ghi file thành công'
    except Exception as E:
        return False, f' Lỗi ghi file { E}'
    
''' Thêm 1 dòng bản ghi vào metadata. csv '''
def add_row_metadata( row):
    try: 
        with open ( METADATA_FILE, 'a', encoding = 'utf-8') as M:
            file = csv. writer( M)
            file. writerow( row)
        return True, f' Thêm dòng dữ liệu thành công'
    except Exception as E:
        return False, f' Thêm dòng dữ liệu bị lỗi { E}'
    
''' Tìm kiếm bản ghi theo ID'''
def find_metadata_ID ( ID):
    success, message, dataset = read_metadata( )
    if not success:
        return False, None, None,f' Không có dữ liệu tìm kiếm'
    for index, row in enumerate( dataset):
        if row[ 0] == ID:
            return True, row, index,f' Đã tìm thấy bản ghi với ID: { ID}'
    return False, None, None,f' Không tìm thấy bản ghi với ID: { ID}'

''' Tìm kiếm bản ghi theo tên'''
def find_metadata_name ( name):
    success, message, dataset = read_metadata( )
    if not success:
        return False, None, f' Không có dữ liệu tìm kiếm'
    for index, row in enumerate ( dataset):
        if row[ 1] == name:
            return True, row, index,f' Đã tìm thấy dữ liệu bản ghi với tên: { name}'
    return False, None, None,f' KHông tìm thấy dữ liệu bản ghi với tên: { name}'