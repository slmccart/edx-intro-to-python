def main():
    prompt = input("What time is it? ").strip()
    float_time = convert(prompt)

    if 7 <= float_time <= 8:
        print("breakfast time")
    elif 12 <= float_time <= 13:
        print("lunch time")
    elif 18 <= float_time <= 19:
        print("dinner time")

def convert(time):
    hour, minute = time.split(":")
    hour = int(hour)
    minute = int(minute) / 60

    return hour + minute

if __name__ == "__main__":
    main()
