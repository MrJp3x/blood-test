import jdatetime


def present_date():
    # months = ["Farvardin", "Ordibehesht", "Khordad", "Tir", "Mordad", "Shahrivar", "Mehr", "Aban", "Azar", "Dey",
    #           "Bahman", "Esfand"]
    
    now = jdatetime.datetime.now()
    # month_name = months[now.month - 1]
    formatted_date = now.strftime(f'%a %H:%M:%S %d/%m/%Y')

    return formatted_date


print(present_date())

