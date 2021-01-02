from gpiozero import LED
from time import sleep

fan = LED(17)
temp_max=int(open("/home/<user>/.config/fan/config","r").read())

threshold = 0.4
count = 0

def run_fan(on):
    if on < 1:
        fan.off()
        sleep((1-on)*0.05)
    if on > 0.5:
        fan.on()
        sleep(on*0.05)


while True:
    temp = int(open("/sys/class/thermal/thermal_zone0/temp","r").read())
    on = min((temp)/(temp_max*10**3),1)
    on = ((threshold-(1-on))/threshold)
    run_fan(on)
    count+=1
    if count >= 100:
        with open("/home/<user>/log/fan_speed","w") as f:
            f.write(str(max(int(200*(on-0.5)),0))+"%")
        count=0
