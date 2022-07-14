import tkinter as tk
import string
win = tk.Tk()

win.geometry('800x800+100+100')

print('Caesar Chypher')


win.title('Caesar Chypher')
text = tk.Entry(win)

offset = tk.Entry(win)


outputText = ''

def encrypt(offset,text):
    global outputText
    offset = int(offset)
    for letter in text:
        if ord(letter) == 32 or ord(letter) == 9:
            encodedWord = ord(letter)
        
        elif letter in string.punctuation:
            encodedWord = ord(letter)
            
        elif letter.islower():
            encodedWord = ord(letter)+offset
            if encodedWord >122:
                encodedWord = (encodedWord - 122) +96
        else:
            encodedWord = ord(letter)+offset
            if encodedWord > 96:
                encodedWord = (encodedWord - 96) +64
        outputText = outputText + chr(encodedWord)    
    OutputTextLabel = tk.Label(win,text = outputText).grid(row = 4,column=0) 
    print(outputText)
    outputText = ''
    
    
    
def decrypt(text,offset):
    global outputText
    offset = int(offset)
    for letter in text:
        if ord(letter) == 32 or ord(letter) == 9:
            encodedWord = ord(letter)
        
        elif letter in string.punctuation:
            encodedWord = ord(letter)
            
        elif letter.islower():
            encodedWord = ord(letter)-offset
            if encodedWord >122:
                encodedWord = (encodedWord - 122) +96
        else:
            encodedWord = ord(letter)-offset
            if encodedWord > 96:
                encodedWord = (encodedWord - 96) +64
        outputText = outputText + chr(encodedWord) 
    outptTextLabel = tk.Label(win,text = outputText).grid(row =4,column =0)
    print(outputText) 
    outputText = ''              
        
def TakeTextToEncrypt():
    Textvalue = text.get()
    offsetValue = offset.get()
    encrypt(text=Textvalue,offset = offsetValue)
def TakeTextToDecrypt():
    TextValue = text.get()
    offsetValue = offset.get()
    decrypt(text = TextValue,offset = offsetValue)
    

    
def EnableDecryptOptions():
    text.grid(row=1,column =1)
    offset.grid(row=2,column =1)
    Ent = tk.Label(win,text = 'Enter text').grid(row = 1,column = 0)
    Off = tk.Label(win,text = 'Enter offset').grid(row = 2,column=0)
    StartDecrypt = tk.Button(win,text = 'Decrypt', command = TakeTextToDecrypt).grid(row = 3,column = 0)
    #EncryptButton.destroy()
    
def EnableEncryptOptions():
    text.grid(row = 1,column = 1)
    offset.grid(row = 2,column = 1)
    
    Ent = tk.Label(win,text = 'Enter text').grid(row = 1,column = 0)
    Off = tk.Label(win,text = 'Enter offset').grid(row = 2,column =0)
    StartEncrypt = tk.Button(win,text = 'Encrypt',command = TakeTextToEncrypt).grid(row = 3,column =0)
    #DecryptButton.destroy()
EncryptButton = tk.Button(win,text='Encrypt',command = EnableEncryptOptions).grid(row = 0, column=0)
DecryptButton = tk.Button(win,text='Decrypt',command = EnableDecryptOptions).grid(row = 0,column=1)
win.mainloop()

    