import sys
from PIL import Image

if len(sys.argv) < 3:
    print("Too few command-line arguments")
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
else:
    (root1, ext1) = os.path.splitext(sys.argv[1])
    (root2, ext2) = os.path.splitext(sys.argv[2])
    if ext1 not in ["jpg","png","jpeg"]:
        sys.exit("Invalid input")
    elif ext2 not in ["jpg","png","jpeg"]:
        sys.exit("Invalid output")
    elif ext1 != ext2:
        sys.exit("Input and output have different extensions")
    else:
        try:
            shirt = Image.open("shirt.png")
            before = Image.open(sys.argv[1])
            size = shirt.size
            after = before.paste(shirt,size)
            after_file = "after. " + ext2
            after.save(after_file)
        except FileNotFoundError:
            sys.exit("File does not exist")

