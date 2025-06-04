import os
from Variable.constants import *
from Dataset_metatdata.metadata_processing import *

def read_file_content( file_path):
#  Đọc nội dung file
    try:
# # Đọc nội dung file với mã hóa utf-8
        with open ( file_path, 'r', encoding = 'utf-8') as f:
            code_content = f. read ( )
        return True, code_content, f' Đọc nội dung file thành công theo mã hóa utf-8'
    except UnicodeDecodeError as U:
# # Đọc nội dung file với mã hóa binary
        try:
            with open ( file_path, 'rb') as f:
                code_content = f. read( )
            return True, code_content, f' Đọc nội dung file thành công theo mã hóa binary'
        except Exception as E:
            return False, None, f' Lỗi đọc file binary với lỗi: { E}'

'''Tìm kiếm thấy dự án theo từ khóa: ID or name project'''
def search_projects( keyword):
#  Tìm kiếm dự án thông qua từ khóa
    if not keyword:
        return False, None, f' Từ khóa tìm kiếm là bắt buộc'
# # Đọc Metadata
    success, message, dataset = read_metadata( )
    if not success:
        return False, None, message
# # Tìm kiếm
    results = [ ]
    for row in dataset:
        if keyword. lower( ) in row[ 0]. lower( ) or keyword. lower( ) in row[ 1]. lower ( ):
            results. append( row)
    if not results:
        return False, None, f' KHông tìm kiếm thấy dự án nào có từ khóa: "{ keyword}"'
    else:
        return True, results, f' Tìm kiếm thấy dự án chứa từ khóa: { keyword}'

def get_project_content( id):
#  Lấy nội dung mã nguồn của dự án 
    if not id:
        return False, None, f' ID là bắt buộc để lấy thông tin'
    file_path = os. path. join( FILE_directory, f'{id}.txt')
    if not os. path. exists ( file_path):
        return False, None, f' Không tìm thấy file chứa ID: { id}'
    success, code_content, message = read_file_content( file_path)
    if not success:
        return False, None, message
    return True, code_content, f' Lấy nội dung file: "{ id} thành công'
    
    
