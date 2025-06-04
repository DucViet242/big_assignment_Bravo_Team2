''' Biến liên quan đến file/ đường dẫn/ thư mục'''
METADATA_FILE = 'metadata.csv'
METADATA_header = ['ID', 'Name', 'Description', 'Creat_Date', 'Last_Creat_Date', 'Hash']
FILE_directory = 'File_save_code'

''' Biến liên quan đến giao diện UI'''
root = None
notebook = None
sync_info = {}
# Dashboard
dashboard_frame = None
project_count_label = None
file_status_label = None
projects_table = None
# Thêm dự án
add_frame = None
add_id_entry = None
add_name_entry = None
add_desc_entry = None
add_code_text = None
input_method_var = None
direct_frame = None
file_frame = None
file_path_var = None
# Xóa dự án
delete_frame = None
delete_entry = None
delete_projects_table = None
# Cập nhật dự án
update_frame = None
update_id_combo = None
update_name_entry = None
update_desc_entry = None
update_code_text = None
# Tìm kiếm dự án
search_frame = None
search_entry = None
search_results_table = None
preview_text = None