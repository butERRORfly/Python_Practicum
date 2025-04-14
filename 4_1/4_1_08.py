def is_palindrome(records):
    if isinstance(records, int):
        return True if str(records) == str(records)[::-1] else False
    else:
        return True if records == records[::-1] else False
