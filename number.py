
# try:
#     x = int(input("whats x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

# while True:
#   try:
#     x = int(input("whats x? "))
#   except ValueError:
#     print("x is not an integer")
#   else:
#      break

# print(f"x is {x}")

# def main():
#     x = get_in()
#     print(f"x is {x}")


# def get_in():
#     while True:
#         try:
#             x = int(input("whats x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             break
#     return x


# main()

#pass

def main():
    x = get_in("what's x? ")
    print(f"x is {x}")

def get_in(prompt):
    while True:
        try:
          return int(input(prompt))
        except ValueError:
          pass

main()