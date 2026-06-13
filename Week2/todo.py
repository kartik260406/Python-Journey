import sys
from pathlib import Path
def main():
    if len(sys.argv) <2:
        sys.exit("Too few args")
    elif len(sys.argv)>2:
        sys.exit("Too many args")
    if not sys.argv[1].endswith(".txt"):
        sys.exit("Wrong file")
    valid_input = ["view tasks","add task","mark task done"]
    task = input("Enter the task from (view tasks,add task,mark task done): ").strip().lower()
    file_path = Path(sys.argv[1])
    file_found = True
    if not file_path.is_file():
        if task == valid_input[1]:
            file_found = False
            pass
        else:
            sys.exit("File not found")
    if task not in valid_input:
        raise ValueError("Wrong task entered")
    if task == valid_input[0]:
        tasks = view_task()
        for task in tasks:
            print(task,end = "")
    elif task == valid_input[1]:
        add_task(file_found)
        print("Task Done")
    elif task == valid_input[2]:
        mark_task()

def view_task():
    tasks = []
    with open(sys.argv[1]) as file:
        for line in file:
            tasks.append(line)
    return tasks

def add_task(file_found):
    task_to_add = input("Enter the tasks seperated by commas: ")
    args = [t.strip() for t in task_to_add.split(",")]
    if file_found:
        work = "a"
    else:
        work = "w"
    with open(sys.argv[1],work) as file:
        for task in args:
            file.write(task+"\n")

def mark_task():
    all_task = view_task()
    task_to_mark = input("Enter the task to mark: ").strip()
    with open(sys.argv[1],"w") as file:
        for task in all_task:
            stripped = task.strip()
            if stripped == task_to_mark:
                file.write("✅"+stripped+"\n")
            else:
                file.write(task)

if __name__ == "__main__":
    main()