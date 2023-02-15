def broom_closet():
    print("You enter a broom closet. It seems normal. There is a broom in one of the corners")
    answer = input("Do you want to stay in the broom closet? (1: Yes, 2: No leave broom closet): ")

    while True:
        if answer == "2":
            print("You leave the broom closet.")
            return

        elif answer == "1":
            print("What did you expect? It's a normal broom closet.")
            answer = input("Do you want to leave the broom closet? (1: Yes, 2: No): ")
            while True:
                if answer == "1":
                    print("You leave the broom closet.")
                    return

                elif answer == "2":
                    print("After some time, the broom in the corner falls over by itself.")
                    answer = input("What do you want to do? (1: Take up the broom, 2: Do nothing, 3: Leave broom closet): ")
                    while True:
                        if answer == "1":
                            print("You pick up the broom and place it back to where it was.")
                            while True:
                                stay_answer = input("Do you still want to stay in the closet? (1: Yes, 2: No): ")
                                if stay_answer == "1":
                                    print("...")
                                    continue
                                elif stay_answer == "2":
                                    print("You leave the broom closet.")
                                    return
                                else:
                                    print("This is not a choice. Please choose 1 or 2.")
                        elif answer == "2":
                            print("You stay in the broom closet with the broom on the floor.")
                            while True:
                                stay_answer = input("Do you still want to stay in the closet? (1: Yes, 2: No): ")
                                if stay_answer == "1":
                                    print("...")
                                    continue
                                elif stay_answer == "2":
                                    print("You leave the broom closet.")
                                    return
                                else:
                                    print("This is not a choice. Please choose 1 or 2.")
                        elif answer == "3":
                            print("You leave the broom closet.")
                            return
                        else:
                            print("This is not a choice. Please choose 1, 2, or 3.")
                            answer = input("What do you want to do? (1: Take up the broom, 2: Do nothing, 3: Leave broom closet): ")
                            continue
                    if answer == "3":
                        break
                    else:
                        continue
                else:
                    print("This is not a choice. Please choose 1 or 2.")
                    answer = input("Do you want to leave the broom closet? (1: Yes, 2: No): ")
                    continue
        else:
            print("This is not a choice. Please choose 1 or 2.")
            answer = input("Do you want to stay in the broom closet? (1: Yes, 2: No leave broom closet): ")
            continue

if __name__ == "__main__":
    broom_closet()
