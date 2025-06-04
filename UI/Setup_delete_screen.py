import tkinter as tk
from tkinter import ttk
import Variable.constants as constants
import UI.event_handling as event_handling

"""Thiết lập màn hình xóa dự án"""
def setup_delete_screen():
    """Setup the Delete Project screen."""
    # Clear existing widgets
    for widget in constants.delete_frame.winfo_children():
        widget.destroy()
# Tiêu đề
    ttk.Label(
        constants.delete_frame,
        text = "Xóa Dự án", 
        font = ("Arial", 14, "bold")
    ). pack( pady = 10)
# Frame xóa
    delete_input_frame = ttk.Frame(constants.delete_frame)
    delete_input_frame.pack(
        fill = tk. X,
        padx = 10, pady = 10
    )
    ttk. Label(
        delete_input_frame, 
        text="Nhập ID hoặc Tên Dự án:"
    ). pack( side = tk. LEFT, padx = 5) 
    constants.delete_entry = ttk.Entry(
        delete_input_frame,
        width=30
    )
    constants.delete_entry.pack(
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
    projects_frame = ttk.LabelFrame(
        constants.delete_frame,
        text = "Dự án Hiện có"
    )
    projects_frame. pack( 
        fill = tk. BOTH, 
        expand = True, 
        padx = 10, pady = 10
    )
# Tạo Treeview
    columns = ( "ID", "Name", "Description")
    constants.delete_projects_table = ttk.Treeview(
        projects_frame,
        columns=columns,
        show="headings",
    )
# Định dạng các cột
    for col in columns:
        constants.delete_projects_table.heading(col, text=col)
    constants.delete_projects_table.column("ID", width=100)
    constants.delete_projects_table.column("Name", width=150)
    constants.delete_projects_table.column("Description", width=300)
# Thêm thanh cuộn
    scrollbar = ttk.Scrollbar(
        projects_frame,
        orient=tk.VERTICAL,
        command=constants.delete_projects_table.yview,
    )
    constants.delete_projects_table.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    constants.delete_projects_table.pack(fill=tk.BOTH, expand=True)
# Gắn sự kiện double-click
    constants.delete_projects_table.bind(
        "<Double-1>", event_handling.on_delete_project_select
    )
# Nút Làm mới
    refresh_button = ttk.Button(
        constants.delete_frame,
        text="Làm mới Danh sách",
        command=event_handling.refresh_delete_list,
    )
    refresh_button.pack(pady=10)
# Gọi hàm làm mới ban đầu 
    event_handling.refresh_delete_list()
