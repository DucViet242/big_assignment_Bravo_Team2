import tkinter as tk
from tkinter import ttk 
from Variable.constants import *
from UI. event_handling import *
from Dataset_metatdata.metadata_processing import *
''' Thiết lập giao diện Dashboard'''
def setup_dashboard( ):
#  Xóa bỏ các widget hiện tại xuất hiện 
    for widget in dashboard_frame. winfo_children ( ):
        widget. destroy( )
#  Tiêu đề 
    ttk. Label( 
        dashboard_frame, 
        text = 'Bảng Điều Khiển chương trình quản lý dự án của Công ty phát triển phần mềm Bravo',
        font = ( 'Times New Roman', 20, 'bold')
    ). pack ( pady = 10)
#  Frame trạng thái 
    status_frame = ttk. LabelFrame(
        dashboard_frame, text = 'Trạng thái kho lưu trữ',
        font = ( 'Times New Roman', 10)
    )
    status_frame. pack ( fill = tk. BOTH, expand = False, padx = 10, pady = 10)
#  Nút làm mới trạng thái 
    ttk.Button(
        status_frame,
        text='Làm mới trạng thái ',
        command=refresh_all
    ).pack(pady=10)
#  Hiển thị trạng thái thông tin đồng bộ 
    if sync_info:
#  Số lượng dự án 
        ttk.Label(
            status_frame,
            text=f"Tổng số Dự án: {sync_info['metadata_count']}"
        ).pack(pady=5)
        if sync_info[ 'is_fully_synced']:
            ttk. Label ( 
                status_frame, 
                text = 'Trạng thái tệp: Tất cả các file đã đồng bộ', 
                foreground = 'Green'
            )
        else:
            status_text = 'Trạng thái tệp: '
            if sync_info['extra_files']:
                status_text += f"Thừa: {len(sync_info['extra_files'])}."
            if sync_info['missing_files']:
                status_text += f"Thiếu: {len(sync_info['missing_files'])}."
            if sync_info['integrity_issues_file']:
                status_text += f"có {len(sync_info['integrity_issues_file'])} tệp có vấn đề toàn vẹn."
            ttk. Label( 
                status_frame, 
                text = status_text, 
                foreground = 'red'
            ). pack ( pady = 5)
    else: 
        ttk. Label(
            status_frame, 
            text = 'Không có thông tin đồng bộ!', 
            foreground = 'orange'
        ). pack ( pady = 5)
#  Hiển thị danh sách dự án 
    project_frame = ttk. LabelFrame( 
        dashboard_frame, 
        text = 'Danh sách dự án', 
        font = ( 'Times New Roman', 10)
    )
    project_frame. pack ( 
        fill = tk. BOTH,
        expand = True,
        padx = 10, 
        pady = 10
    )
#  Tạo Treeview( dạng kiểu table)
    columns = ( 'ID', 'Name', 'Description', 'Creationdate', 'Lastmodified')
    projects_table = ttk. Treeview( 
        project_frame, 
        columns = columns, 
        show = 'headings'
    )
#  Định dạng các cột 
    for column in columns:
        projects_table. heading( column, text = column)
        projects_table. column( column, width = 100)
#  Thêm thanh cuộn
    scrollbar = ttk. Scrollbar( project_frame, orient = tk. VERTICAL, command = projects_table. yview)
    projects_table. configure( yscrollcommand = scrollbar. set)
    scrollbar. pack ( side = tk. RIGHT, fill = tk. Y)
    projects_table. pack( fill = tk. BOTH, expand = True)

#  Đọc và hiển thị dữ liệu 
    success, message, dataset = read_metadata( )
    if success: 
        for row in dataset:
            display_row = row [ :5]
            projects_table. insert ( '', tk. END, values = display_row)


    
