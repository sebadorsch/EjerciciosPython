import datetime

def format_duration(total_seconds):
    result = ""

    formated_time = datetime.timedelta(seconds=total_seconds)

    return(result)




if __name__ == '__main__':

    print(format_duration(1), "1 second")
    print(format_duration(62), "1 minute and 2 seconds")
    print(format_duration(120), "2 minutes")
    print(format_duration(3600), "1 hour")
    print(format_duration(3662), "1 hour, 1 minute and 2 seconds")
    print(format_duration(565653662))