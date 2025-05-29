import os
import csv 
from Variable.constants import *


'''Nếu thư mục và file chưa tồn tại '''
#  Hàm tạo thư mục File_save_code, metadata. csv
def create_directory_file ( ):
# # Khởi tạo thư mục 
    try:
        if not os. path. exists ( FILE_directory):
            os. makedirs ( FILE_directory)
            print ( ' Tạo thư mục thành công')
    except Exception as E:
        print ( f' Gặp lỗi tạo thư mục { E}')
        return
# # KHởi tạo file metadata. csv
    try: 
        if not os. path. exists ( METADATA_FILE):
            with open ( METADATA_FILE, 'w', encoding = 'utf-8') as M:
                file = csv. writer ( M)
                file. writerow( METADATA_header)
            print ( ' Tạo file thành công')
    except Exception as E:
        print ( f' Gặp lỗi tạo file { E}')
        return 
    
''' Liệt kê các file trong thư mục File_save_code'''
def list_file_in_directory( File_directory):
    files = [ ]
    try:
        if not os. path. exists( FILE_directory):
            return False, None, f' Không tìm thấy thư mục'
        for file_txt in os.listdir( FILE_directory):
            files. append (file_txt)
        return True, files, f' Đã tìm thấy { len ( files)} trong thư mục { File_directory}'
    except Exception as E:
        return False, None, f' Lỗi liệt kê file: { E}'
    

    