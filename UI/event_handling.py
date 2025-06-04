import tkinter as tk 
from Variable.constants import *
from other_functions.Data_synchronization import *
from Dataset_metatdata.metadata_processing import *
from UI. Dasboard import *
from tkinter import messagebox, filedialog
from Business_function_CRUD. Add_project import *
from Business_function_CRUD. Delete_project import *
from Business_function_CRUD. Find_project import * 
from Business_function_CRUD. Update_project import *

def refresh_all( ):
#  Làm mới tất cả các tab
# # Kiểm tra đồng bộ
    success, sync_data, message = Data_synchronization( )
    if success:
        sync_info = sync_data
# # Làm mới các tab
    setup_dashboard( )
    refresh_delete_list( )
    refresh_update_list( )
    
def refresh_delete_list( ):
# Làm mới danh sách dự án trong tab xóa
    for item in delete_projects_table. get_children ( ):
        delete_projects_table. delete( item)
# # Đọc và hiển thị dữ liệu
    success, message, dataset = read_metadata( )
    if success:
        for row in dataset:
            delete_projects_table. insert ( 
                '', 
                tk. END, 
                values = ( row[ 0], row[ 1], row[ 2])
            )

def refresh_update_list( ):
# Làm mới danh sách cập nhập trong tab cập nhập 
    success, message, dataset = read_metadata( )
    Ids = [ ]
    if success:
        for row in dataset:
            Ids. append ( row[ 0])
        update_id_combo[ 'values'] = Ids

def handle_add_project():
# Xử lý khi nhấn nút Thêm dự án
# # Lấy thông tin dự án
    project_id = add_id_entry. get( ). strip( )
    project_name = add_name_entry. get( ). strip ( )
    project_desc = add_desc_entry. get( ). strip ( )
    
# # Kiểm tra dữ liệu đầu vào
    if not project_id or not project_name:
        messagebox. showerror("Lỗi", "ID và Tên dự án là bắt buộc!")
        return
    
# # Thêm dự án dựa trên phương thức đã chọn
    if input_method_var. get( ) == "direct":
# # # Lấy mã nguồn từ Text widget
        code_content = add_code_text. get( "1.0", tk. END)
        
# # # Gọi hàm thêm dự án
        success, message = add_project_from_soure_code( project_id, project_name, project_desc, code_content)
    else:
# # # Lấy đường dẫn file
        file_path = file_path_var. get( )
        
        if not file_path:
            messagebox. showerror( "Lỗi", "Vui lòng chọn một tệp!")
            return
        
# # # Gọi hàm thêm dự án từ file
        success, message = add_project_from_file( project_id, project_name, project_desc, file_path)
    
# # Hiển thị kết quả
    if success:
        messagebox. showinfo( "Thành công", message)
        
# # # Xóa dữ liệu đã nhập
        add_id_entry. delete( 0, tk. END)
        add_name_entry. delete( 0, tk. END)
        add_desc_entry. delete( 0, tk. END)
        add_code_text. delete( "1.0", tk. END)
        file_path_var. set( "")
        
# # # Gọi hàm làm mới
        refresh_all( )
    else:
        messagebox. showerror( "Lỗi", message)

def toggle_input_method( ):
# Chuyển đổi giữa hai chế độ nhập dự án
    if input_method_var. get( ) == "direct":
        file_frame. pack_forget()
        direct_frame. pack( fill = tk. BOTH, expand = True, padx = 10, pady = 10)
    else:
        direct_frame. pack_forget()
        file_frame. pack( fill = tk. BOTH, expand = True, padx = 10, pady = 10)

def browse_file():
# Mở hộp thoại chọn file
    file_path = filedialog. askopenfilename(
        title = "Chọn tệp mã nguồn",
        filetypes =[ ("Tệp văn bản", "*.txt"), ("Tất cả các tệp", "*.*")]
    )
    if file_path:
        file_path_var. set( file_path)


def on_delete_project_select( event):
# Xử lý sự kiện khi double-click vào một dự án trong tab Xóa
# # Lấy mục đã chọn
    selected_item = delete_projects_table. focus( )
    if not selected_item:
        return
# # Lấy giá trị của mục đã chọn
    values = delete_projects_table. item( selected_item, "values")
# # Đặt ID vào entry
    delete_entry. delete( 0, tk.END)
    delete_entry. insert( 0, values[0])  # ID

def handle_delete_project( ):
#  Xử lý khi nhấn nút Xóa dự án
# # Lấy ID hoặc tên
    id_or_name = delete_entry. get( ). strip( )
    if not id_or_name:
        messagebox. showerror( "Lỗi", "Vui lòng nhập ID hoặc Tên dự án!")
        return
