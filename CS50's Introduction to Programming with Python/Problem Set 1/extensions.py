name = input("File name: ")

name=name.replace(" ", "")

if ".jpg" in name:
    print("image/jpeg")
elif ".jpeg" in name:
    print("image/jpeg")
elif ".gif" in name:
    print("image/gif")
elif ".png" in name:
    print("image/png")
elif ".pdf" in name:
    print("application/pdf")
elif ".txt" in name:
    print("text/plain")
elif ".zip" in name:
    print("application/zip")
else:
    print("Not valid")
