import statistics as s


def correct_len (list):
    """Ensures the lists are the same len."""

    if len(set(map(len, list))) <= 1:
        print(f"All items are equal length.")
    else:
        print(f"The lists are not the same length.")



def list_average (list):
    """ Returns the average of the list given."""
    average = sum(list) / len(list)
    print(f" --AVG:  {round(average, 0)}")

def s_dev(list): # Std.Deviation
    print(f"S.DEV:  {s.stdev(list)}")
