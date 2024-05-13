def write_to_file(filename, content):
    """
    Write content to a text file

    Parameters:
        filename (str): The name of the file to write to.
        content (str): The content to write to the file.

    Returns:
        bool: True if the operation successful, False otherwise
    """
    try:
        with open(filename, "w") as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Error occurred: {e}")
        return False
    
# Example usage:
# filename = 'example.txt'
# run = "0"
# stop = "1"
# if write_to_file(filename, stop):
#     print("Content has been written to the file successfully.")
# else:
#     print("Failed to write content to the file.")
