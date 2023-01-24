# from functions import get_todos, save_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()
            
        todos.append(todo)

        functions.save_todos(todos)
            
    elif user_action.startswith("show"):            
        
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index  + 1}. {item}")

    elif user_action.startswith("edit"):
        try:      
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Please input new todo: ")
            todos[number] = new_todo + '\n'

            functions.save_todos(todos)
        except ValueError:
            print("Command Invalid. Please try again.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
                
            todos = functions.get_todos()
            index = number - 1
            task_to_remove = todos[index].strip('\n')
            todos.pop(number - 1)

            functions.save_todos(todos)

            print(f'Todo {task_to_remove} has been removed.')    

        except:
            print("Command Invalid. Please try again.")
            continue

    elif 'exit' in user_action:
            break

    else:
        print("Command invalid. Please Try again.")

print("Bye!")