def secret_replace(text, **replaces):
    records = ''
    for letter in text:
        if letter in replaces:
            records += replaces[letter][0]
            replaces[letter] = replaces[letter][1:] + (replaces[letter][0],)
        else:
            records += letter
    return records
