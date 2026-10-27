# Danh sách lưu các công việc dưới dạng dictionary
tasks = []

def add_task(task_name):
    """Thêm một công việc mới với trạng thái hoàn thành mặc định là False."""
    task = {'name': task_name, 'completed': False}
    tasks.append(task)
    print(f"Đã thêm công việc: '{task_name}'")

def complete_task(task_index):
    """Đánh dấu một công việc là đã hoàn thành dựa vào chỉ số (index)."""
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f"Đã hoàn thành công việc: '{tasks[task_index]['name']}'")
    else:
        print("Chỉ số công việc không hợp lệ!")

def list_tasks():
    """Hiển thị danh sách công việc kèm trạng thái."""
    print("\n--- DANH SÁCH CÔNG VIỆC ---")
    for index, task in enumerate(tasks):
        status = "x" if task['completed'] else " "
        print(f"{index}. [{status}] {task['name']}")
    print("-" * 28)

# --- Điểm bắt đầu chương trình ---
if __name__ == "__main__":
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    
    # Đánh dấu công việc đầu tiên (index 0) là đã hoàn thành
    complete_task(0)
    
    # Hiển thị lại danh sách
    list_tasks()