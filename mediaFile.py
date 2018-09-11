def isMedia(extension):
    extns = ['.mp4','.avi','.mpg','.mkv','.mov','.flv','.3gp']
    if extension in extns:
        return True
    else:
        return False
