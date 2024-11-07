import random


def Random_Integer(min, max):                   #function name changed to make it better understandable
    #To select a random integer for question

    return random.randint(round(min), round(max)) #added a round 0ff method because random integer takes integers as arguments


def Random_Operator():                          #function name changed to make it better understandable
    #To select a random operation for question

    return random.choice(['+', '-', '*'])


def Problem_Answer_Generator(n1, n2, o):        #function name changed to make it better understandable
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2         #correct operation "+" is added 
    elif o == '-': a = n1 - n2       #correct operation of "-" is added
    else: a = n1 * n2
    return p, a

def math_quiz():
    score = 0               #variable name changed to make it better understandable
    Total_question = 3      #variable name changed to make it better understandable and rounded it to 3 as number of questions can't be a fraction.

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(Total_question):
        n1 = Random_Integer(1, 10); n2 = Random_Integer(1, 5.5); o = Random_Operator()

        PROBLEM, ANSWER = Problem_Answer_Generator(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")

        try:                                                              #Added exception handling for the wrong user inputs.                         
          useranswer = input("Your answer: ")
          useranswer = int(useranswer)
          if useranswer == ANSWER:
                print("Correct! You earned a point.")
                score += 1
          else:
                print(f"Wrong answer. The correct answer is {ANSWER}.")
        except Exception as e:
          print(e)

    print(f"\nGame over! Your score is: {score}/{Total_question}")

if __name__ == "__main__":
    math_quiz()