# def is_prime(x):
#     for i in range(2,int(x**0.5)+1 ):
#         if x%i==0:
#             return False
#     return True


# n=int(input("Enter size of list:"))
# li=[]
# for i in range(0,n):
#     x=int(input("Enter a value"))
#     while not is_prime(x):
#         x=int(input("Not a prime number,Enter a value: "))
#         li.append(x)

# print(li)


#Program 1

# def count_freq(paragraph):
#     dic={}
#     for row in paragraph:
#         for word in row:
#             lower_word= word.lower()
#             if lower_word =="stop":
#                 break
#             if len(lower_word)<3:
#                 continue
#             if lower_word in dic:
#                 dic[lower_word]+=1
#             else:
#                 dic[lower_word]=1
#         else:
#             continue
#         break
#     return dic

    
                
            
# paragraph = [
#     ["Hello", "world", "hello"],
#     ["this", "is", "a", "test"],
#     ["STOP", "ignore", "this", "line"],
#     ["should", "not", "be", "processed"]
# ]
# res=count_freq(paragraph)
# print(res)


#program 2
# def check_winner(board):
#     for row in board:
#         if row==["","",""]:
#             continue
#         if row[0]==row[1]==row[2]!="": 
#             return row[0]
#     for col in range(3):
#         if board[0][col]==board[1][col]==board[2][col]!="":
#             return board[0][col]
#     if board[0][0]==board[1][1]==board[2][2]!="":
#         return board[0][0]
#     if board[0][2]==board[1][1]==board[2][0]!="":
#         return board[0][2]
#     return "Draw"

        
# board = [
#     ["X", "O", "X"],
#     ["O", "X", ""],
#     ["O", "", "X"]
# ]

# res=check_winner(board)
# print(res)






      























