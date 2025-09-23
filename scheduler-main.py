
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
        return str([event.name for event in self.events_list])
    
    def exists(self,event_name:str) -> int:
        for ind,event in enumerate(self.events_list):
            if event.name.lower()==event_name.lower():
                return ind
        return -1
    
    def check_conflict_datetime(self,event:Event) -> bool:
        for e in self.events_list:
            if e.date==event.date and e.time==event.time:
                return True
        return False
    
    def add_event(self, event:Event) -> bool:
        if self.check_conflict_datetime(event):
            print("Conflicting event found")
            return False
        if self.exists(event.name)==-1:
            self.events_list.append(event)
            return True
        print("Event already exists")
        return False
    
    def update(self, old_event_name:str,new_event:Event) -> bool:
        if self.check_conflict_datetime(new_event):
            print("Conflicting event found")
            return False
        ind=self.exists(old_event_name)
        if(ind!=-1):
            self.events_list=self.events_list[:ind]+[new_event]+self.events_list[ind+1:]
            return True
        print("Event does not exist")
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
        print("4. Show events")
        print("5. Exit")
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input, please enter a number")
            continue
        if choice==1:
            print("Add event details:")
            name=input("Event name:")
            date=input("Event date(dd:mm:yy):")
            time=input("Event time(hh:mm):")
            desc=input("Event description:")
            event=Event(name,date,time,desc)
            if scheduler.add_event(event):
                print("Event added successfully")
            else:
                print("Event not added")
        elif choice==2:
            print("Update event details:")
            old_name=input("Old event name:")
            name=input("New event name:")
            date=input("New event date(dd:mm:yy):")
            time=input("New event time(hh:mm):")
            desc=input("New event description:")
            event=Event(name,date,time,desc)
            if scheduler.update(old_name,event):
                print("Event updated successfully")
            else:
                print("Event not updated")
        elif choice==3:
            print("Remove event details:")
            name=input("Event name:")
            event=scheduler.delete_event(name)
            if event:
                print("Following event removed successfully: ",event)
            else:
                print("Event does not exist")
        elif choice==4:
            print("Available events: ",scheduler)
        elif choice==5:
            print("Exiting scheduler...\nHere are the events: ",scheduler)
            break

if __name__=="__main__":
    mainloop()