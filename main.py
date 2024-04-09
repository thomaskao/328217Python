
import client
import socket 
from AddStu import AddStu
from PrintAll import PrintAll
from client import SocketClient


host = "127.0.0.1"
port = 20001


          
def send_add(client_main):
    parameters = AddStu().execute()
    client_main.send_command('add', parameters)
    data = client_main.wait_response()
    print(f"The client received data => {data}")
    if data['status'] == 'OK':
        print(f"Add {parameters} success")
    else:
        print(f"Add {parameters} fail")

def send_show(client_main):
    client_main.send_command('show', {})
    data = client_main.wait_response()
    print(f"The client received data => {data}")
    student_dict = data["parameters"]
    PrintAll().execute(student_dict)

def print_menu():
    print()
    print("add: Add a student's name and score")
    print("show: Print all")
    print("exit: Exit")
    selection = input("Please select: ")

    return selection


action_list = {
    "add": send_add, 
    "show": send_show
}
def main():
    client_main = client.SocketClient(host,port)
    select_result = "initial"

    while select_result != "exit":
        select_result = print_menu()
        try:
            action_list[select_result](client_main)
        except Exception as e:
            print(e)
main()