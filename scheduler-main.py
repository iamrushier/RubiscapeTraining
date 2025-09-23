
class Event:
    def __init__(self,name:str,date:str,time:str,description:str):
        self.name=name
        self.date=date
        self.time=time
        self.description=description
    
    def __str__(self):
        return f"Event: {self.name}\nDate: {self.date}\nTime: {self.time}\nDescription: {self.description}"
        
class Scheduler:
    def __init__(self):
        self.events_list=[]
    def __str__(self):
        return self.events_list
    
    def exists(self,event_name:str) -> int:
        for ind,event in enumerate(self.events_list):
            if event.name.lower()==event_name.lower():
                return ind
        return -1
    
    def add_event(self, event:Event) -> bool:
        if self.exists(event.name)==-1:
            self.events_list.append(event)
            return True
        return False
    
    def update(self, old_event:Event,new_event:Event) -> bool:
        ind=self.exists(old_event.name)
        if(ind!=-1):
            self.events_list=self.events_list[:ind]+[new_event]+self.events_list[ind+1:]
            return True
        return False
        
    
    def delete_event(self, event_name:str) -> Event:
        ind=self.exists(event_name)
        if(ind!=-1):
            return self.events_list.pop(ind)
        return None
    
    

def mainloop():
    scheduler=Scheduler()
    while True:
        print("=================================================")
        print("Scheduler options: ")
        print("1. Add event")
        print("2. Update event")
        print("3. Remove event")
        print("4. Exit")
        choice=int(input("Enter choice:"))
        if choice==1:
            print("Add event details:")
            name=input("Event name:")
            date=input("Event date:")
            time=input("Event time:")
            desc=input("Event description:")
            event=Event(name,date,time,desc)
            if scheduler.add_event(event):
                print("Event added successfully")
            else:
                print("Event with this name already exists")
        elif choice==2:
            event=Event()
            pass
        elif choice==3:
            pass
        elif choice==4:
            print("Exiting scheduler...\nHere are the events: ",scheduler)
            break
        else:
            continue

if __name__=="__main__":
    # mainloop()
    pass

sched=Scheduler()
event1=Event("one","222","44","one desc")
event2=Event("two","222","44","one desc")
event3=Event("three","222","44","one desc")
sched.add_event(event1)