from zimz_class import ZIM

peter = ZIM("Peter", "Zim", 32)
polina = ZIM("Polina", "Zim", 27)


def main():
    """ Main Game loop --
    - Displays Peter's needs
    - Display the task q
    - Counts up time
    - Update Peter's needs
    - 'Meets needs' by adding to task q
    """
    TIME = 0

    while True:
        """One loop is a moment/turn"""

        print(f"The time is: {TIME}.")
        print(f"Peter's Needs: {peter.needs_display}")
        print(f"Peter's Tasks: {peter.task_q}")


        peter.update_needs(peter.needs_display)
        # If nothing in task_q, add something
        # if len(peter.task_q) == 0:
        peter.update_task_q(peter.needs_display, peter.task_q)
        # If nothing in task_q, don't update time reqd
        # if len(peter.task_q) > 0:
        # peter.resolve_time_reqd_tasks(peter.needs_display, peter.task_q)

        TIME += 1

        input("> ")
        print()

main()