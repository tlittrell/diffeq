import numpy as np

# Physical constants
g = 9.8
pendulum_length = 2
air_resistance = 0.1

# Initial conditions
THETA_0 = np.pi / 3
THETA_DOT_0 = 0


def get_theta_double_dot(theta, theta_dot) -> float:
    return -air_resistance * theta_dot - (g / pendulum_length) * np.sin(theta)


def theta(t):
    # Initialize angle and angular velocity
    theta = THETA_0
    theta_dot = THETA_DOT_0
    delta_t = 0.1  # time step
    for _ in np.arange(0, t, delta_t):
        theta_double_dot = get_theta_double_dot(theta, theta_dot)
        theta += theta_dot * delta_t
        theta_dot = theta_double_dot * delta_t
    return theta
