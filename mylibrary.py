# this file contains simple/dummy functions to test a 
# pipeline in tekton with flake8 and unit test tasks

def sumValues(in_=[1,2,3]):
    '''this function returns the sum of all the array entries'''

    out_ = 0
    for i_ in in_:
        if str(i_).isdigit() is True:
            out_ += i_
    return out_
