import os
from Dataset_metatdata.metadata_processing import *
from other_functions.file_processing import *
from other_functions.security import *
from Variable.constants import *

''' Kiểm tra tính đồng bộ giữa các file trong thư mục với trong metadata'''
def Data_synchronization():
    # Đọc dữ liệu metadata.csv
    success, message, dataset = read_metadata()
    if not success:
        return False, {}, message

    # Lấy danh sách file 
    success, files, message = list_file_in_directory(FILE_directory)
    if not success:
        return False, {}, message
    
    # Lấy danh sách ID từ metadata
    metadata_IDs = []
    for row in dataset:
        # Kiểm tra row không empty và có đủ columns
        if row and len(row) >= 6:
            metadata_IDs.append(row[0])
        
    # Lấy tên file = ID + '.txt' 
    metadata_name_file = []
    for ID in metadata_IDs:
        metadata_name_file.append(f'{ID}.txt')
    
    # Tìm file thừa và thiếu
    # Tìm file thừa 
    extra_files = []
    for file in files:
        if file.endswith('.txt') and file not in metadata_name_file:
            extra_files.append(file)
            
    # Tìm file thiếu
    missing_files = []
    for file in metadata_name_file:
        if file not in files:
            missing_files.append(file)

    # Kiểm tra tính toàn vẹn của file 
    integrity_issues_file = []
    for row in dataset:
        # Kiểm tra row có đủ columns không
        if row and len(row) >= 6:
            column_file_hash = row[5]
            column_file_id = row[0]
            file_path = os.path.join(FILE_directory, f'{column_file_id}.txt')
            if os.path.exists(file_path):
                success, intact, message = verify_file_integrity(file_path, column_file_hash)
                if success and not intact:
                    integrity_issues_file.append(column_file_id)
                
    # Xác định trạng thái đồng bộ
    is_fully_synced = (
        len(extra_files) == 0 and 
        len(missing_files) == 0 and 
        len(integrity_issues_file) == 0
    )

    # Tạo kết quả 
    sync_data = {
        'metadata_count': len(dataset),
        'file_count': len(files),
        'extra_files': extra_files,
        'missing_files': missing_files,
        'integrity_issues_file': integrity_issues_file,
        'is_fully_synced': is_fully_synced
    }
    return True, sync_data, f'Kiểm tra đồng bộ hoàn tất'