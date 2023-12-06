with open('inputs/1.txt') as f:
    data = f.read().splitlines()
    
    total_1 = 0
    total_2 = 0
    spelled_nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


    #   FOR PART 1
    for line in data:
        num_list_1 = []
        for char in line:
            if char.isdigit():
                num_list_1.append(char)
        line_num = int(num_list_1[0] + num_list_1[-1])
        total_1+=line_num
    
    #   FOR PART 2
    for line in data: #looping thru each line in file
        num_list_2 = [] #init empty array
        for i, char in enumerate(line): #looping through each char in the line, with indexes
            if char.isdigit(): # check if the char is a number character
                num_list_2.append(char) 
            for n, num in enumerate(spelled_nums): # loop through each spelled out number, with index to correspond with spelled out number
                if line[i:].startswith(num): # if the characer at i starts with the spelled out number, append n+1 to num list
                    num_list_2.append(str(n+1))
        line_num=int(num_list_2[0] + num_list_2[-1])
        total_2 += line_num


# runtime O(n^3)? three for loops. Could be dumb idk
print(total_1)
print(total_2)
