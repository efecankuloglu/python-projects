def plain(p_text):
    return p_text

def bold(text):
    return f"**{text}**"

def italic(text):
    return f"*{text}*"

def link(label, link):
    return f"[{label}]({link})"

def header(level, text):
    return f"{'#' * level}" + " " + text + "\n"

def new_line():
    return "\n"

def inline_code(link):
    return f"`{link}`"

def lists(rows, type):
    if type == "ordered-list":
        o_list = ""
        for i in range(1, rows + 1):
            element = input(f"- Row #{i}: ")
            ol = f"{i}. {element}\n"
            o_list += ol
        return o_list
    elif type == "unordered-list":
        u_list = ""
        for i in range(1, rows + 1):
            element = input(f"- Row #{i}: ")
            ul = f"* {element}\n"
            u_list += ul
        return u_list

text =[]

lt = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list", "new-line"]

while True:
    formatter = input("- Choose a formatter: ")
    if formatter in lt:
        if formatter == "plain":
            txt = input("- Text: ")
            text.append(plain(txt))
        elif formatter == "bold":
            txt = input("- Text: ")
            text.append(bold(txt))
        elif formatter == "italic":
            txt = input("- Text: ")
            text.append(italic(txt))
        elif formatter == "header":
            lvl = int(input("- Level: "))
            if lvl < 0 or lvl > 6:
                print("The level should be within the range of 1 to 6")
            else:
                txt = input("- Text: ")
                text.append(header(lvl, txt))
        elif formatter == "link":
            lbl = input("- Label: ")
            url = input("- URL: ")
            text.append(link(lbl, url))
        elif formatter == "new-line":
            text.append(new_line())
        elif formatter == "inline-code":
            txt = input("- Text: ")
            text.append(inline_code(txt))
        elif formatter == "ordered-list":
            while True:
                rows = int(input("- Number of rows:"))
                if rows <= 0:
                    print("The number of rows should be greater than zero")
                else:
                    text.append(lists(rows, formatter))
                    break
        elif formatter == "unordered-list":
            while True:
                rows = int(input("- Number of rows:"))
                if rows <= 0:
                    print("The number of rows should be greater than zero")
                else:
                    text.append(lists(rows, formatter))
                    break
        print("".join(text))
    elif formatter == "!help":
        print(f"Available formatters: {' '.join(lt)}")
        print("Special commands: !help !done")
    elif formatter == "!done":
        with open("output.md", "w") as f:
            f.write("".join(text))
        break
    else:
        print("Unknown formatter or command. Please try again.")