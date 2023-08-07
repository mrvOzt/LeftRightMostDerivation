#2019510089_Hatice_Çelik
#2019510097_Merve_Öztürk


#files

FILE_LL = "ll.txt"
FILE_LR = "lr.txt"
FILE_INPUT = "input.txt"
stack = []


# function for LR(1)
def LR(input):
    input = input.strip() #remove \n
    state_stack = "1"
    alphabet = {} # use to keep state order
    operators = {} # use to keep operators (a c d $ B S )
    products = [] # use to keep LR table
    no = 1
    print("\n")
    print("Processing input string {0} for LR(1) parsing table".format(input))
    print("\n")
    lr_file = open(FILE_LR, "r", encoding='utf-8') # open the FILE_LR to read file
    for line_no, line in enumerate(lr_file):
        line = line.strip()
        line = line.replace(" ", "").split(";")

        if (line_no == 1):
            for no, symbols in enumerate(line):
                symbols = symbols.strip()
                operators[symbols] = no # keep operators -->  {'a': 1, 'c': 2, 'd': 3, '$': 4, 'S': 5, 'B': 6}
        else:
            products.append(line)    # for example state 1 line  --->  ['State_1', 'State_3', '', '', '', 'State_2', '']
            alphabet[line[0][-1]] = line_no -1        # '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7  --> order of states

    state_stack = products[1][0][-1]  # last element of stack
    no=1
    input_control = 0  # for reading stack element

    print("NO  | STATE STACK | READ |  INPUT  |  ACTION ", end="\n" )
    
    if(products[alphabet[state_stack[-1]]][operators[input[input_control]]] == ''):  # if does not have an action/step for
        print(f"{no:<4}| {state_stack:<12}|{input[input_control]:^6}|{input:>7}  | ",
        "REJECTED  ({0} does not have an action/step for {1})".format(products[alphabet[state_stack[-1]]][0],input[input_control]))
        print("\n")
        exit()
    else:  # if have an action 
        print(f"{no:<4}| {state_stack:<12}|{input[input_control]:^6}|{input:>7}  | ",
            "Shift to state {0}".format(products[1][operators[input[input_control]]]))
        state_stack += " " + products[1][operators[input[input_control]]][-1]    
    while(True):
        no+=1
        input_control +=1
        
        if "->"  in products[alphabet[state_stack[-1]]][operators[input[input_control]]] :  # if we need to reverse stack for example B -> d
            temp =products[alphabet[state_stack[-1]]][operators[input[input_control]]][0]   # temp is B
            lenght = len(products[alphabet[state_stack[-1]]][operators[input[input_control]]][3:])  # len("d") for delete states from stack

            print(f"{no:<4}| {state_stack:<12}|{input[input_control]:^6}|{input:>7}  | ",
            "Reverse {0}".format(products[alphabet[state_stack[-1]]][operators[input[input_control]]]))

            for i in range(lenght):
                state_stack  = state_stack[0:-1]  # for delete last element
                state_stack = state_stack.strip()
            str_temp = input[input_control:]
            input = input[:input_control - lenght] + temp + str_temp # for update input 
            input_control -= lenght + 1
        else:    
            if(products[alphabet[state_stack[-1]]][operators[input[input_control]]] == "Accept"):       # if state is accepted for special operator
                print(f"{no:<4}| {state_stack:<12}|{input[input_control]:^6}|{input:>7}  |  ACCEPTED")
                print("\n")
                break
            else:
                if(products[alphabet[state_stack[-1]]][operators[input[input_control]]] == ''):    # if state not have match
                    print(f"{no:<4}| {state_stack:<12}|{input[input_control]:^6}|{input:>7}  | ",
                    "REJECTED  ({0} does not have an action/step for {1})".format(products[alphabet[state_stack[-1]]],operators[input[input_control]]))
                    print("\n")
                    break
                else:
                    
                    print(f"{no:<4}| {state_stack:<12}|{input[input_control]:^6}|{input:>7}  | ",    # if have an action for operator
                    "Shift to state {0}".format(products[alphabet[state_stack[-1]]][operators[input[input_control]]]))
                    state_stack += " " + products[alphabet[state_stack[-1]]][operators[input[input_control]]][-1]
            
