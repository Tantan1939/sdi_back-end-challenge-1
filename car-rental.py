from collections import namedtuple
import math


def app():
    seat = input("Please input number (seat): ")

    try:
        user_input = int(seat)

        rental_setting = namedtuple('option', ['Size', 'Seat', 'Cost'])

        car_rentals = [
            rental_setting('Small (S)', 5, 5000),
            rental_setting('Medium (M)', 10, 8000),
            rental_setting('Large (L)', 15, 12000),
        ]

        selected_car = {
            "size": "",
            "number_of_car": 0,
            "total": 0
        }

        for index, rental in enumerate(car_rentals):
            number_of_car = math.ceil(user_input / rental.Seat)
            rental_cost = rental.Cost * number_of_car

            if index == 0 or rental_cost < selected_car["total"]:
                selected_car["size"] = rental.Size
                selected_car["number_of_car"] = number_of_car
                selected_car["total"] = rental_cost

        print(
            f"{selected_car['size']} x {selected_car['number_of_car']} \nTotal = PHP {selected_car['total']}")

    except ValueError:
        print("You can only input an integer value. Try again.")


app()
