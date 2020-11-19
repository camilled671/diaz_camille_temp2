tempf =70
while True:
    print("temperature"+input.temperature(TemperatureUnit.FAHRENHEIT))
    if input.temperature(TemperatureUnit.FAHRENHEIT) > tempf:
        light.set_pixel_color(5, light.rgb(255, 0, 0))
    elif :
        if input.temperature(TemperatureUnit.FAHRENHEIT) < tempf:
            light.set_pixel_color(5, light.rgb(0, 0, 255))
