from random import choice 

# activities that are queued up to satisfy the current greatest need
# [action, lvl_satisfied, time_reqd]
idle_activities = [["Idle", "reading the newspaper", 0, 1], ["Idle", "washing the dishes", 0, 2], ["Idle", "humming", 0, 1], ["Idle", "planning the next meal", 0, 1]]
hunger_activities = [["Hunger", "having a snack", 5, 1],["Hunger", "eating dinner", 7, 3]]
energy_activities = [["Energy", "sleeping", 8, 8]]
social_activities = [["Social", "chatting with a friend", 3, 2]]
bathroom_activities = [["Bathroom", "going pee", 6, 1], ["Bathroom", "having a tinkle", 6, 1], ["Bathroom", "taking a piss", 6, 1], ["Bathroom", "going poop", 6, 2]]


class ZIM:
    
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

        
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def age_up(self):
        self.age += 1
    
    needs_display = {
        "Bathroom": {
            "current_lvl": 0,
            "incrementer": 1,
            "threshold": 7
        },
        "Hunger": {
            "current_lvl": 0,
            "incrementer": 1.2,
            "threshold": 6
        },
        "Energy": {
            "current_lvl": 0,
            "incrementer": 0.5,
            "threshold": 8
        },
        "Social": {
            "current_lvl": 0,
            "incrementer": 0.75,
            "threshold": 5
        },
        "Idle": {
            "current_lvl": 1,
            "incrementer": 0,
            "threshold": 1
        }
    }
    
    task_q = []
    
    def update_needs(self, needs_display):
        #Dictionary version
        """ Loops through needs_display and 
        add the incrementer to the current_lvl to update the need"""
        for need, specs in needs_display.items():
            specs["current_lvl"] += specs["incrementer"]
        
        return needs_display

    
    def update_task_q(self, needs_display, task_q):
        # Dictionary version
        """ Loop through each need in needs_display,
        Compare current_lvl to threshold, 
        if current_lvl is over threshold,
        Update task_q with appropriate activity
        """
        if needs_display["Bathroom"]["current_lvl"] > needs_display["Bathroom"]["threshold"]:
            task_q.append(choice(bathroom_activities))
        elif needs_display["Hunger"]["current_lvl"] > needs_display["Hunger"]["threshold"]:
            task_q.append(choice(hunger_activities))
        elif needs_display["Energy"]["current_lvl"] > needs_display["Energy"]["threshold"]:
            task_q.append(choice(energy_activities))
        elif needs_display["Social"]["current_lvl"] > needs_display["Social"]["threshold"]:
            task_q.append(choice(social_activities))
        else:
            task_q.append(choice(idle_activities))
        
        return task_q


    def resolve_time_reqd_tasks(self,needs_display,task_q):
        """ Decrement time reqd of first item in task_q, 
        Remove if 0"""

        if task_q[0][3] <= 0:
            task_q.pop(0)
        task_q[0][3] -= 1

        return task_q

    def meet_needs(self,needs_display,task_q):
        """ Read the first item in the list, 
        turn first index into key to apply to neesd display"""
        being_met = task_q[0][0]
        needs_display[being_met]["current_lvl"] -= task_q[0][2]

        return needs_display