def LL(input):
    input = input.strip()
    operators = {}  # use to keep operators order
    alphabet = {}   # use to keep letter order
    products = []   # use to keep LL table

    print("\n")
    print("Processing input string {0} for LL(1) parsing table".format(input))
    print("\n")
    ll_file = open(FILE_LL, "r", encoding='utf-8')  # to read FILE_LL 
    for line_no, line in enumerate(ll_file):
        line = line.strip()
        line = line.replace(" ", "").split(";")
        alphabet[line[0]] = line_no    # 'E': 1, 'A': 2, 'T': 3, 'B': 4, 'F': 5

        if (line_no == 0):
            for no, symbols in enumerate(line):
                symbols = symbols.strip()
                operators[symbols] = no   # 'id': 1, '+': 2, '*': 3, '(': 4, ')': 5, '$': 6
        else:
            products.append(line)   # ['E', 'E->TA', '', '', 'E->TA', '', '']   for letter E this line is E line
   
    stack ="$"
    no=1
    
    print("NO  |  STACK  | INPUT     |  ACTION ")
    print(f"{no:<4}|  {stack:<7}|{input:>10} | ",  products[0][1])
    stack += parser(products[0][1])  # e->TA parse AT and insert stack
    while(True):
        if(alphabet.get(stack[-1])):
            no+=1
            temp = parser(products[alphabet[stack[-1]] - 1][operators[input_parser(input)]])   # for example T -> FB and temo = BF
            if(temp == ''):   # if temp is empty --> REJECTED
                print(f"{no:<4}|  {stack:<7}|{input:>10} | ",
                  "REJECTED  ({0} does not have an action/step for {1})".format(stack[-1],input_parser(input)))
                
                break
            else:   # for delete rlast element of stack and insert temp
                print(f"{no:<4}|  {stack:<7}|{input:>10} | ",
                    products[alphabet[stack[-1]] - 1][operators[input_parser(input)]])
            stack = stack[0:-1]
            stack += temp
        else:       # if stack last element is an operator 
            stack_operator = stack[-1]
            if(stack_operator == "d"):
                stack_operator = "id"
            if(stack_operator == input_parser(input)):
                no+=1
                if(stack_operator == "$"):    # we reach to final
                    print(f"{no:<4}|  {stack:<7}|{input:>10} | ",
                  "ACCEPTED",end="\n")
                    break
                else:   
                    print(f"{no:<4}|  {stack:<7}|{input:>10} | ",
                    "Match and remove " + stack_operator )    
                # we have match for example $ABid    id+id*id$    delete id and   $AB     +id*id$
                if(stack_operator == "id"):  # if stack_operator is id 
                    stack = stack[0:-2]    # delete last top element
                    input = input[2:]     # delete first two element from input
                else:  # if stack operator is + , * , ( ,)
                    stack = stack[0:-1]
                    input = input[1:]
            elif(stack_operator == "ϵ" or stack_operator == "ε"):   # if stack_operator is epsilon , only delete stack last element
                stack = stack[0:-1]
            
def input_parser(input):  # to find input operator
    
    if(input[0:2]=="id"):
        return "id"
    elif(input[0]=="+"):
        return "+"
    elif (input[0] == "*"):
        return "*"
    elif (input[0] == "("):
        return "("
    elif (input[0] == ")"):
        return ")"
    elif (input[0] == "$"):
        return "$"
        
def parser(action):   # for T -> FB  to  BF (to insert stack )
    temp = action[3:]
    if(temp!="id"):
        return temp[::-1]

    else:
        return temp

input_file = open(FILE_INPUT, "r", encoding='utf-8')
print("Read LL(1) parsing table from file " + FILE_LL)
print("Read LR(1) parsing table from file " + FILE_LR)
print("Read input strings from file " +FILE_INPUT)
for line in input_file:   # to read input file line by line 
    line = line.split(";")
    if (line[0].strip() == "LL"):
        LL(line[1])
    elif (line[0].strip() == "LR"):
        LR(line[1])
print("\n")
   
