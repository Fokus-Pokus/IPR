import json

def pars_and_paste (list_of_tests, value):
    for test in range(len(list_of_tests)):
        # print(list_of_tests[test])
        for number in range(len(value['values'])):
            # print(value['values'][number])
            if (value['values'][number]['id'] == list_of_tests[test]['id']):
                # print(list_of_tests[test])
                list_of_tests[test]['value'] = value['values'][number]['value']
                #print(list_of_tests[test])

def id_generator(dict_var):
    for k, v in dict_var.items():
        print(k)
        if k == "tests":
            yield v
        elif isinstance(v, dict):
            for id_val in id_generator(v):
                yield id_val


with open("tests.json", "r") as read_file:
    tests = json.load(read_file)
    list_of_tests = tests['tests']
    print(type(tests))
    for _ in id_generator(tests):
        print(_)
    with open("values.json", "r") as values_file:
        value = json.load(values_file)
        pars_and_paste(list_of_tests, value)



