import tkinter as tk
from tkinter import ttk 
from Variable import constants
from Dataset_metatdata.metadata_processing import *

''' Thiết lập giao diện Dashboard'''
def setup_dashboard():
    """Setup dashboard tab widgets."""
    
    # Xóa bỏ các widget hiện tại xuất hiện 
    for widget in constants.dashboard_frame.winfo_children():
        widget.destroy()
        
    # Tiêu đề 
    ttk.Label(
        constants.dashboard_frame,
        text='Bảng Điều Khiển chương trình quản lý dự án của Công ty phát triển phần mềm Bravo',
        font=('Times New Roman', 20, 'bold')
    ).pack(pady=10)
    
    # Frame trạng thái 
    status_frame = ttk.LabelFrame(
        constants.dashboard_frame,
        text='Trạng thái kho lưu trữ'
    )
    status_frame.pack(fill=tk.BOTH, expand=False, padx=10, pady=10)
    
    # Nút làm mới trạng thái 
    # Import local để tránh circular import
    from UI.event_handling import refresh_all
    ttk.Button(
        status_frame,
        text='Làm mới trạng thái',
        command=refresh_all
    ).pack(pady=10)
    
    # Hiển thị trạng thái thông tin đồng bộ 
    if constants.sync_info:
        # Số lượng dự án 
        ttk.Label(
            status_frame,
            text=f"Tổng số Dự án: {constants.sync_info['metadata_count']}"
        ).pack(pady=5)
        
        if constants.sync_info['is_fully_synced']:
            ttk.Label(
                status_frame, 
                text='Trạng thái tệp: Tất cả các file đã đồng bộ', 
                foreground='Green'
            ).pack(pady=5)
        else:
            status_text = 'Trạng thái tệp: '
            if constants.sync_info['extra_files']:
                status_text += f"Thừa: {len(constants.sync_info['extra_files'])}."
            if constants.sync_info['missing_files']:
                status_text += f"Thiếu: {len(constants.sync_info['missing_files'])}."
            if constants.sync_info['integrity_issues_file']:
                status_text += f"có {len(constants.sync_info['integrity_issues_file'])} tệp có vấn đề toàn vẹn."
            ttk.Label(
                status_frame, 
                text=status_text, 
                foreground='red'
            ).pack(pady=5)
    else: 
        ttk.Label(
            status_frame, 
            text='Không có thông tin đồng bộ!', 
            foreground='orange'
        ).pack(pady=5)
        
    # Hiển thị danh sách dự án 
    project_frame = ttk.LabelFrame(
        constants.dashboard_frame,
        text='Danh sách dự án'
    )
    project_frame.pack(
        fill=tk.BOTH,
        expand=True,
        padx=10, 
        pady=10
    )
    
    # Tạo Treeview (dạng kiểu table)
    columns = ('ID', 'Name', 'Description', 'Creationdate', 'Lastmodified')
    constants.projects_table = ttk.Treeview(
        project_frame,
        columns=columns,
        show='headings'
    )
    
    # Định dạng các cột 
    for column in columns:
        constants.projects_table.heading(column, text=column)
        constants.projects_table.column(column, width=100)
        
    # Thêm thanh cuộn
    scrollbar = ttk.Scrollbar(project_frame, orient=tk.VERTICAL, command=constants.projects_table.yview)
    constants.projects_table.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    constants.projects_table.pack(fill=tk.BOTH, expand=True)

    # Đọc và hiển thị dữ liệu 
    success, message, dataset = read_metadata()
    if success:
        for row in dataset:
            # Kiểm tra row có đủ dữ liệu không
            if row and len(row) >= 5:
                display_row = row[:5]
                constants.projects_table.insert('', tk.END, values=display_row)
