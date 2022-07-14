import json

import pyzstd
from rich.console import Console
from rich.syntax import Syntax

console = Console()


def main():
    while True:
        console.print('paste hex pls. Then send EOF or ENTER.')

        hex_string = ''
        try:
            while True:
                line = input()
                if not line:
                    break

                hex_column = line.split('  ')[1]
                hex_column = hex_column[:47]  # Sometimes 3rd column clips to 2nd.
                hex_string += ' ' + hex_column

        except EOFError:
            pass

        body_compressed = bytearray.fromhex(hex_string)
        body_decompressed = pyzstd.decompress(body_compressed)
        body_str = body_decompressed.decode('utf-8')
        body_json = json.loads(body_str)
        pretty_json = json.dumps(body_json, indent=4, sort_keys=False)

        syntax = Syntax(pretty_json, "json", theme="monokai", line_numbers=True)
        console.print(syntax)


if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        console.print('Bye bye')
