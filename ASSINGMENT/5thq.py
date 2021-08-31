# 5) Write Program - A train 340 m long is running at a speed of 45 km/hr. what time will it take to cross a 160 m long tunnel?

train_length=340
tunnel_length=160
#Total distance to be travelled by train
distance=train_length+tunnel_length
print("Total distance to be travelled by train:",distance,"meter")
#Conversion of km per hour into m per seconds
speed=(45*5)/18
print("Speed=",speed,"m/sec")
time=distance/speed
print("Time taken by train to cross the tunnel=",time,"sec")

