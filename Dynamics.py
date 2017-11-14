from math import sin as s
from math import cos as c
import numpy as np



l = [1, 1, 1]
r = [0.5, 0.5, 0.5] # r0 r1 r2
m = [1, 1, 1]
I = [[1, 1, 1], [1, 1, 1], [1, 1, 1]] # Ix Iy Iz

def make_mass_matrix(theta):

    """

    :type theta_1: object
    """

    theta_1 = theta[0]
    theta_2 = theta[1]
    theta_3 = theta[2]

    M_11 = I[1][1] * s(theta_2) ** 2 + I[2][1] * s(theta_2 + theta_3) ** 2 + \
           I[0][2] + I[1][2] * c(theta_2) ** 2 + \
           I[1][2] * c(theta_2 + theta_3) ** 2
    M_12 = 0

    M_13 = 0
    M_21 = 0
    M_22 = I[1][0] + I[2][0] + m[2] * lengths[0] ** 2 + \
           m[1] * r[0] ** 2 + m[1] ** 2 + \
           2 * m[2] * lengths[0] * r[1] * c(theta_3)

    M_23 = I[2][0] + m[2] * r[1] ** 2 + \
           m[2] * lengths[0] * r[1] * c(theta_3)


    M_31 = 0
    M_32 = I[2][0] + m[2] * r[1] ** 2 + \
           m[2] * l[1] * r[1] * c(theta_3)
    M_33 = I[2][0] + m[2] * r[1] ** 2



    M = np.matrix([ [ M_11, M_12, M_13],
                    [ M_21, M_22, M_23],
                    [ M_31, M_32, M_33] ] )
    return  M

def make_gravity_matrix(theta):

    theta_1 = theta[0]
    theta_2 = theta[1]
    theta_3 = theta[2]

    gravity = 9.81

    G_1 = 0


    G_2 = -(m[1] * r[0] + m[2] * lengths[0]) * gravity * c(theta_2) \
          - m[2] * r[1] * c(theta_2 + theta_3)

    G_3 = -m[2] * gravity * r[1] * c(theta_2 + theta_3)

    G = np.matrix([ [ G_1 ], [ G_2 ], [ G_3 ] ])


    return G


def make_coriolis_matrix(theta):


    theta_1 = theta[0]
    theta_2 = theta[1]
    theta_3 = theta[2]

    theta_23 = theta_2 + theta_3
    C =  np.zeros(shape=(3,3))

    gamma_001 = 0.5*( I[1][2] - I[2][2] - m[1]*r[1]^2)*s(2*theta_2) + 0.5*(  I[2][1] - I[2][2] )*s(2*theta_23) \
                 -m[2]*(l[1]*c(theta_2) + r[2]*c(theta_23))*(l[1]*s(theta_2) + r[2] *s(theta_23))

    gamma_002 = 0.5*(I[2][1] - I[2][2])*c(2*theta_23) -m[2]*r[2]*s(theta_23)*(l[1] *c(theta_2) + r[2]*c(theta_23))

    gamma_010 = 0.5*(I[1][1] - I[1][2] - m[1]*r[1]^2 )*c(2*theta_2) + 0.5*( I[2][1] - I[2][2])*c(2*theta_2) \
                - m[2]*(  l[1]*c(theta_2) + r[2]*c(theta_23) )*( l[1]*s(theta_2) + r[2]*s(theta_23)  )

    gamma_020 = 0.5*( I[2][1] - I[2][2] )*sin(2*theta_23) - m[2]*r[2]*s(theta_23)*( l[1]*c(theta_2) + r[2]*c(theta_23))

    gamma_100 = 0.5*(I[1][2] - I[1][1] + m[1]*r[1]^2)*s(2*theta_2) + 0.5*(I[2][2] - I[2][1])*s(2*theta_23) + \
                m[2]*( l[1]*c(theta_2) + r[2]*c(theta_23) )*(l[1]*s(theta_2) +  r[2]*s(theta_23) )


    gamma_112 = -l[1]*m[2]*r[2]*s(theta_3)

    gamma_121 = gamma_112
    gamma_122 = gamma_112


    gamma_200 = 0.5*(I[2][2] - I[2][1]) + m[1]*r[2]*s(theta_23)*(l[1]*c(theta_2) + r[2]*c(theta_23))
    gamma_211 = l[1]*m[2]*r[2]*s(theta_3)


    C[0,0] = gamma_001 + gamma_002
    C[0, 1] = gamma_010
    C[0, 2] = gamma_020
    C[1,0] = gamma_100
    C[1, 1] = gamma_112
    C[1, 2] = gamma_121 + gamma_122

    C[2,0] = gamma_200
    C[2,1] = gamma_211


    return C




def get_jacoboian_matricies(theta):

    theta_1 = theta[0]
    theta_2 = theta[1]
    theta_3 = theta[2]


    J_1 =  np.zeros(shape=(6,3))
    J_1[5,0] = 1


    J_2 = np.matrix(  [ [-r[0] * c(theta_2), 0, 0],
                        [  0,                              0,                0],
                        [0, -r[0], 0],
                        [  0,                             -1,                0],
                        [  -s(theta_2),                    0,                0],
                        [c(theta_2),                       0,                0] ] )

    J_3 = np.matrix( [ [l[1] * c(theta_2) - r[1] * c(theta_2 + theta_3), 0, 0],
                       [0, l[0] * s(theta_1), 0],
                       [0, -l[1] - l[0] * c(theta_3), -r[1]],
                       [ 0,                                          -1,                    -1 ],
                       [-s(theta_2+theta_3),                          0,                     0 ],
                       [c(theta_2+theta_3),                           0,                     0 ] ])

    return (J_1, J_2, J_3)



print get_jacoboian_matricies([3.14,3.14,3.14])