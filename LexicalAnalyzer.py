import tkinter as tk
from tkinter import filedialog, messagebox, font
from Dictionaries import OPERATORS, SPECIAL_SYMBOLS,RESERVEDORKEY_WORDS, NOISE_WORDS
from Evaluation import contains_alphabet, contains_num, lexeme


def analyze_file(file_path):
    try:
        tempstring = ''
        lexemes = []
        SynTokens = []
        line_number = 1  # Initialize line number
        
        # Read the chosen file
        with open(file_path, 'r') as content:
            # Create Symbol Table
            with open("SymbolTable.txt", 'w') as output:
                output.write("__________________________________________________________________________\n")
                output.write("| {:<30} | {:<20} | {:<15} |\n".format("Lexemes", "Tokens", "Line Number"))
                output.write("|_________________________________________________________________________|\n")
                
                # Scan the file by line
                for line in content:
                    # Scan the line by character
                    for char in line:
                        # Check if the character is alphabet
                        if char == ' ':
                            # Check for comments and strings
                            if '//' in tempstring or '/*' in tempstring or '"' in tempstring or "'" in tempstring:
                                tempstring += char
                            elif tempstring in RESERVEDORKEY_WORDS or NOISE_WORDS:
                                lexemes.append((tempstring, line_number))  # Append lexeme with line number
                                tempstring = ''
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
                            # Handle various cases of operators
                            if tempstring == '':
                                tempstring += char
                            elif tempstring == '-' and char == '-':
                                tempstring += char
                            elif tempstring == '-' and char == '=':
                                tempstring += char
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                            # Add more conditions for other operators...
                            else:
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                                tempstring += char
                        # Checks if the character is a digit
                        elif char.isdigit():
                            # Handle digit cases
                            if tempstring == '' or tempstring.isdigit() or tempstring.isalpha():
                                tempstring += char
                            elif '.' in tempstring and contains_num(tempstring):
                                tempstring += char
                            elif tempstring.isalnum():
                                tempstring += char
                            # Handle negation vs. minus operator
                            elif tempstring == '-':
                                tempstring += 'n'
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                                tempstring += char
                            else:
                                lexemes.append((tempstring, line_number))
                                tempstring = ''
                                tempstring += char

                    # Increment line number after processing each line
                    line_number += 1

                    # Checks if the tempstring is a multi-line comment
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

                # Empties the remaining string and appends it to the lexeme list
                if tempstring.strip() != '':
                    lexemes.append((tempstring.strip(), line_number))

                # Analyze every lexeme in the lexemes list
                for token, line_num in lexemes:
                    if token.strip():  # Check if token is not empty
                        tokens = token.strip()
                        result = lexeme(tokens)

                        output.write("| {:<30} | {:<20} | {:<15} |\n".format(tokens, result, line_num))
                        SynTokens.append((result,line_num))

                output.write('|_________________________________________________________________________|\n')

                    
                for SynToken, SynLine in SynTokens:
                    output.write(str(SynToken) + '\n')  # Write each item to the output file


    except FileNotFoundError:
        print("File not found!!")


def show_symbol_table():
    try:
        with open("SymbolTable.txt", 'r') as symbol_file:
            symbol_table_content = symbol_file.read()

        symbol_table_window = tk.Toplevel(root)
        symbol_table_window.title("Symbol Table")
        symbol_table_window.geometry("800x400")
        symbol_table_window.iconbitmap("icon.ico")
        symbol_table_window.configure(bg="#F4C2C2")

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
        messagebox.showinfo("Analysis Complete", "Lexical analysis completed successfully!")

    else:
        messagebox.showwarning("Invalid File", "Please select a valid Dash file.")


# Set Tkinter as GUI
root = tk.Tk()
root.title("Pegasus Lexical Analyzer")
root.geometry("600x300")
#root.iconbitmap("icon.ico")


# Set font and background color
title_style = tk.font.Font(family="Ariel", size=25)
subtitle_style = tk.font.Font(family="Ariel", size=14)
root.configure(bg="#FFFFFF")  

# Set Label
title_label = tk.Label(root, text="PEGASUS", font=title_style, bg="#FFFFFF")
subtitle_label = tk.Label(root, text="Lexical Analyzer", font=subtitle_style, bg="#FFFFFF")
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