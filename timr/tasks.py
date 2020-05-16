import threading

class Tasks():
    tasklist = []
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def add_task(self):
        if (len(self.tasklist)<4):
            newtask = {'name':self.name, 'duration': self.duration}
            self.tasklist.append(newtask)
            print(f"task saved with id: {len(self.tasklist)}")
        else:
            print("Limit of 4 tasks reached already!!!")
    
    def show_tasks(self):
        for item in self.tasklist:
            taskname = item['name']
            tasktime = item['duration']
            print(f"{taskname}:{tasktime}")


    def initiate(self):
        self.show_tasks()
        id = int(input("Enter the task id you want to initiate: "))
        print(f"Are you sure you want to initiate {self.tasklist[id]['name']} for {self.tasklist[id]['duration']} minutes?")
        time = int(self.tasklist[id]['duration'])
        self.timer = threading.Timer(time*10, None)
        choice = input()
        if (choice.lower() == 'yes'):
            self.timer.start()
            print("task initiated successfully")
            exit
        else:
            print("Ok, terminating timer start")

    def showtime(self, id):
        print(f"task {self.name} still has {self.duration} minutes to go!!")

    def end_task(self, id):
        print(f"Are you sure you want to end the timer for {self.tasklist[id]}")
        endchoice = input()
        if(endchoice.lower() == 'yes'):
            print("cancelling timer")
            self.timer.cancel()
        else:
            pass

    def empty_list(self):
        print("Are you sure you want to delete all your timers?")
        choicempty = input()
        if(choicempty.lower() == "yes"):
            self.tasklist.clear()
        else:
            pass

def add(name, duration):
    Task = Tasks(name, duration)
    Task.add_task()
    Task.show_tasks()
    Task.initiate()

print("Welcome to timr, add a new task")

for i in range(4):
    print("Want to add a task?")
    answer = input()
    if (answer.lower()=="yes"):
        name = input("Enter the name of the task: ")
        duration = input("Enter the duration of the task: ")
        add(name, duration)
    else:
        exit()