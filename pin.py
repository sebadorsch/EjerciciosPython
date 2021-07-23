def validate_pin(pin):
    str(pin)
    if len(pin) != 4 and len(pin) != 6:
        return False
    elif not pin.isdigit():
        return False
    else:
        return True


if __name__ == '__main__':
    print(validate_pin("1234"))