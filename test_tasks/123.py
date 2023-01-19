import json
import requests


def pars_and_paste (test_dict, value_dict):
    for number in range(len(value_dict['values'])):
        # print(value['values'][number])
        if (value_dict['values'][number]['id'] == test_dict['id']):
            # print(list_of_tests[test])
            test_dict['value'] = value_dict['values'][number]['value']
            #print(test_dict)
            return test_dict

def full_perebor (test_dict, value_dict):
    test_dict = pars_and_paste(test_dict, value_dict)
    print(test_dict)
    if (len(test_dict)==4):
        for test_values in test_dict['values']:
            print(test_values)
            full_perebor(test_values, value_dict)



with open("values.json", "r") as values_file:
    value_dict = json.load(values_file)

    with open("tests.json", "r") as read_file:
        tests = json.load(read_file)
        list_of_tests = tests['tests']
        #print(type(tests))
        for test in list_of_tests:
            #print(test)
            full_perebor(test, value_dict)









    #for _ in id_generator(data):
     #   print(_)