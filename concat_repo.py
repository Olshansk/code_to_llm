import argparse
import os


def get_files_with_extensions(repo_path, extensions, excluded_extensions):
    """
    Traverse the repository and return a list of files that match the given extensions.

    :param repo_path: Path to the Git repository
    :param extensions: List of file extensions to include
    :return: List of matched file paths
    """
    matched_files = []
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            skip = False
            for exc_ext in excluded_extensions:
                if file.endswith(exc_ext):
                    print(f"Excluding file: {file}")
                    skip = True
                    break
            if skip:
                continue
            if any(file.endswith(ext) for ext in extensions):
                matched_files.append(os.path.join(root, file))
    return matched_files


def concatenate_files(files):
    """
    Concatenate the content of the provided files into a single string.

    :param files: List of file paths to concatenate
    :return: Concatenated content as a string
    """
    concatenated_content = ""
    for file in files:
        with open(file, "r") as f:
            concatenated_content += f"File: {file}\n"
            concatenated_content += f.read() + "\n\n"
    return concatenated_content


def save_concatenated_repo(repo_path, extensions, excluded_extensions, output_path):
    """
    Save the concatenated content to an output file.

    :param content: Concatenated content to save
    :param output_path: Path to the output .txt file
    """
    files = get_files_with_extensions(repo_path, extensions, excluded_extensions)
    concatenated_content = concatenate_files(files)
    with open(output_path, "w") as f:
        f.write(concatenated_content)


def main(repo_path, extensions, excluded_extensions, output_path):
    """
    Main function to perform the concatenation of files and save the result.

    :param repo_path: Path to the Git repository
    :param extensions: List of file extensions to include
    :param excluded_extensions: List of file extensions to exclude
    :param output_path: Path to the output .txt file
    """
    save_concatenated_repo(repo_path, extensions, excluded_extensions, output_path)


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Concatenate files in a Git repo based on extensions"
    )
    parser.add_argument("repo_path", type=str, help="Path to the Git repository")
    parser.add_argument(
        "extensions",
        type=str,
        nargs="+",
        help="List of file extensions to include (e.g., .py .txt)",
    )
    parser.add_argument(
        "excluded_extensions",
        type=str,
        nargs="+",
        help="List of file extensions to exclude exclude (e.g., _test.go)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="output.diff",
        help="Output file path for concatenated content",
    )

    # Parse arguments
    args = parser.parse_args()

    # Run main function with parsed arguments
    main(args.repo_path, args.extensions, args.excluded_extensions, args.output)
