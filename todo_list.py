tasks = []

# Add task  function
def add_task(task):
    tasks.append({'task': task, 'completed': False})
    print(f'Task "{task}" added!')

# View task function
def view_tasks():
    if not tasks:
        print('No tasks available.')
    else:
        print('\nTo-Do List:')
        for i, task in enumerate(tasks, start=1):
            status = 'Completed' if task['completed'] else 'Incomplete'
            print(f'{i}. [{status}] {task["task"]}')

# Mark task as completed function
def mark_completed(task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True
        print(f'Task {task_number} marked as completed!')
    else:
        print('Invalid task number.')

# Delete task function
def delete_task(task_number):
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f'Task "{removed_task["task"]}" deleted!')
    else:
        print('Invalid task number.')

# Main function
def main():
    while True:
        print('\nTo-Do List Menu:') # Menu options
        print('1. Add Task')
        print('2. View Tasks')
        print('3. Mark Task as Completed')
        print('4. Delete Task')
        print('5. Exit')
        
        choice = input('Enter your choice: ')
        
        if choice == '1':
            task = input('Enter the task: ')
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            task_number = int(input('Enter task number to mark as completed: '))
            mark_completed(task_number)
        elif choice == '4':
            view_tasks()
            task_number = int(input('Enter task number to delete: '))
            delete_task(task_number)
        elif choice == '5':
            print('Exiting program. Goodbye!')
            break
        else:
            print('Invalid choice, please try again.')

if __name__ == '__main__':
    main()
