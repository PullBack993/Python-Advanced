import os

def get_extension(fls):
    report = {}
    for fl in fls:
        name_fl, extension_fl = fl.split(".")
        if extension_fl not in report:
            report[extension_fl] = []
        report[extension_fl].append(fl)
    return report
directory_content = os.listdir('.')
files = get_extension(directory_content)

result = ''
for extension, file_name in sorted(files.items(), key=lambda x: x[0]):
    result += f".{extension}\n"
    for name in file_name:
        result += f"- - - {name}\n"



with open('C:\\Users\\User\\PycharmProjects\\Python Advanced\\report.txt', 'w') as file:
    file.writelines(result)
