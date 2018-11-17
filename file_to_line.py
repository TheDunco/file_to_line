'''
Created on Nov 3, 2018
@authors: Haram Koo, Duncan Van Keulen
'''


def file_to_line(file):
    '''
    This function turns a file into a string
    '''
    with open(file, 'r') as file:
        list_1 = []

        for line in file:
            list_1.append(str(line))

        string_list = ''.join(list_1)

        nl_string = string_list.replace('\n', '\\n')
        final_string = nl_string.replace('    ', '\\t')
        
    return final_string


def file_to_line_overwrite(overwrite, to_1):
    '''Dangerous, overwrites files, meant to be copied into another file'''
    # from file_to_line import *
    # with open("<file you're in/want to overwrite>", 'w') as file:
    #     file.write('''{}'''.format(str(file_to_string('<file you want to be converted to 1 line>'))))
    with open(overwrite, 'w') as file:
         file.write('''{}'''.format(str(file_to_string(to_1))))


def file_to_line_print(file_handle):
    '''Prints the file in one line'''
    # If you want to copy this code...
    # from file_to_string import *
    # print(str(file_to_line('<file to be converted to 1 line>')))
    print(str(file_to_line(str(file_handle))))


