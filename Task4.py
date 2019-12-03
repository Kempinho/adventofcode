#!/usr/bin/env python3
input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,19,5,23,2,23,13,27,1,10,27,
        31,2,31,6,35,1,5,35,39,1,39,10,43,2,9,43,47,1,47,5,51,2,51,9,55,1,13,55,59,
        1,13,59,63,1,6,63,67,2,13,67,71,1,10,71,75,2,13,75,79,1,5,79,83,2,83,9,87,
        2,87,13,91,1,91,5,95,2,9,95,99,1,99,5,103,1,2,103,107,1,10,107,0,99,2,14,0,0
        ]

def intcode(input_list, noun, verb):
    input_list[1] = noun
    input_list[2] = verb
    output_list = input_list
    i = 0
    while i <= len(input_list):
        if input_list[i] == 1: # addition
            pos_a = input_list[i+1]
            pos_b = input_list[i+2]
            result_pos = input_list[i+3]
            output_list[result_pos] = input_list[pos_a] + input_list[pos_b]
        elif input_list[i] == 2: # multiplication
            pos_a = input_list[i+1]
            pos_b = input_list[i+2]
            result_pos = input_list[i+3]
            output_list[result_pos] = input_list[pos_a] * input_list[pos_b]
        elif input_list[i] == 99: # halt program
            #print("HALT at position", i)
            if output_list[0] == 19690720:
                print("Hit with {0} and {1}, result is {2}".format(
                    noun, verb, 100*noun+verb))
            break
        else:
            print ("wrong Instruction:", input_list[i],
                "at position:", i)
        i += 4


if __name__ == "__main__":
    for noun in range(10):
        for verb in range(1):
            intcode(input[:], noun, verb)