# todo.py

class ToDoList:
    def __init__(self):
        self.tasks = []  # Listeyi başlatıyoruz

    def add_task(self, task):
        self.tasks.append({'task': task, 'done': False})  # Yeni görev ekliyoruz

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)  # Verilen index'teki görevi listeden siliyoruz
        else:
            print("Geçersiz görev index'i!")

    def mark_done(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['done'] = True  # Görevi tamamlanmış olarak işaretliyoruz
        else:
            print("Geçersiz görev index'i!")

    def show_tasks(self):
        if not self.tasks:
            print("Yapılacak işler listesi boş!")
        else:
            for idx, task in enumerate(self.tasks):
                status = "✓" if task['done'] else "✗"
                print(f"{idx + 1}. {task['task']} [{status}]")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\n--- To-Do List ---")
        print("1. Yapılacak iş ekle")
        print("2. Yapılacak işleri göster")
        print("3. Yapılan işi işaretle")
        print("4. Yapılacak işi sil")
        print("5. Çıkış")

        choice = input("Bir işlem seçin (1/2/3/4/5): ")

        if choice == '1':
            task = input("Yapılacak işi girin: ")
            todo_list.add_task(task)
            print(f"'{task}' eklendi.")

        elif choice == '2':
            todo_list.show_tasks()

        elif choice == '3':
            todo_list.show_tasks()
            task_index = int(input("Tamamlanan işin sırasını girin: ")) - 1
            todo_list.mark_done(task_index)
            print("İşaretlendi.")

        elif choice == '4':
            todo_list.show_tasks()
            task_index = int(input("Silmek istediğiniz işin sırasını girin: ")) - 1
            todo_list.remove_task(task_index)
            print("Silindi.")

        elif choice == '5':
            print("Çıkılıyor...")
            break

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
