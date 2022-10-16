import fastf1
from matplotlib import pyplot as plt
session = fastf1.get_session(2022, 'Silverstone', 'R')
session.load
speed_sainz = session.laps.pick_driver('SAI').pick_fastest
sai_car_data = speed_sainz.get_car_data()
t = sai_car_data['time']
spd = sai_car_data['speed']

fig, ax = plt.subplots()
ax.plot(t, spd, label='Speed', color='blue')
ax.set_ylabel('Speed in Km/H')
ax.set_xlabel('Time')
ax.set_title('Sainz speed over laps')
ax.legend()
plt.show()  