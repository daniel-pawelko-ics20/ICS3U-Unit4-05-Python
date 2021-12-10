#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Dec 2021
# Continue keyword


def main():
    # main function for creating adding program

    # defining variables
    total_sum = 0
    # asking for input
    total_nums = input("How many numbers would you like to add: ")
    total_nums = int(total_nums)

    # process/input
    for number in range(total_nums):
        temp_num = input("Enter a number to add: ")
        temp_num = int(temp_num)
        if temp_num <= 0:
            continue
        total_sum += temp_num

    # output
    print(f"Sum of just the positive numbers is = {total_sum}")

    # done
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
