import random 

# activities that are queued up to satisfy the current greatest need
# [action, lvl_satisfied, time_reqd]
idle_activities = [["Idle", "reading the newspaper", 0, 1], ["Idle", "washing the dishes", 0, 2], ["Idle", "humming", 0, 1], ["Idle", "planning the next meal", 0, 1]]
hunger_activities = [["Hunger", "having a snack", 5, 1],["Hunger", "eating dinner", 7, 3]]
energy_activities = [["Energy", "sleeping", 8, 8]]
social_activities = [["Social", "chatting with a friend", 3, 2]]
bathroom_activities = [["Bathroom", "going pee", 7, 1], ["Bathroom", "having a tinkle", 7, 1], ["Bathroom", "taking a piss", 7, 1], ["Bathroom", "going poop", 7, 2]]


class ZIM:
    
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

        
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def age_up(self):
        self.age += 1

    # [need, current_lvl, incrementer, threshold]
    # needs_display = [["Bathroom", 0, 1, 7], 
    #         ["Hunger", 0, 1.2, 6], 
    #         ["Energy", 0, 0.5, 8], 
    #         ["Social", 0, 0.75, 5], 
    #         ["Idle", 1, 0, 1]]
    
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

    # def update_needs(self, needs_display):
    #     # List version
    #     """ Loops through needs_display and 
    #     add the incrementer to the current_lvl to update the need"""
    #     for sublist in needs_display:
    #         sublist[1] += sublist[2] 
    #     return needs_display
    
    def update_needs(self, needs_display):
        #Dictionary version
        for need, specs in needs_display.items():
            specs["current_lvl"] += specs["incrementer"]
        return needs_display





    # Can I simplify this to look through the needs once and pull from appropriate list? 
    def update_task_q(self, needs_display, task_q):
        """ Loop through each need in needs_display,
            Compare current_lvl to threshold, if current_lvl is over threshold,
            Update task_q with appropriate activity
            """
        if needs_display[0][1] >= needs_display[0][3]:
            task_q.append(random.choice(bathroom_activities))
        elif needs_display[1][1] >= needs_display[1][3]:
            task_q.append(random.choice(hunger_activities))
        elif needs_display[2][1] >= needs_display[2][3]:
            task_q.append(random.choice(energy_activities))
        elif needs_display[3][1] >= needs_display[3][3]:
            task_q.append(random.choice(social_activities))
        # only add idle action if no items in task_q...
        else:
            task_q.append(random.choice(idle_activities))

        return task_q
    
    def resolve_time_reqd_tasks(self,needs_display,task_q):
        """ Decrement time reqd of first item in task_q, 
        Apply amnt of need fulfilled to needs_display
        Remove if 0"""
        # task_q[0] = current_activity
        # task_q[0][0] = need_fullfilment_type
        task_q[0][3] -= 1
        if task_q[0][3] <= 0:
            task_q.pop(0)
        # USE DICT TO APPLY TO NEEDS! MAKE NEEDS A DICT??
        return needs_display, task_q

    def meet_needs2(self,needs_display,task_q):
        pass



    def meet_needs(self, needs_display, task_q):
        """ Checks if the 1st item in the task_q matches the first index of a need,
        Decrement the lvl_satisfied from current_lvl
        if the time required is 0, remove

        I DONT THINK THIS WORKS """
        for sublist in range(len(needs_display)):
            # apply the lvl_satisfied to the needs_display
            # decrease time_reqd
            # if time_reqd <= 0, remove item
            if task_q[0][1] == needs_display[sublist][0]:
                needs_display[sublist][1] -= task_q[0][2]
                task_q[0][3] -=1
                if task_q[0][3] == 0:
                    task_q.pop(0)


