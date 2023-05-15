#collect email from user
#slice /split email using the @, the first parst as the username and the second part as domain
#split domain using .


def main():
  print(" Welcome to the email slicer ")
  print("")

  email_input = input("Input your email address: ")

  (username, domain) = email_input.split("@")
  (domain, extension) = domain.split(".")

  print("Username : ", username)
  print("Domain :", domain)
  print("Extension :", extension
       
while True:
  main()
