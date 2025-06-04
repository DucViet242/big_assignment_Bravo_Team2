import os
import datetime
from Variable.constants import *
from other_functions.security import *
from Dataset_metatdata.metadata_processing import *

''' Ghi dữ liệu vào file dạng utf-8'''
def write_file_content ( file_path, content):
    try:
        with open ( file_path, 'w', encoding = 'utf-8') as f:
            f. write ( content)
            return True, f' Ghi file thành công'
    except UnicodeEncodeError as E:
        return False, f' Lỗi ghi file: { E}'
    
''' Ghi file dưới dạng binary'''
def write_file_binary ( file_path, content_binary):
    try: 
        with open ( file_path, 'wb') as f:
            f. write ( content_binary)
            return True, f' Ghi file thành công'
    except Exception as E:
        return False, f' Lỗi ghi file: { E}'
    
''' Thêm dự án '''
#  Thêm dự án từ mã nguồn trưc tiếp
def add_project_from_soure_code ( id, name, description, code_content):
# # Kiểm tra đầu vào 
    if not id or not name:
        return False, f' ID và tên dự án là bắt buộc'
# # Kiêm tra xem có trùng lặp ID không?
    success, row, index, message = find_metadata_ID( id)
    if success:
        return False, message
# # Kiểm tra tên dự án nhập vào có trùng lặp với các tên dự án trước đó không?
    success, row, index, message = find_metadata_name( name)
    if success:
        return False, message
# # Tạo đường dẫn file 
    file_path = os. path. join ( FILE_directory, f'{id}.txt')
# # Ghi mã nguồn vào file 
# # # Ghi bằng utf-8
    success, message = write_file_content( file_path, code_content)
    if not success:
# # # Ghi bằng binary
        code_content_binary = code_content. encode ( 'utf-8', errors = 'replace')
        success, message = write_file_binary( file_path, code_content_binary)
        if not success:
            return False, message
# # Tính hash
    success, hash_value, message = calculate_file_hash( file_path)
    if not success:
        return False, message
# # Lấy ngày hiện tại 
    current_date = datetime. datetime. now( )
# # Thêm vào metadata
    metadata_row = [ id, name, description, current_date, current_date, hash_value]
    success, message = add_row_metadata( metadata_row)
    if success:
        return True, f' Ghi file: { name} thành công'
    else:
        return False, message
    
#  Thêm dự án mới từ file
def add_project_from_file ( id, name, description, source_file_path):
# # Kiểm tra đầu vào 
    if not id or not name:
        return False, f' ID avf tên dự án là bắt buộc'
# # Kiêm tra xem có trùng lặp ID không?
    success, _, _, _ = find_metadata_ID( id)
    if success:
        return False, f' Dự án đã tồn tại ID: { id}'
# # Kiểm tra file tồn tại không?
    if not os. path. exists( source_file_path):
        return False, f' File: { source_file_path} không tồn tại'
# # Tạo đường dẫn cho file đích 
    file_path = os. path. join ( FILE_directory, f'{id}.txt')
# # ĐỌc nội dung file 
    with open ( source_file_path, 'r', encoding = 'utf-8') as f:
        content = f. read( )
# # # Ghi nội dung vào file đích 
    success, message = write_file_content( file_path, content)
    if not success:
        code_content_binary = content. encode( 'utf-8', errors = ' replace')
        success, message = write_file_binary( file_path, code_content_binary)
        if not success:
            return False, message
# # Tính mã hash 
    success, hash_value,message = calculate_file_hash( file_path)
    if not success:
        return False, message
# # Lấy ngày hiện tại 
    current_date = datetime. datetime. now( )
# # Thêm vào metadata 
    metadata_row = [ id, name, description, current_date, current_date, hash_value]
    success, message = add_row_metadata( metadata_row)
    if success:
        return True, f' Ghi file thành công'
    else: 
        return False, message
    

