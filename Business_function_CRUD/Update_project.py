import os
from Variable.constants import *
from other_functions.security import *
import datetime
from Dataset_metatdata.metadata_processing import *
#  Ghi file bằng encoding utf-8
def write_file_content ( file_path, content_code): 
    try:
        with open ( file_path, 'w', encoding = 'utf-8') as f:
            f. write( content_code)
            return True, f' Ghi file thành công'
    except Exception as E:
        return False, f' Ghi file không thành công với lỗi: { E}'
#  Ghi file bằng binary
def write_file_binary ( file_path, content_code_bianry):
    try:
        with open ( file_path, 'wb') as f:
            f. write( content_code_bianry)
            return True, f' Ghi file thành công'
    except Exception as E:
        return False, f' Ghi file không thành công với lỗi: { E}'
    
'''Cập nhập thông tin và mã nguồn của dự án'''
def update_project ( id_or_name_old, name_new, description, code_content):
#  Kiểm tra đầu vào 
    if not id_or_name_old:
        return False, f' Cần có ID hoặc tên dự án để tìm kiếm'
#  Tìm kiếm id or name xem có xuất hiện trong metadata không?
    success, row, index, message = find_metadata_ID( id_or_name_old)
    if not success:
        success, row, index, message = find_metadata_name( id_or_name_old)
        if not success:
            return False, f' Không có dự án với ID: { row [ 0]} với tên: { row[ 1]}'
#  Lấy ID và name từ row tìm được 
    dataset_ID = row[ 0]
    dataset_name = row [ 1]
# Lấy thông tin file metadata. csv hiện tại 
    success, message, dataset = read_metadata ( )
    if not success:
        return False, message
#  Kiểm tra name_new có trùng với tên các dự án khác kh?
    if name_new != dataset_name:
        success, row, index, message = find_metadata_name( name_new)
        if success:
            return False, f'Tên dự án "{name_new}" đã được sử dụng'
# Tạo đường dẫn file
    file_path = os. path. join ( FILE_directory, f'{dataset_ID}.txt')
    if not os. path. exists( file_path):
        return False, f' Không tìm thấy file với ID: { dataset_ID}'
    success, message = write_file_content( file_path, code_content)
    if not success:
        code_content_binary = code_content. encode ( 'utf-8', errors = 'replace')
        success, message = write_file_binary( file_path, code_content_binary)
        if not success:
            return False, message
# Tính hash mới
    success, hash_value, message = calculate_file_hash( file_path)
    if not success:
        return False, message
#  Lấy ngày hiện tại 
    last_creat_date = datetime. datetime. now( )
# Cập nhập lại dataset 
    dataset[ index][ 1] = name_new
    dataset[ index][ 2] = description
    dataset [ index][ 4] = last_creat_date
    dataset [ index][ 5] = hash_value
#  Ghi lại file metadata
    success, message = write_metadata ( dataset)
    if success:
        return True, f' Cập nhâp dự án với ID: { dataset_ID} thành công'
    return False, f' Cập nhập dự án với ID: { dataset_ID} không thành công'

    
    
