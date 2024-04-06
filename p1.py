# https://blog.51cto.com/u_16175475/7139037

file_content = "print('Hello World!')"  # Content for the new Python file

# Writing content to a new Python file
with open("p1_created.py", "w") as file:
    file.write(file_content)

