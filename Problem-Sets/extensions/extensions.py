filename = input("File name: ").strip().lower()

name, sep, extension = filename.rpartition(".")

match extension:
    case "gif" | "jpeg" | "png":
        print("image/" + extension)
    case "jpg":
        print("image/jpeg")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
