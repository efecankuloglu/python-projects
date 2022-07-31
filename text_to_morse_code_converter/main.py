alphabet_dict = {
"a": ".−",
"b": "−...",
"c": "−.−.",
"d": "−..",
"e": ".",
"f": "..−.",
"g": "−−.",
"h": "....", 
"i": "..",
"j": ".−−−", 
"k": "−.−", 
"l": ".−..",
"m": "−−", 
"n": "−.", 
"o": "−−−", 
"p": ".−−.", 
"q": "−−.−", 
"r": ".−.",
"s": "...",
"t": "−",
"u": "..−",
"v": "...−",
"w": ".−−",
"x": "−..−",
"y": "−.−−",
"z": "−−..",
"1": ".−−−−", 
"2": "..−−−",
"3": "...−−",
"4": "....−",
"5": ".....", 
"6": "−....",
"7": "−−...",
"8": "−−−..",
"9": "−−−−.",
"0": "−−−−−",
}


def text_to_morse(text):
    morse_text = []
    for i in text.lower():
        if i == " ":
            morse_text.append("/")
        elif i not in alphabet_dict.keys():
            continue
        else:
            morse_text.append(alphabet_dict[i])
    return " ".join(morse_text)


input_text = input("Please write the text you want to convert to Morse: ")
print(text_to_morse(input_text))
