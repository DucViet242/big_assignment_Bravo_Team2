import hashlib

''' Tính toán mã hash SHA-256 cho nội dung file'''
def calculate_file_hash(file):
    try: 
        with open(file, 'rb') as F:
            hash_object = hashlib.sha256()
            # Đọc file theo chunks để xử lý file lớn
            while chunk := F.read(8192):
                hash_object.update(chunk)
        # Convert hash object sang string
        hash_value = hash_object.hexdigest()
        return True, hash_value, f'Đã tính hash thành công'
    except Exception as E:
        return False, None, f'Lỗi tính toán hash: {E}'

''' So sánh mã hash để so sánh tính toàn vẹn xem file đã bị chỉnh sửa bên ngoài chưa'''
def verify_file_integrity(file, expected_hash):
    success, actual_hash, message = calculate_file_hash(file)
    if not success:
        return False, False, message
    
    if actual_hash == expected_hash:
        return True, True, f'File còn nguyên vẹn'
    else:
        return True, False, f'File không còn nguyên vẹn'