# # Xác nhận xóa
    confirm = messagebox. askyesno(
        "Xác nhận", 
        f"Bạn có chắc chắn muốn xóa dự án '{ id_or_name}'?",
        icon = messagebox. WARNING
    )
    if not confirm:
        return
# # Gọi hàm xóa dự án
    success, message = delete_project(id_or_name)
# # Hiển thị kết quả
    if success:
        messagebox. showinfo( "Thành công", message)    
# # # Xóa dữ liệu đã nhập
        delete_entry.delete(0, tk.END)  
# # # Làm mới danh sách
        refresh_delete_list()  
# # # Gọi hàm làm mới các màn hình khác
        refresh_all()
    else:
        messagebox.showerror("Lỗi", message)
        
def load_project():
# Tải thông tin dự án khi nhấn nút Tải
# # Lấy ID đã chọn
    project_id = update_id_combo. get( )
    if not project_id:
        messagebox. showerror( "Lỗi", "Vui lòng chọn một ID dự án!")
        return
# # Tìm dự án
    success, row, message = search_projects( project_id)
    if not success:
        messagebox. showerror( "Lỗi", message)
        return
# # Điền thông tin
    update_name_entry. delete( 0, tk.END)
    update_name_entry. insert( 0, row[ 1])
    update_desc_entry. delete( 0, tk.END)
    update_desc_entry. insert( 0, row[ 2])
# # Lấy nội dung mã nguồn
    success, content, message = get_project_content( project_id)
    if not success:
        messagebox. showerror( "Lỗi", message)
        return
# # Hiển thị mã nguồn
    update_code_text. delete( "1.0", tk. END)
    if isinstance( content, str):
        update_code_text. insert( "1.0", content)
    else:
# # Nếu là binary, hiển thị thông báo
        update_code_text. insert( "1.0", "[Nội dung binary - không thể hiển thị]")

def handle_update_project( ):
#  Xử lý khi nhấn nút Cập nhật dự án
# # Lấy ID đã chọn
    project_id = update_id_combo. get( )
    if not project_id:
        messagebox. showerror( "Lỗi", "Vui lòng chọn một ID dự án!")
        return
# # Lấy thông tin đã cập nhật
    project_name = update_name_entry. get( ). strip( )
    project_desc = update_desc_entry. get( ). strip( )
    if not project_name:
        messagebox.showerror("Lỗi", "Tên dự án là bắt buộc!")
        return
# # Lấy mã nguồn
    code_content = update_code_text. get( "1.0", tk. END)
# # Gọi hàm cập nhật dự án
    success, message = update_project( project_id, project_name, project_desc, code_content)
# # Hiển thị kết quả
    if success:
        messagebox. showinfo( "Thành công", message)    
# # Gọi hàm làm mới các màn hình khác
        refresh_all()
    else:
        messagebox. showerror( "Lỗi", message)
def handle_search_projects():
# Xử lý khi nhấn nút Tìm kiếm
# # Lấy từ khóa
    keyword = search_entry. get( ). strip( )   
    if not keyword:
        messagebox. showinfo("Thông báo", "Vui lòng nhập từ khóa tìm kiếm!")
        return
# # Xóa kết quả cũ
    for item in search_results_table. get_children( ):
        search_results_table. delete( item)
# # Gọi hàm tìm kiếm
    success, results, message = search_projects( keyword)
# # Xóa nội dung xem trước
    preview_text. config( state = tk. NORMAL)
    preview_text. delete("1.0", tk. END)
    preview_text. config(state = tk. DISABLED)
# # Hiển thị kết quả
    if not success:
        messagebox. showinfo( "Kết quả", message)
        return
# # Hiển thị kết quả vào bảng
    for row in results:
        search_results_table. insert( "", tk. END, values = ( row[0], row[1], row[2]))

def on_search_result_select( event):
# Xử lý sự kiện khi chọn một dự án trong kết quả tìm kiếm
# # Lấy mục đã chọn
    selected_item = search_results_table. focus( )
    if not selected_item:
        return
# # Lấy giá trị của mục đã chọn
    values = search_results_table. item( selected_item, "values")
    project_id = values[ 0]
# # Lấy nội dung mã nguồn
    success, content, _ = get_project_content( project_id)
# # Hiển thị nội dung xem trước
    preview_text. config( state = tk. NORMAL)
    preview_text. delete( "1.0", tk. END)
    if success and isinstance( content, str):
        preview_text. insert( "1.0", content)
    elif success:
        preview_text. insert( "1.0", "[Nội dung binary - không thể hiển thị]")
    else:
        preview_text. insert( "1.0", "Không thể tải nội dung mã nguồn.")
    preview_text. config( state = tk. DISABLED)