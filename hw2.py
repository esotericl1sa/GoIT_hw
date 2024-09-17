from random import sample


def get_numbers_ticket(min_int, max_int, quantity):
    # Check for invalid arguments
    if min_int > max_int or quantity <= 0 or quantity > (max_int - min_int + 1):
        return []

    # Return a list of unique random integers using sample() method
    return sample(range(min_int, max_int + 1), quantity)
