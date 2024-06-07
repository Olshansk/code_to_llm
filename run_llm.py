import argparse
import os

from openai import OpenAI

import prompts

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Function to read data from concat.txt
def read_data(file_path):
    """
    Read the content of the specified file.

    :param file_path: Path to the file to read
    :return: Content of the file
    """
    with open(file_path, "r") as file:
        return file.read()


# Function to send data to GPT-4 and get the response
def get_gpt4_response(data, custom_prompt, programming_language):
    """
    Send data and a custom prompt to GPT-4 and retrieve the response.

    :param data: The concatenated file content to send to GPT-4
    :param custom_prompt: The custom prompt to guide GPT-4
    :param programming_language: The programming language to specify in the system message
    :return: The response from GPT-4
    """
    # Ensure the API key is set

    # System message for GPT-4 to specify its role
    system_message = {
        "role": "system",
        "content": f"You are an expert {programming_language} programmer.",
    }

    # User message with the custom prompt and the data
    user_message = {"role": "user", "content": f"{custom_prompt}\n\n{data}"}

    # Send the request to GPT-4 and get the response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k", messages=[system_message, user_message]
    )

    # Return the content of the response
    return response.choices[0].message.content


# Function to save response to a .diff file
def save_to_diff_file(response, output_path):
    """
    Save the GPT-4 response to a .diff file.

    :param response: The response content from GPT-4
    :param output_path: Path to the output .diff file
    """
    with open(output_path, "w") as file:
        file.write(response)


# Main function to coordinate reading, processing, and saving
def main(file_path, custom_prompt, programming_language, output_path):
    """
    Main function to generate a unit test diff using GPT-4.

    :param file_path: Path to the concat.txt file
    :param custom_prompt: Custom prompt for GPT-4
    :param programming_language: Programming language for the system message
    :param output_path: Path to the output .diff file
    """
    # Read the data from concat.txt
    data = read_data(file_path)

    # Get the GPT-4 response
    response = get_gpt4_response(data, custom_prompt, programming_language)

    # Save the response to a .diff file
    save_to_diff_file(response, output_path)

    print(f"Response saved to {output_path}")


# Entry point of the script
if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate a unit test using GPT-4")
    parser.add_argument("file_path", type=str, help="Path to the concat.txt file")
    parser.add_argument(
        "output",
        type=str,
        default="",
        help="Output file path for the diff content",
    )
    parser.add_argument("--custom_prompt", type=str, help="Custom prompt for GPT-4")
    parser.add_argument(
        "--programming_language",
        type=str,
        default="Golang",
        help="Programming language for the system message",
    )

    # Parse arguments
    args = parser.parse_args()

    if args.custom_prompt == "":
        # args.custom_prompt = prompts.get_ring_prompt(args.programming_language)
        args.custom_prompt = prompts.get_smt_prompt()

    # Run main function with parsed arguments
    main(args.file_path, args.custom_prompt, args.programming_language, args.output)
