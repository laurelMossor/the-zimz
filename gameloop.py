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
        print(peter.needs_display)
        print(peter.task_q)

        TIME += 1

        peter.update_needs(peter.needs_display)
        peter.update_task_q(peter.needs_display, peter.task_q)
        peter.meet_needs(peter.needs_display, peter.task_q)


        input("> ")

main()