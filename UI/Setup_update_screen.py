import tkinter as tk
from tkinter import ttk 
from Variable. constants import *
from UI. event_handling import *
"""Thiết lập màn hình cập nhật dự án"""
def setup_update_screen( ):
# Xóa các widget hiện có
    for widget in update_frame. winfo_children( ):
        widget. destroy( )
# Tiêu đề
    ttk. Label( 
        update_frame, 
        text = "Cập nhật Dự án", 
        font=("Arial", 14, "bold") 
        ). pack( pady = 10)
# Frame chọn dự án
    select_frame = ttk. Frame( update_frame)
    select_frame. pack( fill = tk. X, padx = 10, pady = 10)
    ttk.Label (
        select_frame, 
        text = "Chọn ID Dự án:"
    ). pack( side = tk. LEFT, padx = 5)
# Combobox chọn ID
    update_id_combo = ttk. Combobox( select_frame, width = 30)
    update_id_combo. pack(side = tk. LEFT, padx = 5)
    load_button = ttk. Button( 
        select_frame, 
        text = "Tải", 
        command = load_project
    )
    load_button. pack( side = tk. LEFT, padx = 5)
# Frame chi tiết dự án
    details_frame = ttk. LabelFrame( update_frame, text = "Chi tiết Dự án")
    details_frame. pack( fill = tk. X, padx = 10, pady = 10)
# Tên Dự án
    ttk. Label( details_frame, text = "Tên Dự án:"). grid( row = 0, column = 0, sticky = tk. W)
    update_name_entry = ttk. Entry( details_frame, width = 30)
    update_name_entry. grid( row = 0, column = 1)
# Mô tả Dự án
    ttk. Label( details_frame, text = "Mô tả Dự án:"). grid( row = 1, column = 0, sticky = tk. W)
    update_desc_entry = ttk. Entry( details_frame, width = 30)
    update_desc_entry. grid(row = 1, column = 1)
# Mã nguồn
    code_frame = ttk. LabelFrame( update_frame, text = "Mã nguồn")
    code_frame. pack( fill = tk. BOTH, expand = True, padx = 10, pady = 10)
# Widget văn bản với thanh cuộn
    update_code_text = tk. Text( code_frame)
    update_code_text. pack( side = tk. LEFT, fill = tk. BOTH, expand = True)
    code_scrollbar = ttk. Scrollbar( code_frame, command = update_code_text. yview)
    code_scrollbar. pack( side = tk. RIGHT, fill = tk. Y)
    update_code_text. config( yscrollcommand = code_scrollbar.set)
# Nút Cập nhật dự án
    update_button = ttk. Button( update_frame, text = "Cập nhật Dự án", command = handle_update_project)
    update_button. pack( pady = 10)
# Gọi hàm làm mới ban đầu
    refresh_update_list()

