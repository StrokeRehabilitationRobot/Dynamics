import Dynamics
import numpy as np


class InverseController(object):
    def __init__(self, Kp, Kv):
        """

        :param Kp: numpy matrix
        :param Kv: numpy matrix
        """
        self._Kv = Kv
        self._Kp = Kp

    def get_torque(self, robot, q,qd,qdd):
        """

        :param robot: the robot
        :param trajectory: tuple of joint trajectories
        :return: the torqu input
        """

        q_measured = np.asarray(robot.q).reshap(3, 1)
        qd_measured = np.asarray(robot.qd).reshap(3, 1)

        q_desired = np.asarray(q).reshap(3, 1)
        qd_desired = np.asarray(qd).reshap(3, 1)
        qdd_desired = np.asarray(qdd).reshap(3, 1)

        aq = qdd_desired - self._Kv*(qd_measured - qd_desired ) - self._Kp*(q_measured - q_desired )

        M = Dynamics.make_mass_matrix(robot)
        C = Dynamics.make_coriolis_matrix(robot)
        G = Dynamics.make_gravity_matrix(robot)
        load = np.asarray(robot.tau).reshap(3, 1)

        u = M*aq + C*qd_measured + G + load



