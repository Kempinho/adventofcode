
with open("Day5_input.txt", "r") as f:
    instruction_set = list(map(int, f.readline().rstrip("\n").split(",")))
    #print(instruction_set)

def slice_instruction(instruction):
    mode1 = 0
    mode2 = 0
    opcode = 0
    opcode = int(instruction[-2:])
    if len(instruction) >= 3: mode1 = int(instruction[-3])
    if len(instruction) == 4: mode2 = int(instruction[-4])

    return opcode, mode1, mode2

def intcode(input_list, input = 1):
    i = 0
    while i <= len(input_list):
        opcode, mode1, mode2 = slice_instruction(str(input_list[i]))
        if opcode == 1: # addition
            param1 = input_list[i+1]
            param2 = input_list[i+2]
            result_addr = input_list[i+3]
            if not mode1: param1 = input_list[param1]
            if not mode2: param2 = input_list[param2]
            input_list[result_addr] = param1 + param2
            i += 4
        elif opcode == 2: # multiplication
            param1 = input_list[i+1]
            param2 = input_list[i+2]
            if not mode1: param1 = input_list[param1]
            if not mode2: param2 = input_list[param2]
            result_addr = input_list[i+3]
            input_list[result_addr] = param1 * param2
            i += 4
        elif opcode == 3: # input instruction
            input_value = input # given by task
            result_addr = input_list[i+1]
            input_list[result_addr] = input_value
            i += 2
        elif opcode == 4: # output instruction 
            param1 = input_list[i+1]
            if not mode1: param1 = input_list[param1]
            output = param1
            print("Value of Output: ", output, "at pos:", i)
            i += 2
        elif opcode == 5: # Jump-if-true
            param1 = input_list[i+1]
            param2 = input_list[i+2]
            if not mode1: param1 = input_list[param1]
            if not mode2: param2 = input_list[param2]
            if param1 != 0: i = param2
            else: i += 3
        elif opcode == 6: # Jump-if-false
            param1 = input_list[i+1]
            param2 = input_list[i+2]
            if not mode1: param1 = input_list[param1]
            if not mode2: param2 = input_list[param2]
            if param1 == 0: i = param2
            else: i += 3
        elif opcode == 7: # less than
            param1 = input_list[i+1]
            param2 = input_list[i+2]
            if not mode1: param1 = input_list[param1]
            if not mode2: param2 = input_list[param2]
            result_addr = input_list[i+3]
            if param1 < param2: input_list[result_addr] = 1
            else: input_list[result_addr] = 0
            i += 4
        elif opcode == 8: # equals
            param1 = input_list[i+1]
            param2 = input_list[i+2]
            if not mode1: param1 = input_list[param1]
            if not mode2: param2 = input_list[param2]
            result_addr = input_list[i+3]
            if param1 == param2: input_list[result_addr] = 1
            else: input_list[result_addr] = 0
            i += 4
        elif opcode == 99: # halt program
            print("HALT at position", i)
            return input_list # for assertion
        else:
            print ("Invalid Instruction:", input_list[i], "at pos:", i)
            break
        

if __name__ == "__main__":
    # PART1:
    assert intcode([3,0,4,0,99]) == [1,0,4,0,99]
    assert intcode([1,0,0,0,99]) == [2,0,0,0,99]
    assert intcode([2,3,0,3,99]) == [2,3,0,6,99]
    assert intcode([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
    assert intcode([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]
    assert intcode([1101,5,6,7,99,20,30,0]) == [1101,5,6,7,99,20,30,11]
    assert intcode([1001,5,6,7,99,20,30,0]) == [1001,5,6,7,99,20,30,26]
    assert intcode([101,5,6,7,99,20,30,0])  == [101,5,6,7,99,20,30,35]
    assert intcode([1102,5,6,7,99,20,30,0]) == [1102,5,6,7,99,20,30,30]
    assert intcode([1002,5,6,7,99,20,30,0]) == [1002,5,6,7,99,20,30,120]
    assert intcode([102,5,6,7,99,20,30,0])  == [102,5,6,7,99,20,30,150]
    assert intcode([104,1,99,20])  == [104,1,99,20]
    assert slice_instruction("1101") == (1, 1, 1)
    assert slice_instruction("1") == (1, 0, 0)
    assert slice_instruction("101") == (1, 1, 0)
    # PART2:
    intcode([3,9,8,9,10,9,4,9,99,-1,8],8) # outputs 1
    intcode([3,9,8,9,10,9,4,9,99,-1,8],7) # outputs 0
    for input in range(7,10):
        intcode([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
                1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
                999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
                ], input) # 999, 1000, 1001
    print ("------------------------------")
    intcode(instruction_set[:], input=1)
    intcode(instruction_set[:], input=5)