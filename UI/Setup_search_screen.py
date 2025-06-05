import tkinter as tk
from tkinter import ttk 
from Variable. constants import *
from UI. event_handling import *
"""Thiết lập màn hình tìm kiếm dự án"""
def setup_search_screen( ):
# Xóa các widget hiện có
    for widget in search_frame. winfo_children( ):
        widget. destroy( )
# Tiêu đề
    ttk.Label( 
        search_frame, 
        text = "Tìm kiếm Dự án", 
        font = ("Arial", 14, "bold")
    ). pack( pady = 10)
# Frame tìm kiếm
    search_input_frame = ttk. Frame( search_frame)
    search_input_frame. pack( fill = tk. X, padx = 10, pady = 10)
    ttk. Label(
        search_input_frame, 
        text = "Từ khóa:"
        ). pack( side = tk. LEFT, padx = 5)
    search_entry = ttk. Entry( search_input_frame, width = 30)
    search_entry. pack( side = tk. LEFT, padx = 5)
    search_button = ttk. Button(
        search_input_frame, 
        text = "Tìm kiếm", 
        command = handle_search_projects
    )
    search_button. pack( side = tk. LEFT, padx = 5)
# Frame kết quả
    results_frame = ttk. LabelFrame(
        search_frame, 
        text = "Kết quả Tìm kiếm"
    )
    results_frame. pack(fill = tk. BOTH, expand = True, padx = 10, pady = 10)
# Tạo Treeview cho kết quả
    columns = ( "ID", "Name", "Description")
    search_results_table = ttk. Treeview(
        results_frame, 
        columns = columns, 
        show = "headings"
    )
# Định dạng các cột
    for col in columns:
        search_results_table. heading( col, text = col)
    search_results_table. column( "ID", width = 100)
    search_results_table. column( "Name", width = 150)
    search_results_table. column( "Description", width = 300)
# Thêm thanh cuộn
    scrollbar = ttk. Scrollbar( 
        results_frame, 
        orient = tk. VERTICAL, 
        command = search_results_table.yview
    )
    search_results_table. configure( yscrollcommand = scrollbar. set)
    scrollbar. pack( side = tk. RIGHT, fill = tk. Y)
    search_results_table.pack(fill = tk.BOTH, expand= True)
# Frame xem trước
    preview_frame = ttk. LabelFrame( search_frame, text = "Xem trước Mã nguồn")
    preview_frame. pack( fill = tk. BOTH, expand = True, padx = 10, pady = 10)
# Widget văn bản xem trước
    preview_text = tk. Text( preview_frame, state = tk. DISABLED)
    preview_text. pack( side = tk. LEFT, fill = tk. BOTH, expand = True)
    preview_scrollbar = ttk. Scrollbar( 
        preview_frame, 
        command = preview_text. yview
    )
    preview_scrollbar. pack( side = tk. RIGHT, fill = tk. Y)
    preview_text. config( yscrollcommand = preview_scrollbar. set)   
# Gắn sự kiện chọn
    search_results_table. bind( "<<TreeviewSelect>>", on_search_result_select)