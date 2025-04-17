import todo

def main():
    while True:
        print("\nTo-Do List")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            todo.view_tasks()
        elif choice == "2":
            task = input("Enter a new task: ")
            todo.add_task(task)
        elif choice == "3":
            task = input("Enter task to remove: ")
            todo.remove_task(task)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
