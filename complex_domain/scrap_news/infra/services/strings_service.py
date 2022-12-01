

def fix_encoding(text):
    return text.encode('iso-8859-1').decode("UTF-8")
    

def clear_string(text):
    try:
        return fix_encoding(text).strip()
    except:
        return text