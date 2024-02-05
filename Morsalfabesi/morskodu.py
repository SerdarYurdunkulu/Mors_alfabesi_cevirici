import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout

alfabe = ["a","b","c","d","e","f","g","h","ı","j","k","l","m","n","o","p","q","r",
          "s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]
mors = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.",
        "--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..",".----","..---","...--","....-",".....",
        "-....","--...","---..","----.","-----"]
mesaj = "i"

def morscevirivi(mesaj):
        for i in mesaj :
            if i in alfabe:
                harf= alfabe.index(i)
                morskarsiligi = mors[harf]
                print(f"{i.upper()} = {morskarsiligi}")
            else:
                i=i
morscevirivi(mesaj)
