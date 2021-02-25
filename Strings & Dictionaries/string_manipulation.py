string_1 = "abc"
string_2 = "bac"

sorted_1 = sorted(string_1)
sorted_2 = sorted(string_2)

if sorted_1 == sorted_2:
    print("String 1 is permutation")

else:
    print("Not permutation!")




def space_check(s):
    string = s.strip()
    spaceless = "%20".join(string.split())
    print(spaceless)


space_check("Mr john Smith      ")



def unique(s):
    store = {}
    is_unique = True
    for letter in s:
        if letter in store.keys():
            is_unique = False
            store[letter] += 1
        else:
            store[letter] = 1


    if is_unique == True:
        print("It is unique")

    else:
        print("Not Unique (-1)")

    for letter, value in store.items():
        if value == 1:
            print(letter, "is first unique letter")
            break

unique("bwertyuiopn")



def does_equal(list, target):
    result = []
    for num in list:
        for second_num in range(num+1, len(list)):
            if num + second_num == target:
                result.append((num, second_num))
    print(result)


test = [1, 2, 3, 4, 5, 6, 7, 8, 11, 12]
does_equal(test, 10)




def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l) 

f(2)
f(3,[3,2,1])
f(3)


#average word lengths
def average_len(s):
    for p in "!?',;:.":
        s = s.replace(p, '')
    words = s.split()
    print(round(sum(len(word) for word in words)/len(words), 2))

average_len("hello there I am a new python thing that will be finished")


#add string
num1 = '364'
num2 = '1836'

def add_str(one, two):
    first_num = int(one)
    scnd_num = int(two)
    added = first_num + scnd_num
    final_str = str(added)
    print(final_str)

add_str(num1, num2)

#add string but not turning str into int
def solution_add(num1, num2):
    ans = str(eval(num1) + eval(num2))
    print(ans)

solution_add(num1, num2)




# Given an array of integers, determine whether the array is monotonic or not.
A = [6, 5, 4, 4] 
B = [1,1,1,3,3,4,3,2,4,2]
C = [1,1,2,3,7]

def solution(nums): 
    return (all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or 
            all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1))) 
  
print(solution(A)) 
print(solution(B)) 
print(solution(C)) 