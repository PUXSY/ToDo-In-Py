import json
import os
from typing import List, Dict, Union

class TodoList:
    def __init__(self) -> None:
        self.tasks: List[Dict[str, Union[str, bool]]] = []
        self.json_handler = JsonHandler()

    def add_task(self, task: str) -> None:
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added successfully!")
        self.save_list()  

    def view_tasks(self) -> None:
        if not self.tasks:
            print("No tasks in the list!")
            return
        
        print("\nTODO LIST:")
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else " "
            print(f"{i}. [{status}] {task['task']}")

    def mark_completed(self, task_number: int) -> None:
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number-1]["completed"] = True
            print(f"Task {task_number} marked as completed!")
            self.save_list()  
        else:
            print("Invalid task number!")

    def remove_task(self, task_number: int) -> None:
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number-1)
            print(f"Task '{removed_task['task']}' removed successfully!")
            self.save_list()  
        else:
            print("Invalid task number!")

    def load_list(self) -> None:
        loaded_tasks = self.json_handler.load_list()
        if loaded_tasks is not None:
            self.tasks = loaded_tasks

    def save_list(self) -> None:
        self.json_handler.save_list(self.tasks)


class JsonHandler:
    def __init__(self) -> None:
        self.json_path = os.path.join(os.path.expanduser("C:\\temp"), "todo.json")
        self._ensure_directory_exists()

    def _ensure_directory_exists(self) -> None:
        directory = os.path.dirname(self.json_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

    def jason_exists(self) -> bool:
        if not os.path.exists(self.json_path):
            print("No existing todo list found. Starting fresh!")
            return False
    
    def load_list(self) -> Union[List[Dict[str, Union[str, bool]]], None]:
        try:

            if not self.jason_exists():
                return []
            
            with open(self.json_path, "r") as file:
                tasks = json.load(file)
                print("List loaded successfully!")
                return tasks
                
        except json.JSONDecodeError:
            print("Error reading JSON file. Starting fresh!")
            return []
        except Exception as e:
            print(f"An error occurred while loading: {str(e)}")
            return None

    def save_list(self, tasks: List[Dict[str, Union[str, bool]]]) -> None:
        try:
            with open(self.json_path, "w") as file:
                json.dump(tasks, file, indent=2)
            print("List saved successfully!")
        except Exception as e:
            print(f"Error saving list: {str(e)}")


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")

def main() -> None:
    todo = TodoList()
    todo.load_list()
    baner:str = """
        ,----,
      ,/   .`|
    ,`   .'  :            ,---,               
  ;    ;     /          .'  .' `\\             
.'___,/    ,'  ,---.  ,---.'     \\    ,---.   
|    :     |  '   ,'\\ |   |  .`\\  |  '   ,'\\  
;    |.';  ; /   /   |:   : |  '  | /   /   | 
`----'  |  |.   ; ,. :|   ' '  ;  :.   ; ,. : 
    '   :  ;'   | |: :'   | ;  .  |'   | |: : 
    |   |  ''   | .; :|   | :  |  ''   | .; : 
    '   :  ||   :    |'   : | /  ; |   :    | 
    ;   |.'  \\   \\  / |   | '` ,/   \\   \\  /  
    '---'     `----'  ;   :  .'      `----'   
                      |   ,.'                 
                      '---'
"""
    
    try:
        print(baner)
        while True:
            print("\n1. Add task")
            print("2. View tasks")
            print("3. Mark task as completed")
            print("4. Remove task")
            print("5. Exit")  

            choice = input("\nEnter your choice (1-5): ")

            if choice == "1":
                clear_screen()
                task = input("Enter task: ")
                todo.add_task(task)

            elif choice == "2":
                clear_screen()
                todo.view_tasks()

            elif choice == "3":
                clear_screen()
                todo.view_tasks()
                try:
                    task_num = int(input("Enter task number to mark as completed: "))
                    todo.mark_completed(task_num)
                except ValueError:
                    print("Please enter a valid number!")

            elif choice == "4":
                clear_screen()
                todo.view_tasks()
                try:
                    task_num = int(input("Enter task number to remove: "))
                    todo.remove_task(task_num)
                except ValueError:
                    print("Please enter a valid number!")

            elif choice == "5":
                print("Goodbye!")
                break
            
            else:
                clear_screen()
                print("Invalid choice! Please try again.")
                
    except KeyboardInterrupt:
        print("\nGoodbye!")


if __name__ == "__main__":
    main()