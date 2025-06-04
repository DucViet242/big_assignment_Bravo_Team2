import tkinter as tk
from tkinter import ttk 
from Variable. constants import *
from UI. event_handling import *

"""Thiết lập màn hình xóa dự án"""
def setup_delete_screen( ):
# Xóa các widget hiện có
    for widget in delete_frame. winfo_children( ):
        widget. destroy( )
# Tiêu đề
    ttk. Label(
        delete_frame, 
        text = "Xóa Dự án", 
        font = ("Arial", 14, "bold")
    ). pack( pady = 10)
# Frame xóa
    delete_input_frame = ttk. Frame( delete_frame)
    delete_input_frame. pack(
        fill = tk. X, 
        padx = 10, pady = 10
    )
    ttk. Label(
        delete_input_frame, 
        text="Nhập ID hoặc Tên Dự án:"
    ). pack( side = tk. LEFT, padx = 5) 
    delete_entry = ttk. Entry(
        delete_input_frame, 
        width=30
    )
    delete_entry. pack(
        side = tk.LEFT, 
        padx=5
    )
    delete_button = ttk. Button( 
        delete_input_frame, 
        text = "Xóa", 
        command = handle_delete_project
    )
    delete_button. pack( side = tk. LEFT, padx = 5)
# Danh sách dự án
    projects_frame = ttk. LabelFrame(
        delete_frame, 
        text = "Dự án Hiện có" 
    )
    projects_frame. pack( 
        fill = tk. BOTH, 
        expand = True, 
        padx = 10, pady = 10
    )
# Tạo Treeview
    columns = ( "ID", "Name", "Description")
    delete_projects_table = ttk. Treeview( 
        projects_frame, 
        columns = columns,  
        show = "headings"
    )
# Định dạng các cột
    for col in columns:
        delete_projects_table. heading( col, text = col)
    delete_projects_table. column( "ID", width = 100)
    delete_projects_table. column( "Name", width = 150)
    delete_projects_table. column( "Description", width = 300)
# Thêm thanh cuộn
    scrollbar = ttk. Scrollbar(
        projects_frame, 
        orient = tk. VERTICAL, 
        command = delete_projects_table. yview
    )
    delete_projects_table. configure( yscrollcommand = scrollbar. set)
    scrollbar. pack( side = tk. RIGHT, fill = tk. Y)
    delete_projects_table. pack( fill = tk. BOTH, expand = True)
# Gắn sự kiện double-click
    delete_projects_table. bind( "<Double-1>", on_delete_project_select)
# Nút Làm mới
    refresh_button = ttk. Button(
        delete_frame, 
        text = "Làm mới Danh sách", 
        command = refresh_delete_list
    )
    refresh_button. pack( pady = 10)
# Gọi hàm làm mới ban đầu 
    refresh_delete_list( )