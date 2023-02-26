"""
Password Generator/Validator
Name: Anirudh Pottammal
From: Dayton, New Jersey
"""

import re
import secrets
import string
import requests
import random



def main():
    print("\nWelcome to the Universal Password Generator/Validator!")
    print("All passwords generated will: ")
    print("\t• be between 10 - 12 characters")
    print("\t• contain at least 1 capitalized letter")
    print("\t• contain at least 1 special character")
    print("\t• contain at least 1 numerical digit")
    print("Any password registered for validation will be given a score out of 10 to describe its strength, along with some feedback if suitable.")
    print("Respond with 'q' at any time to exit.\n")
    while True:
        choice = input("Generate, or validate a password? ").strip().lower()
        match choice:
            case 'generate' | 'generate password' | 'generate a password' | 'i would like to generate a password' | 'i would like to generate' | 'i want to generate a password':
                generate_pass()
                if ask_to_continue() == False:
                    break
            case 'validate' | 'validate password' | 'validate a password' | 'i would like to validate a password' | 'i would like to validate' | 'i want to validate a password':
                validate_pass()
                if ask_to_continue() == False:
                    break
            case 'q':
                break
            case _:
                print("Invalid input. Respond with either generate or validate!")


    print("\nThank you for using the Universal Password Generator/Validator. Goodbye!\n")




def ask_to_continue():
    choice = input("Would you like to continue? (Y/N) ").lower().strip()
    match choice:
        case 'y' | 'yes' | 'yeah':
            return True
        case 'n' | 'no' | 'nah':
            return False
        case 'q':
            return False
        case _:
            print("Invalid input")




def generate_pass():
    new_pass_list = []
    new_pass = ""
    letters = string.ascii_letters
    digits = string.digits
    special_chars = '!#$%&?@'
    while True:
        complexity = input("Would you like a simple or complex password? ").strip().lower()
        match complexity:
            case 'simple' | 'easy':
                pass_length = 10
                response = requests.get("https://www.mit.edu/~ecprice/wordlist.10000")
                words = response.content.splitlines()
                while True:
                    word = random.choice(words)
                    if len(word) != 6:
                        pass
                    else:
                        word = word.decode().capitalize()
                        new_pass_list.append(word)
                        for i in range(3):
                            new_pass_list.append(secrets.choice(digits))
                        new_pass_list.append(secrets.choice(special_chars))
                        break


                random.shuffle(new_pass_list)
                for i in range(len(new_pass_list)):
                    new_pass += new_pass_list[i]
                print(f"\nYour Randomly Generated Password: {new_pass}\n")
                break


            case 'complex' | 'complicated':
                letters_nums = letters + digits
                pass_length = 12
                for i in range(pass_length-1):
                    new_pass_list.append(secrets.choice(letters_nums))
                new_pass_list.append(secrets.choice(special_chars))
                random.shuffle(new_pass_list)
                for i in range(12):
                    new_pass += new_pass_list[i]
                print(f"\nYour Randomly Generated Password: {new_pass}\n")
                break


            case _:
                print("Invalid input. Respond with either simple or complex!")




def validate_pass():
    password = input("Password for Validation: ")
    if re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#!%*?&\.])[A-Za-z\d@$!%#*?&\.]{10,12}$", password):
        print("\nValid! Very strong password")
        score, feedback = score_pass(password)
        print(f"Score: {str(score)}/10 \nFeedback: {feedback}\n")


    else:
        score, feedback = score_pass(password)
        password_strength = ""
        if score == 0:
            password_strength = "Terrible password."
        elif score == 2:
            password_strength = "Password is not very strong."
        elif score == 4:
            password_strength = "Weak password."
        elif score == 6:
            password_strength = "Password is okay."
        elif score == 8:
            password_strength = "Good password."
        print(f"\nInvalid. {password_strength}")
        print(f"Score: {str(score)}/10 \nFeedback: {feedback}\n")




def score_pass(pwd):
    score = 0
    feedback = ""
    if re.search(r"(?=.*[a-z])", pwd):
        score += 2
    else:
        feedback += "\n\t• Missing at least 1 lower case letter "
    if re.search(r"(?=.*[A-Z])", pwd):
        score += 2
    else:
        feedback += "\n\t• Missing at least 1 upper case letter "
    if re.search(r"(?=.*\d)", pwd):
        score += 2
    else:
        feedback += "\n\t• Missing at least 1 numerical digit "
    if re.search(r"(?=.*\W)", pwd):
        score += 2
    else:
        feedback += "\n\t• Missing at least 1 special character "
    if len(pwd) >= 8 and len(pwd) <= 12:
        score += 2
    else:
        feedback += "\n\t• Not enough characters in length "
    if feedback == "":
        feedback = "None!"
    return score, feedback




if __name__ == "__main__":
    main()