import tkinter as tk
from tkinter import ttk 
from Variable. constants import *
from UI. event_handling import *
''' Thiết lập màn hình thêm dự án'''
def setup_add_screen( ):
#  Xóa các widget hiện có 
    for widget in add_frame. winfo_children( ):
        widget. destroy( )

#  Tiêu đề
    ttk. Label ( 
        add_frame, 
        text = 'Thêm Dự án Mới', 
        font = ( 'Times New Roman', 20, 'bold')
    ). pack ( pady = 10)

#  Farme chi tiết dự án 
    details_frame = ttk. LabelFrame ( 
        add_frame,
        text = 'Chi tiết dự án'
    )
    details_frame. pack ( 
        fill = tk. X, 
        expand = False, 
        padx = 10,
        pady = 10
    )

#  ID dự án
    ttk. Label( 
        details_frame, 
        text = 'ID Dự án: '
    ). grid ( row = 0, column = 0, sticky = tk. W)
    add_id_entry = ttk.Entry(
        details_frame,
        width = 30
    )
    add_id_entry.grid(row = 0, column = 1)

# Tên Dự án
    ttk. Label( 
        details_frame, 
        text = "Tên Dự án:"
    ).grid( row = 1, column = 0, sticky = tk.W)
    add_name_entry = ttk. Entry( 
        details_frame, 
        width = 30
    )
    add_name_entry. grid( row = 1, column = 1)
    
# Mô tả Dự án
    ttk. Label( 
        details_frame, 
        text = "Mô tả Dự án:"
    ). grid( row = 2, column = 0, sticky = tk.W)
    add_desc_entry = ttk. Entry( 
        details_frame, 
        width = 30
    )
    add_desc_entry. grid( row = 2, column = 1)
    
# Lựa chọn phương thức nhập
    input_method_var = tk. StringVar( value = "direct")
    method_frame = ttk. LabelFrame( 
        add_frame,
        text = "Phương thức Nhập"
    )
    method_frame. pack( 
        fill = tk. BOTH, 
        expand = False, 
        padx = 10, pady = 10
    )
    
# Frame cho các phương thức
    direct_rb = ttk. Radiobutton(
        method_frame, 
        text = "Nhập Mã Trực tiếp", 
        variable = input_method_var, 
        value = "direct", 
        command = toggle_input_method
    )
    direct_rb.pack( anchor = tk. W, padx = 5, pady = 5)
     
    file_rb = ttk. Radiobutton( 
        method_frame, 
        text = "Tải lên Tệp", 
        variable = input_method_var, 
        value = "file", 
        command = toggle_input_method
    )
    file_rb. pack ( anchor = tk. W, padx = 5, pady = 5)
    
# Frame nhập trực tiếp
    direct_frame = ttk. Frame( add_frame)
    direct_frame. pack( 
        fill = tk.BOTH,  
        expand = True, 
        padx = 10, pady = 10
    )
    
    ttk. Label( 
        direct_frame, 
        text = "Mã nguồn:"
        ). pack( anchor = tk. W)
    
# Widget văn bản với thanh cuộn
    code_frame = ttk. Frame( direct_frame)
    code_frame. pack( fill = tk. BOTH, expand = True)
    
    add_code_text = tk. Text( code_frame)
    add_code_text. pack( 
        side = tk. LEFT, 
        fill = tk. BOTH, 
        expand = True
    )
    
    code_scrollbar = ttk. Scrollbar(
        code_frame, 
        command = add_code_text. yview
    )
    code_scrollbar. pack(
        side = tk. RIGHT, 
        fill = tk. Y
    )
    add_code_text. config( yscrollcommand = code_scrollbar. set)
    
# Frame tải file
    file_frame = ttk. Frame( add_frame)
    
    ttk. Label (
        file_frame, 
        text = "Tệp đã chọn:"
    ). pack( anchor = tk. W, pady = 5)
    file_path_var = tk. StringVar( )
    
    file_path_entry = ttk. Entry(
        file_frame, 
        textvariable = file_path_var, 
        state = "readonly", 
        width = 50
    )
    file_path_entry. pack(
        fill = tk. X, 
        expand = True, 
        padx = 5
    )
    
    browse_button = ttk. Button( 
        file_frame,  
        text = "Duyệt...", 
        command = browse_file
    )
    browse_button. pack( pady = 10)
    
# Nút Thêm dự án
    add_button = ttk. Button( 
        add_frame, 
        text = "Thêm Dự án", 
        command = handle_add_project
    )
    add_button. pack( pady = 10)
    
# Gọi toggle_input_method ban đầu để hiển thị đúng frame
    toggle_input_method()
