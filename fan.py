from gpiozero import LED
from time import sleep

fan = LED(17)
temp_max = int(open("/home/<user>/.config/fan/config","r").read())

while True:
    temp = int(open("/sys/class/thermal/thermal_zone0/temp","r").read()) // 1000 * 1000
    on = min(temp/(temp_max*10),100)
    if on>=100:
        fan.on()
        sleep(1)
    elif on<80:
        fan.off()
        sleep(1)
    else:
        on = ((20-(100-on))/20)*10**-1
        for _ in range(10):
            fan.on()
            sleep(on)
            fan.off()
            sleep((0.1-on))
        on*=1000
    with open("/home/<user>/log/fan_speed","w") as f:
        f.write(str(int(on))+"%")

