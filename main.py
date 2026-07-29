questions = [
    ["What is the capital of India?","Mumbai", "New Delhi", "Kolkata", "Chennai", 2],
    ["How many states does India have?","26", "27", "28", "29", 3],
    ["Who is known as the Father of the Indian Constitution?","Mahatma Gandhi", "B. R. Ambedkar", "Jawaharlal Nehru", "Sardar Patel", 2],
    ["Which is India's national animal?","Lion", "Tiger", "Elephant", "Leopard", 2],
    ["Which is the longest river in India?","Yamuna", "Godavari", "Ganga", "Krishna", 3],
    ["Which planet is called the Red Planet?","Earth", "Mars", "Venus", "Jupiter", 2],
    ["How many colors are there in the Indian flag?","3", "2", "4", "1", 1],
    ["Who wrote the Indian National Anthem?","Bankim Chandra", "Rabindranath Tagore", "Premchand", "Vivekananda", 2],
    ["Which symbol is used for comments in Python?","//", "#", "<!--", "/*", 2],
    ["Which loop repeats until a condition becomes False?","if", "while", "switch", "foreach", 2],
    ["What is the output of print(type(5))?","float", "int", "string", "bool", 2],
    ["Which keyword exits a loop?","stop", "break", "exit", "end", 2],
    ["Which number comes next? 2, 4, 8, 16, ?","20", "24", "32", "30", 3],
    ["Odd one out?","Apple", "Mango", "Carrot", "Banana", 3],
    ["Which is heavier?","1 kg Iron", "1 kg Cotton", "Both Equal", "Cannot Say", 3],
    ["Which month has 28 days?","February", "January", "All Months", "December", 3],
    ["If TODAY is Monday, what day comes after 10 days?","Wednesday", "Thursday", "Friday", "Saturday", 2],
    #["question[0]","question[1]","question[2]","question[3]","question[4]","question[5]"]
]
prizes = [100, 200, 300, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000, 2500000, 5000000, 10000000]
i = 0
for question in questions:
    print(question[0])
    print(f"A. {question[1]}")
    print(f"B. {question[2]}")
    print(f"C. {question[3]}")
    print(f"D. {question[4]}")

    #check whether the answer is correct or not
    answer = int(input("Enter your answer: 1 for A, 2 for B, 3 for C, 4 for D.\n"))
    if(question[5] ==answer):
        print("Correct answer.")
        print(f"You Won {prizes[i]} rupees.")
        i+=1
    else:
        print(f"Incorrect answer!! Correct answer was {question[question[5]]}.")
        print("Ughhh, Better luck next time!")
        break