import tkinter as tk
from tkinter import filedialog, messagebox, font
from Dictionaries import OPERATORS, SPECIAL_SYMBOLS,RESERVE_WORDS, NOISE_WORDS
from Evaluation import contains_alphabet, contains_num, lexeme
from Grammar import *


def analyze_file(file_path):
    try:
        tempstring = ''
        lexemes = []
        SynTokens = []
        line_number = 0  # Initialize line number
        
        # Read the chosen file
        with open(file_path, 'r') as content:
            # Create Symbol Table
            with open("SymbolTable.txt", 'w') as output:
                output.write("__________________________________________________________________________\n")
                output.write("| {:<30} | {:<20} | {:<15} |\n".format("Lexemes", "Tokens", "Line Number"))
                output.write("|_________________________________________________________________________|\n")
                
                # Scan the file by line
                for line in content:
                    line_number +=1
                    # Scan the line by character
                    for char in line:
                        # Check if the character is alphabet
                        if char == ' ':
                            if '//' in tempstring or '/*' in tempstring:
                                tempstring += char 
                            elif '"' in tempstring:
                                tempstring += char
                            elif "'" in tempstring:
                                tempstring += char
                            elif tempstring == '':
                                continue
                        elif char.isalpha():
                            if tempstring == '' or tempstring.isalpha() or '"' in tempstring or "'" in tempstring:
                                tempstring += char
                            elif tempstring == '\\' and (char == 'n' or char == 't'):
                                tempstring += char
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                            elif tempstring.startswith('//'):
                                tempstring += char
                            elif tempstring.startswith('/*'):
                                tempstring += char
                            else:
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                                tempstring += char
                        # Check if the character is part of the special symbols
                        elif char in SPECIAL_SYMBOLS:
                            if tempstring == '':
                                tempstring += char
                            elif tempstring.isdigit() and char == '.':
                                tempstring += char
                            elif tempstring == '*' and char == '/':
                                tempstring += char
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                            elif '"' in tempstring and contains_alphabet(tempstring) and char == '"':
                                tempstring += char
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                            elif "'" in tempstring and contains_alphabet(tempstring) and char == "'":
                                tempstring += char
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                            else:
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                                tempstring += char
                        # Checks if the character is part of the operators
                        elif char in OPERATORS:
                            if (lexemes and ('"' in lexemes[-1] or "'" in lexemes[-1])) and char == '+':
                                tempstring = char + 'c'
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                            elif tempstring == '':
                                tempstring += char
                            elif tempstring == '-' and char == '-':
                                tempstring += char
                            elif tempstring == '-' and char == '=':
                                tempstring += char
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                            elif tempstring == '--' and char == '-':
                                tempstring += char
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                            elif tempstring == '/' and char == '/':
                                tempstring += char
                            elif tempstring == '/' and char == '*':
                                tempstring += char
                            elif '/*' in tempstring and (char == '*' or char == '/'):
                                tempstring += char
                            elif tempstring.endswith('*/'):
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                                tempstring += char
                            elif tempstring.startswith('//') or tempstring.startswith('/*'):
                                tempstring+= char
                            elif tempstring == '>' and char == '>':
                                tempstring += char
                            elif tempstring == '>' and char == '=':
                                tempstring += char
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                            elif tempstring == '>>' and char == '>':
                                tempstring += char
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                            elif tempstring == '+' and (char == '+' or char == '='):
                                tempstring += char
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                            elif tempstring == '<' and char == '=':
                                tempstring += char
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                            elif tempstring == '#' and char == '>':
                                tempstring += char
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                            elif tempstring == '!' and char == '=':
                                tempstring += char
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                            elif tempstring == '~' and char == '=':
                                tempstring += char
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                            elif tempstring == '%' and char == '=':
                                tempstring += char
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                            elif tempstring == '/' and char == '=':
                                tempstring += char
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                            elif tempstring == '=' and char == '=':
                                tempstring += char
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                            elif tempstring == '|' and char == '|':
                                tempstring += char
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                            elif tempstring == '&' and char == '&':
                                tempstring += char
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                            elif tempstring == '*' and (char == '*' or char == '='):
                                tempstring += char
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                            else:
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                                tempstring += char
                        # Checks if the character is a digit
                        elif char.isdigit():
                            if tempstring == '' or tempstring.isdigit() or tempstring.isalpha():
                                tempstring += char
                            elif '.' in tempstring and contains_num(tempstring):
                                tempstring += char
                            elif tempstring.isalnum():
                                tempstring += char
                            # Checks if the '-' is a negation or minus operator
                            elif tempstring == '-':
                                tempstring += 'n'
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                                tempstring += char
                            else:
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                                tempstring += char

                    # Checks if the tempstring is a multi line comment
                    if tempstring.endswith('*/'):
                        lexemes.append((tempstring, line_number))
                        tempstring = ''
                    elif tempstring.startswith('/*'):
                        continue
                    elif tempstring == ' ':
                        tempstring = ''
                    elif tempstring != '':
                        lexemes.append((tempstring, line_number))
                        tempstring = ''
                
                # Empties the remaining string and append it to the lexeme list
                if tempstring != '':
                        lexemes.append((tempstring, line_number))
                        tempstring = ''

                # Analyze every lexeme in the lexemes list
                for token, line_num in lexemes:
                    if token.strip():  # Check if token is not empty
                        tokens = token.strip()
                        result = lexeme(tokens)

                        output.write("| {:<30} | {:<20} | {:<15} |\n".format(tokens, result, line_num))
                        SynTokens.append((result,line_num))

                output.write('|_________________________________________________________________________|\n')

                parser = Parser()
                parser.parseSymbolTable(SynTokens)




    except FileNotFoundError:
        print("File not found!!")

