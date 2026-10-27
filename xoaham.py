# Danh sách lưu các công việc dưới dạng dictionary
tasks = []

def add_task(task_name):
    """Thêm một công việc mới dưới dạng dictionary."""
    tasks.append({'name': task_name, 'completed': False})

def complete_task(task_index):
    """Đánh dấu công việc tại vị trí task_index là hoàn thành."""
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True

def delete_task(task_index):
    """Xóa một công việc khỏi danh sách theo chỉ số task_index."""
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Đã xóa công việc: {removed_task['name']}")
    else:
        print("Chỉ số công việc không hợp lệ!")

def list_tasks():
    """Hiển thị danh sách công việc kèm trạng thái [x] hoặc [ ]."""
    print("Danh sách công việc:")
    for index, task in enumerate(tasks, start=1):
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{index}. {status} {task['name']}")

if __name__ == "__main__":
    # Thêm các công việc mẫu
    add_task("Học bài Git")
    add_task("Làm bài tập")
    add_task("Đọc tài liệu")
    
    # Đánh dấu công việc 1 hoàn thành
    complete_task(0)
    
    # Xóa công việc 2 (Làm bài tập - chỉ số 1)
    delete_task(1)
    
    # In lại danh sách
    list_tasks()