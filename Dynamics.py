from math import sin as s
from math import cos as c
import numpy as np


class RoboticArm(object):

    def __init__(self):
        self.link_lengths = [1,1,1]
        self.link_centroid = [0.5,0.5,0.5]
        self.link_masses = [1,1,1]
        self.link_inertia = [[1,1,1],[1,1,1],[1,1,1]]

    def make_mass_matrix(self,theta_1,theta_2,theta_3):

        """

        :type theta_1: object
        """
        M_11 =  self.link_inertia[2][2]*s(theta_2)**2 + self.link_inertia[3][2]*s.(theta_2+theta_3)**2 + \
                self.link_inertia[1][3] + self.link_inertia[2][3] *c(theta_2)**2 + \
                self.link_inertia[2][3] *c(theta_2+theta_3)**2
        M_12 = 0

        M_13 = 0
        M_21 = 0
        M_22 = self.link_inertia[2][1] + self.link_inertia[3][1] + self.link_masses[3]*self.link_lengths[1]**2 + \
               self.link_masses[2]*self.link_centroid[1]**2 + self.link_masses[2]**2 + \
               2*self.link_masses[3]*self.link_lengths[1]*self.link_centroid[2]*c(theta_3)

        M_23 = self.link_inertia[3][1] + self.link_masses[3]*self.link_centroid[2]**2 + \
               self.link_masses[3]*self.link_lengths[1]*self.link_centroid[2]*c(theta_3)


        M_31 = 0
        M_32 =  self.link_inertia[3][1] + self.link_masses*self.link_centroid[2]**2 + \
                self.link_masses[3]*self.link_lengths[2]*self.link_centroid[2]*c(theta_3)
        M_33 = self.link_inertia[3][1] + self.link_masses[3]*self.link_centroid[2]**2



        M = np.matrix([ [ M_11, M_12, M_13],
                        [ M_21, M_22, M_23],
                        [ M_31, M_32, M_33] ] )
        return  M

    def make_gravity_matrix(self,theta_1,theta_2,theta_3):


        gravity = 9.81

        G_1 = 0


        G_2 = -(self.link_masses[2]*self.link_centroid[1] + self.link_masses[3]*self.link_lengths[1])*gravity*c(theta_2) \
              -self.link_masses[3]*self.link_centroid[2]*c(theta_2+theta_3)

        G_3 = -self.link_masses[3]*gravity*self.link_centroid[2]*c(theta_2+theta_3)

        G = np.matrix[ [ G_1 ], [ G_2 ], [ G_3 ] ]


        return G

        pass
    def make_coriolis_matrix(self):
        pass
    def get_jacoboian_matrix(self):
        pass