def show_symbol_table():
    try:
        with open("SymbolTable.txt", 'r') as symbol_file:
            symbol_table_content = symbol_file.read()

        symbol_table_window = tk.Toplevel(root)
        symbol_table_window.title("Symbol Table")
        symbol_table_window.geometry("800x400")
        symbol_table_window.configure(bg="#FFFFFF")

        scrollbar = tk.Scrollbar(symbol_table_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        symbol_table_text = tk.Text(symbol_table_window, font=("Courier New", 12), wrap=tk.WORD, yscrollcommand=scrollbar.set)
        symbol_table_text.insert(tk.END, symbol_table_content)
        symbol_table_text.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)

        scrollbar.config(command=symbol_table_text.yview)


    except FileNotFoundError:
        messagebox.showwarning("Symbol Table Not Found", "Symbol table not found. Please analyze a file first.")


def browse_file():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Pegasus", "*.pgs")])
    if file_path:
        analyze_file(file_path)

    else:
        messagebox.showwarning("Invalid File", "Please select a valid Pegasus file.")


# Set Tkinter as GUI
root = tk.Tk()
root.title("Pegasus Lexical and Syntax Analyzer")
root.geometry("600x300")
#root.iconbitmap("icon.ico")


# Set font and background color
title_style = tk.font.Font(family="Cooper Black", size=30)
subtitle_style = tk.font.Font(family="Ariel", size=14)
root.configure(bg="#FFFFFF")  

# Set Label
title_label = tk.Label(root, text="PEGASUS", font=title_style, bg="#FFFFFF")
subtitle_label = tk.Label(root, text="Lexical and Syntax Analyzer", font=subtitle_style, bg="#FFFFFF")
title_label.pack(pady=10, expand=True, fill="both")
subtitle_label.pack(pady=8, expand=True, fill="both")

browse_button = tk.Button(
    root, text="Analyze File", 
    font = subtitle_style, 
    relief = tk.RAISED, 
    width = 10,
    height = 1,
    borderwidth = 3,
    command = browse_file)
browse_button.pack(pady=10)

show_table_button = tk.Button(
    root, text="Symbol Table", 
    font=subtitle_style, 
    relief=tk.RAISED, 
    width=15,
    height=1,
    borderwidth=3,
    command=show_symbol_table)
show_table_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()