from zimz_class import ZIM

peter = ZIM("Peter", "Zim", 32)
polina = ZIM("Polina", "Zim", 27)


TIME = 0

while True:
    # every loop is a turn/moment
    # every turn;
        # display needs
        # time increments by 1
        # hunger and bathroom level decrement
        # there is an action

    print(f"The time is: {TIME}.")
    print(peter.needs_display)
    print(peter.task_q)

    TIME += 1

    peter.update_needs(peter.needs_display)
    peter.update_task_q(peter.needs_display, peter.task_q)
    peter.meet_needs(peter.needs_display, peter.task_q)


    input("> ")