import hashlib

''' Tính toán mã hash SHA-256 cho nội dung file'''
def calculate_file_hash( file):
    try: 
        with open ( file, 'rb') as F:
            hash_value = hashlib. file_digest( F, "sha256")
        return True, hash_value, f' Đã tính hash thành công'
    except Exception as E:
        return False, None, f' Lỗi tính toán hash'

''' So sánh mã hash để so sánh tính toàn vẹn xem file đã bị chỉnh sửa bên ngoài chưa'''
def verify_file_integrity( file, expected_hash):
    success, actual_hash, message = calculate_file_hash( file)
    if not success:
        return False, False, None
    
    if actual_hash == expected_hash:
        return True, True, f' File còn nguyên vẹn'
    else:
        return True, False, f' File không còn nguyên vẹn'

