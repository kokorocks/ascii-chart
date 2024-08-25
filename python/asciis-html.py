def generate_html_chart():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ASCII Characters Chart</title>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h1>ASCII Characters Chart</h1>
        <table>
            <tr>
                <th>Char</th>
                <th>Decimal</th>
                <th>Hex</th>
                <th>Binary</th>
            </tr>
    """
    
    # ASCII printable characters range from 32 to 126
    for code in range(32, 55296):
        print(code)
        char = chr(code)
        decimal = code
        hex_code = format(code, 'X')  # Uppercase hex format
        binary = format(code, '08b')  # 8-bit binary format
        html_content += f"""
            <tr>
                <td>{char}</td>
                <td>{decimal}</td>
                <td>{hex_code}</td>
                <td>{binary}</td>
            </tr>
        """
    
    # ASCII control characters range from 0 to 31 and 127
    '''for code in range(0, 32):
        char = chr(code) if code != 0 else 'NUL'  # NUL for 0
        decimal = code
        hex_code = format(code, 'X')
        binary = format(code, '08b')
        html_content += f"""
            <tr>
                <td>{char}</td>
                <td>{decimal}</td>
                <td>{hex_code}</td>
                <td>{binary}</td>
            </tr>
        """
    
    # ASCII 127 (DEL)
    char = chr(127)
    decimal = 127
    hex_code = format(127, 'X')
    binary = format(127, '08b')
    html_content += f"""
        <tr>
            <td>{char}</td>
            <td>{decimal}</td>
            <td>{hex_code}</td>
            <td>{binary}</td>
        </tr>
    """'''
    
    html_content += """
        </table>
    </body>
    </html>
    """
    
    # Write to HTML file with UTF-8 encoding
    with open("index.html", "w", encoding="utf-8") as file:
        file.write(html_content)

if __name__ == "__main__":
    generate_html_chart()