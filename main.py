from translate import Translator
import pykakasi

red ="\033[0;31m"
x = f"""
{red}

⣠⣤⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣤⣄
⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟
⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀
⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⣸⣿⣇⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀⠀⣸⣿⣇⠀⠀⠀⠀
⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⠀⠉⢹⣿⣿⣿⡏⠉⠉⠉⠉⠉⠉⠉⠉⢹⣿⣿⣿⡏⠉⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀  ⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀  ⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀  ⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀  ⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠘⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀  ⠀⠀⠈⠛⠛⠛⠃⠀⠀⠀⠀



by - abdlurhman salah 
version - 1.0 

"""
print(x)
translator = Translator(to_lang="ja")
#user input 
text = str(input("Enter your text : "))

translation = translator.translate(text)

print("Original Text:", text)
print("Translated Text:", translation)


def save() : 
    
    with open("jp-file.txt", "a", encoding="utf-8") as file:

        file.write(f"{text}, {translation}\n")
        
    

       


ask = (input ("Do u wont save the word in your vocab file ?  (y/n): "))
ask2 = input("do u wont save more ? : ")

if ask == "y" :
    save()
    pass
if ask =="n" :
    print ("okay ...")
    exit  
    
if ask2 == "y" :

    while True : 
        print("★゜・。。・゜゜・。。・゜☆゜・。。・゜゜・。。・゜★")
        translator = Translator(to_lang="ja")
        #user input 
        text = str(input("Enter your text : "))

        translation = translator.translate(text)

        print("Original Text:", text)
        print("Translated Text:", translation)
        save()