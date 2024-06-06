import re

keywords = {
    "if": "KEYWORD",
    "else": "KEYWORD",
    "for": "KEYWORD",
    "while": "KEYWORD",
    "int": "KEYWORD",
    "float": "KEYWORD",
    "return": "KEYWORD",
}

operators = {
    "+": "OPERATOR",
    "-": "OPERATOR",
    "*": "OPERATOR",
    "/": "OPERATOR",
    "=": "OPERATOR",
    "<": "OPERATOR",
    ">": "OPERATOR",
    "==": "OPERATOR",
    "!=": "OPERATOR",
}


def identify_token(token):
    """
    Identifies the type of token based on the provided string.
    """
    if re.match(r"^\d+$", token):
        return "NUMBER"
    elif re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", token):
        return keywords.get(token, "IDENTIFIER")
    elif token in operators:
        return operators[token]
    else:
        return "UNKNOWN"


def main():
    """
    Main function to handle user interaction and tokenization.
    """
    while True:
        user_input = input("Enter source code (or 'q' to quit): ")
        if user_input == 'q':
            break

        # Tokenize user input
        tokens = []
        pattern = r"(\d+|[a-zA-Z_][a-zA-Z0-9_]*|[^\s\w])\s*"
        for match in re.findall(pattern, user_input):
            tokens.append((match.strip(), identify_token(match.strip())))

        # Print tokens
        if tokens:
            print("\nTokenized Input:")
            for token, token_type in tokens:
                print(f"{token}: {token_type}")

        # Check specific token
        check_token = input("\nEnter a token to identify (or 'q' to quit checking): ")
        while check_token != 'q':
            token_type = identify_token(check_token)
            print(f"{check_token}: {token_type}")
            check_token = input("\nEnter another token to identify (or 'q' to quit checking): ")


if __name__ == "__main__":
    main()