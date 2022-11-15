HEADER = 'header'
PLAIN = 'plain'
BOLD = 'bold'
ITALIC = 'italic'
LINK = 'link'
INLINE_CODE = 'inline-code'
NEW_LINE = 'new-line'
LIST = ['ordered-list', 'unordered-list']

formatted_text = ''

formatters = 'Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line\
\nSpecial commands: !help !done'
formatters_list = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line',
                   'ordered-list', 'unordered-list']


def header():
    while True:
        level = int(input('Level: '))
        if level > 6 or level < 1:
            print('The level should be within the range of 1 to 6')
            continue
        else:
            text = input('Text: ')
            return '#' * level + ' ' + text + '\n'


def plain_bold_italic_inline(formatt):
    text = input('Text: ')
    if formatt == ITALIC:
        return f'*{text}*'
    elif formatt == BOLD:
        return f'**{text}**'
    elif formatt == PLAIN:
        return text
    elif formatt == INLINE_CODE:
        return f'`{text}`'


def link():
    label = input('Label: ')
    url = input('URL: ')
    return f'[{label}]({url})'


def create_list(list_type):
    while True:
        num_of_rows = int(input("Number of rows: "))
        if num_of_rows < 1:
            print("The number of rows should be greater than zero")
            continue
        else:
            list_text = ''
            for r in range(num_of_rows):
                row_input = input(f'Row #{r + 1}: ')
                list_text += f'{r + 1}. {row_input}\n' if list_type == LIST[0] else f'* {row_input}\n'
            return list_text


def choose_formatter(ui):
    global formatted_text
    if ui == HEADER:
        if formatted_text != '':
            formatted_text += '\n' + header()
        else:
            formatted_text += header()
    elif ui in [PLAIN, BOLD, ITALIC, INLINE_CODE]:
        formatted_text += plain_bold_italic_inline(ui)
    elif ui == NEW_LINE:
        formatted_text += '\n'
    elif ui == LINK:
        formatted_text += link()
    elif ui in LIST:
        formatted_text += create_list(ui)
    return formatted_text


def save_to_the_file():
    global formatted_text
    file = open('README.md', 'w')
    file.write(formatted_text)
    file.close()


def main():
    while True:
        user_input = input('Choose a formatter (write !help for help): ')
        if user_input == '!done':
            save_to_the_file()
            break
        elif user_input == '!help':
            print(formatters)
        elif user_input not in formatters_list:
            print('Unknown formatting type or command')
            continue
        else:
            result_text = choose_formatter(user_input)
            print(result_text)


if __name__ == '__main__':
    main()