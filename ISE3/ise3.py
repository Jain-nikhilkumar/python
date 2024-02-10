    def replace_word_in_file(input_file, output_file):
        with open(input_file, 'r') as file:
            content = file.read()

        modified_content = content.replace('is', 'was')

        with open(output_file, 'w') as file:
            file.write(modified_content)

        print("File processed successfully!")


    input_filename = "TestFile1.txt"
    output_filename = "TestFile2.txt"

    replace_word_in_file(input_filename, output_filename)