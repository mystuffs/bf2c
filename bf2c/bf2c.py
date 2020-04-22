bf_chars = {
    ',': 'scanf("%c", p);',
    '.': 'printf("%c", *p);',
    '[': 'while (*p) {',
    ']': '}',
    '>': '++p;',
    '<': '--p;',
    '+': '++(*p);',
    '-': '--(*p);'
}


def convert(bf: str, indent_style: str = '    ') -> str:
    indent = 1

    result = '#include <stdio.h>\n#include <stdlib.h>\n\nint main() {' \
             + indent_style + 'char *p = (char *)malloc(1000);\n'

    for c in bf:
        if c in bf_chars.keys():
            if c == ']':
                indent -= 1
            result += (indent_style * indent) + bf_chars[c]
            if c == '[':
                indent += 1

    result += '\n' + indent_style + 'free(p);' + indent_style + 'return 0;\n}'
    return result
