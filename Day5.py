
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

def intcode(input_list):
    debug_list = []
    i = 0
    ip_incr = 4 # instruction pointer increment
    while i <= len(input_list):
        opcode, mode1, mode2 = slice_instruction(str(input_list[i]))
        if opcode == 1: # addition
            param1 = input_list[i+1]
            param2 = input_list[i+2]
            result_addr = input_list[i+3]
            if not mode1: param1 = input_list[param1]
            if not mode2: param2 = input_list[param2]
            input_list[result_addr] = param1 + param2
            ip_incr = 4
        elif opcode == 2: # multiplication
            param1 = input_list[i+1]
            param2 = input_list[i+2]
            if not mode1: param1 = input_list[param1]
            if not mode2: param2 = input_list[param2]
            result_addr = input_list[i+3]
            input_list[result_addr] = param1 * param2
            ip_incr = 4
        elif opcode == 3: # input instruction
            input_value = 1 # given by task
            result_addr = input_list[i+1]
            input_list[result_addr] = input_value
            ip_incr = 2
        elif opcode == 4: # output instruction 
            param1 = input_list[i+1]
            if not mode1: param1 = input_list[param1]
            output = param1
            print("Value of Output: ", output, "at pos:", i)
            if output != 0:
                [print(x) for x in debug_list]
            ip_incr = 2
        elif opcode == 99: # halt program
            print("HALT at position", i)
            return input_list # for assertion
        else:
            print ("Invalid Instruction:", input_list[i], "at pos:", i)
            break
        debug_list.append(input_list[i:i+ip_incr])
        i += ip_incr

if __name__ == "__main__":
    # assert intcode([3,0,4,0,99]) == [1,0,4,0,99]
    # assert intcode([1,0,0,0,99]) == [2,0,0,0,99]
    # assert intcode([2,3,0,3,99]) == [2,3,0,6,99]
    # assert intcode([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
    # assert intcode([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]
    # assert intcode([1101,5,6,7,99,20,30,0]) == [1101,5,6,7,99,20,30,11]
    # assert intcode([1001,5,6,7,99,20,30,0]) == [1001,5,6,7,99,20,30,26]
    # assert intcode([101,5,6,7,99,20,30,0])  == [101,5,6,7,99,20,30,35]
    # assert intcode([1102,5,6,7,99,20,30,0]) == [1102,5,6,7,99,20,30,30]
    # assert intcode([1002,5,6,7,99,20,30,0]) == [1002,5,6,7,99,20,30,120]
    # assert intcode([102,5,6,7,99,20,30,0])  == [102,5,6,7,99,20,30,150]
    # assert intcode([104,1,99,20])  == [104,1,99,20]
    assert slice_instruction("1101") == (1, 1, 1)
    assert slice_instruction("1") == (1, 0, 0)
    assert slice_instruction("101") == (1, 1, 0)
    #[print(x) for x in map(str,instruction_set) if len(x) == 5]
    intcode(instruction_set)