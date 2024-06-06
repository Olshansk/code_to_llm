import sys

import tiktoken


def estimate_tokens_in_file(file_path):
    """
    Estimate the number of tokens in a .txt file using tiktoken.

    :param file_path: Path to the .txt file
    :return: Estimated number of tokens
    """
    # Load the file content
    with open(file_path, "r") as file:
        text = file.read()

    # Choose the tokenizer for the model you are using
    # For example, let's use the tokenizer for GPT-3
    # encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    encoding = tiktoken.encoding_for_model("gpt-4o")

    # Tokenize the text
    tokens = encoding.encode(text)

    # Return the number of tokens
    return len(tokens)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python estimate_tokens.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    estimated_tokens = estimate_tokens_in_file(file_path)
    print(f"Estimated number of tokens in {file_path}: {estimated_tokens}")
