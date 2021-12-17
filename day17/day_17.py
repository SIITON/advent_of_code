import matplotlib.pyplot as plt
import numpy as np

target_x = np.array([70, 96])
target_y = np.array([-179, -124])

#  Max initial x velocity is determined by the integer n such that n(n+1)/2 is within target_x:
initial_x_vel = [12, 13]
#  Then we just shoot the probe in to heaven and it drops down in to the target area at high velocity.
#  initial y vel = abs(target_y.min()) + 1 = 178

def compute_trajectory(x, y):
    if x > 0:
        x -= 1  # Due to drag
    y -= 1      # Due to gravity
    return [x, y]


def send_probe(x_vel, y_vel):
    xx = np.array([0])
    yy = np.array([0])
    step = 0
    while True:
        xx = np.append(xx, xx[step] + x_vel)
        yy = np.append(yy, yy[step] + y_vel)
        if target_x.max() >= xx[-1] >= target_x.min() and target_y.max() >= yy[-1] >= target_y.min():
            return xx, yy, True
        if xx[-1] > target_x.max() or yy[-1] < target_y.min():
            return xx, yy, False
        [x_vel, y_vel] = compute_trajectory(x_vel, y_vel)
        step += 1


y_max = 0
hit_counts = 0
for x_vel in range(target_x.max() + 1):
    for y_vel in range(target_y.min(), abs(target_y.min()) + 1):
        hit = False
        X, Y, hit = send_probe(x_vel, y_vel)
        if hit:
            hit_counts += 1
        if hit and Y.max() > y_max:
            y_max = Y.max()
            velocity_x = x_vel
            velocity_y = y_vel

X, Y, hit = send_probe(velocity_x, velocity_y)
print("Initial x vel:", velocity_x)
print("Initial y vel:", velocity_y)

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(0, 0, 'k*')
# plot target area.
plt.plot([target_x[0], target_x[0], target_x[1], target_x[1]], [target_y[0], target_y[1], target_y[0], target_y[1]], '*')
plt.plot(X, Y, '.')
plt.xlim(-100, 200)
ax.set_aspect('equal', adjustable='box')
plt.show()
print("Highest point: ", Y.max())
print("Number of hits: ", hit_counts)
