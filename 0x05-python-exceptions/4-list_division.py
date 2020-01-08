#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    resul_list = []
    for count in range(list_length):
        try:
            list_div = (my_list_1[count] / my_list_2[count])
        except ZeroDivisionError:
            list_div = 0
            print("division by 0")
        except TypeError:
            list_div = 0
            print("wrong type")
        except IndexError:
            list_div = 0
            print("out of range")
        finally:
            resul_list.append(list_div)
    return resul_list
