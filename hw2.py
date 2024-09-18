from random import sample


def get_numbers_ticket(min_int, max_int, quantity):
    # Check for invalid arguments
    if not 1 <= min_int < max_int <= 1000:
        return []

    # Return a list of unique random integers using sample() method
    return sorted(sample(range(min_int, max_int + 1), quantity))
