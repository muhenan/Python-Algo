class Solution:
    def hello(self):
        print("hellp")

def fizzBuzz(n):
    # Write your code here
    for i in range(1, n+1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

def buyVolumes(volumes):
    # Write your code here
    volumes_size = len(volumes)
    my_arr = [-1] * volumes_size
    index = 0
    for num in volumes:
        my_arr[num-1] = 0


def find_daily_purchases(n):
    """
    Determines which volumes can be purchased each day based on the rules:
    1. Can't purchase a volume that's already been purchased
    2. Must own all prequels before purchasing a volume

    Args:
        n (int): Total number of volumes

    Returns:
        List[List[int]]: List of n arrays where i-th array contains volumes purchased on day i
    """
    # Initialize variables
    purchased = set()  # Keep track of purchased volumes
    result = []  # Store daily purchases

    for day in range(n):
        daily_purchases = []

        # Check each volume from 1 to n
        for vol in range(1, n + 1):
            # Skip if already purchased
            if vol in purchased:
                continue

            # Check if all prequels are owned
            can_purchase = True
            for prequel in range(1, vol):
                if prequel not in purchased:
                    can_purchase = False
                    break

            # If we can purchase this volume, add it to today's purchases
            if can_purchase:
                daily_purchases.append(vol)

        # Update purchased set with today's purchases
        purchased.update(daily_purchases)
        # Add today's purchases to result
        result.append(daily_purchases)

    return result


def find_daily_purchases2(stock_sequence):
    """
    Determines which volumes can be purchased each day based on:
    1. What's available in stock that day (given by stock_sequence)
    2. Can't purchase a volume that's already been purchased
    3. Must own all prequels before purchasing a volume
    4. Returns [-1] for days where no purchase is possible

    Args:
        stock_sequence (List[int]): Sequence of volumes coming into stock each day

    Returns:
        List[List[int]]: List of n arrays where i-th array contains volumes purchased on day i,
                         or [-1] if no purchase is possible that day
    """
    n = len(stock_sequence)
    purchased = set()  # Keep track of purchased volumes
    available = set()  # Keep track of what's in stock
    result = []

    for day in range(n):
        # Add today's volume to available stock
        current_vol = stock_sequence[day]
        available.add(current_vol)

        # Try to purchase volumes
        can_purchase = []

        # Check each available volume
        for vol in sorted(available):  # Sort to ensure we try volumes in order
            if vol in purchased:
                continue

            # Check if all prequels are owned
            has_all_prequels = True
            for prequel in range(1, vol):
                if prequel not in purchased:
                    has_all_prequels = False
                    break

            # If we can purchase this volume
            if has_all_prequels:
                can_purchase.append(vol)
                purchased.add(vol)

        # If we couldn't purchase anything today, add [-1], otherwise add the sorted purchases
        result.append([-1] if not can_purchase else sorted(can_purchase))

    return result


def findSecurityCode(code, k):
    """
    Optimized solution for finding security code after k transformations.
    Instead of simulating each step, we calculate the final state directly.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(code)
    code = list(code)

    # Find the position of the leftmost '0' followed by '1'
    # and count how many steps needed for one complete transformation
    steps_needed = 0
    left_zeros = []  # Store positions of zeros

    # First pass: count total transformations needed
    for i in range(n):
        if code[i] == '0':
            # Count how many 1s are to the left of this 0
            ones_before = 0
            for j in range(i):
                if code[j] == '1':
                    ones_before += 1
            # Each 1 before this 0 represents a necessary swap
            steps_needed += ones_before

    # If k is less than steps needed, we need to simulate
    if k < steps_needed:
        # Reset code and simulate only k steps
        code = list(code)
        done = 0
        while done < k:
            for i in range(n - 1):
                if code[i] < code[i + 1]:
                    code[i], code[i + 1] = code[i + 1], code[i]
                    done += 1
                    break
    else:
        # We can achieve the maximum string
        # Sort in descending order (all 1s followed by all 0s)
        code.sort(reverse=True)

    return ''.join(code)

def findSecurityCode22(code, k):
    count_ones = code.count('1')
    one_indexs = [-1] * count_ones
    index_of_one_indexs = 0
    my_length = len(code)
    for i in range(my_length):
        if code[i] == '1':
            one_indexs[index_of_one_indexs] = i
            index_of_one_indexs += 1
    ##print(one_indexs)
    for i in range(len(one_indexs)):
        if k == 0:
            break
        max1 = 0
        if i == 0:
            max1 = one_indexs[i]
        else:
            max1 = one_indexs[i] - one_indexs[i-1] - 1
        max_value = min(max1, k)
        one_indexs[i] -= max_value
        k -= max_value
    ##print(one_indexs)
    # Generate the final string using the new positions
    result = ['0'] * my_length
    for pos in one_indexs:
        result[pos] = '1'
    ##print(result)
    return ''.join(result)


#print(find_daily_purchases2([1,4,3,2,5]))

findSecurityCode22('0010', 5)