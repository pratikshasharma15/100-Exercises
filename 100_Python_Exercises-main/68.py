d = dict(weather="clima", earth="terra", rain="chuva")

user_input = input("Enter Your Input: ").lower()

match user_input:
    case "weather":
        print(d[user_input])
    case "earth":
        print(d[user_input])
    case "rain":
        print(d[user_input])
    case _:
        print("We couldn't find that word!")
