import math


def quections():
    
    number_of_answers = 0
    user_answers = []
    result_val = 0
    
    for key in quection_set:
        print(key)
        for i in answers[number_of_answers]:
            print(i)
        answer = input("Enter Your Answer : ")
        answer = answer.upper()
        user_answers.append(answer)
        result_val += checking_qct(quection_set.get(key),answer)
        number_of_answers = number_of_answers+1
    
    print("All the answer that you called")
    print(result_val)
    result(result_val,number_of_answers)
   
    

def checking_qct(exact_answer,entered_answer):
    
    if(exact_answer == entered_answer):
        return 1
    else:
        return 0
        


def result(result_that_user_got,anserws):
    
    my_result = ((result_that_user_got/anserws)*100)
    
    print("My Grade is "+str(my_result)+"%")
    

quection_set = {
    
    "1. What is the meaning of DOM ? ":"A",
    "2. What ithe interpriter of Programming language ? ":"B",
    "3. What is the most popular programming language in 2023 ?":"C"
}


answers = [
    ["A . JavaScript","B . Python","C . Java"],
    ["A . High Level","B . Low Level","C . Mide Level"],
    ["A . C++","B . Dango","C . Python"]
]


quections()



