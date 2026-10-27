# Danh sách lưu các công việc dưới dạng dictionary
tasks = []

def add_task(task_name):
    """Thêm một công việc mới dưới dạng dictionary."""
    tasks.append({'name': task_name, 'completed': False})

def complete_task(task_index):
    """Đánh dấu công việc tại vị trí task_index là hoàn thành."""
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True

def list_tasks():
    """Hiển thị danh sách công việc kèm trạng thái [x] hoặc [ ]."""
    print("Danh sách công việc:")
    for index, task in enumerate(tasks, start=1):
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{index}. {status} {task['name']}")

if __name__ == "__main__":
    # Thêm công việc mẫu
    add_task("Học bài Git")
    add_task("Làm bài tập")
    
    # Đánh dấu công việc đầu tiên là hoàn thành
    complete_task(0)
    
    # Gọi hàm hiển thị danh sách
    list_tasks()