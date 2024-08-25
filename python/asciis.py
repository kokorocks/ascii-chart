def print_ascii_characters():
    print(f"{'Char':<6} {'Decimal':<10} {'Hex':<6} {'Binary':<10}")
    print("-" * 32)
    
    # ASCII printable characters range from 32 to 126
    for code in range(0, 55296):
        char = chr(code)
        decimal = code
        hex_code = format(code, 'X')  # Uppercase hex format
        binary = format(code, '08b')  # 8-bit binary format
        print(f"{char:<6} {decimal:<10} {hex_code:<6} {binary:<10}")
    
    # ASCII control characters range from 0 to 31 and 127
    # ASCII 127 (DEL)
    char = chr(127)
    decimal = 127
    hex_code = format(127, 'X')
    binary = format(127, '08b')
    print(f"{char:<6} {decimal:<10} {hex_code:<6} {binary:<10}")

if __name__ == "__main__":
    print_ascii_characters()