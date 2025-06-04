import os
from Variable.constants import *
from Dataset_metatdata.metadata_processing import *
'''Xóa file'''
def delete_file ( file_path):
    try:
        if os. path. exists( file_path):
            os. remove ( file_path)
            return True, f' Xóa file thành công'
        else: 
            return False, f' File không tồn tại'
    except Exception as E:
        return False, f' Lỗi không xóa được file: { E}'


'''Xóa dự án theo tên hoặc ID'''
def delete_project ( id_or_name):
#  Tìm kiếm theo ID
    success, row, index, message = find_metadata_ID( id_or_name)
    if not success:
#  Nếu không tìm thấy theo ID thì tìm kiếm theo tên 
        success, row, index, message = find_metadata_name( id_or_name)
        if not success:
            return False, message
#  Lấy tên và ID của dự án 
    project_id = row[ 0]
    project_name = row [ 1]
#  Lấy link file cần xóa
    file_path = os. path. join ( FILE_directory, f'{project_id}.txt')
#  Xóa file
    success, message = delete_file( file_path)
    if not success:
        return False, message
#  Xóa bản ghi file khỏi metadata
    success, message, dataset = read_metadata( )
    if not success:
        return False, message

    dataset. pop( index)
#  Cập nhập lai metadata
    success, message = write_metadata( dataset)
    if success:
        return True, f' Xóa dự án có ID: { project_id} với tên: { project_name} thành công'
    else: 
        return False, f' Xóa dự án có ID: { project_id} với tên: { project_name} không thành công'
         

