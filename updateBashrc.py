import os
import re

def getFileContent(filePath):
    """
    Reads the content of a file and returns it as a list of lines.
    """
    with open(filePath, 'r') as file:
        return file.readlines()


def writeFileContent(filePath, content):
    """
    Writes a list of lines to a file.
    """
    with open(filePath, 'w') as file:
        file.writelines(content)


def main():
    # Get the path to the user's home directory
    homeDirectory = os.path.expanduser("~")

    # Define the path to the .bashrc file
    bashrcPath = os.path.join(homeDirectory, ".bashrc")

    if not os.path.exists(bashrcPath):
       print(f"{bashrcPath} does not exist.")
       return

    bashrcContent = getFileContent(bashrcPath)
    colorCodeBashrcContent = getFileContent("bashrcColorCode")

    colorCodeFound = False
    newBashrcContent = []
    for line in bashrcContent:
        if re.search(r"^#{47}\s*BASH\s*COLOR\s*UPDATE\s*SCRIPT\s*#{47}$", line):
            colorCodeFound = True

        if re.search(r"^#{45}\s*END\s*BASH\s*COLOR\s*UPDATE\s*SCRIPT\s*#{45}$", line):
            colorCodeFound = False
            continue

        if  not colorCodeFound:
            # Remove the line from bashrcContent
            newBashrcContent.append(line)

    # if the last line of bashrcContent is not a new line, add a new line
    if newBashrcContent[-1] != "\n":
        colorCodeBashrcContent[0] = f"\n\n{colorCodeBashrcContent[0]}"

    # extend the newBashrcContent with colorCodeBashrcContent
    newBashrcContent.extend(colorCodeBashrcContent)

    # move the old .bashrc file to .bashrc_old
    os.rename(bashrcPath, bashrcPath+"_old")
    writeFileContent(bashrcPath, newBashrcContent)


def runBashrc():
    """
    create a new bash session to run the .bashrc file
    """
    newScript = [
        "#!/bin/bash\n\n",
        "source ~/.bashrc\n",
        "exec bash\n"
    ]
    writeFileContent("runBashrc.sh", newScript)


if __name__ == "__main__":
    main()
    runBashrc()
