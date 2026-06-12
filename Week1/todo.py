import sys
from pathlib import Path
def main():
    if len(sys.argv) <2:
        sys.exit("Too few args")
    elif len(sys.argv)>2:
        sys.exit("Too many args")
    if not sys.argv[1].endswith(".txt"):
        sys.exit("Wrong file")
    valid_input = ["view tasks","add task","mark test done"]
    task = input("Enter the task from (view tasks,add task,mark test done): ").strip().lower()
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
        print(view_task)
    elif task == valid_input[1]:
        add_task(file_found)
        print("Task Done")
    

def view_task():
    tasks = []
    with open(sys.argv[1]) as file:
        for line in file:
            tasks.append(line)
    return tasks

def add_task(*args,file_found):
    task_to_add = input("Enter the tasks seperated by commas: ")
    args = task_to_add.split(",").strip()
    if file_found:
        work = "a"
    else:
        work = "w"
    with open(sys.argv[1],work) as file:
        for task in args:
            file.write(task,end = "")

def mark_task():
    all_task = view_task()
    test_to_mark = input("Enter the task to mark: ")
    with open(sys.argv[1],"w") as file:
        for task in all_task:
            file.write(task,end = "")
            if task == test_to_mark:
                file.write("✅",end = "")

if __name__ == "__main__":
    main()