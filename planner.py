# Type of planner
POINT_PLANNER=0; TRAJECTORY_PLANNER=1

TRAJECTORY_TYPE = 'sigmoid' # change manually

STEP = 0.1
X_MAX_PARABOLA = 1.5
X_MAX_SIGMOID  = 2.5

import math

class planner:
    def __init__(self, type_):

        self.type=type_

    
    def plan(self, goalPoint=[-1.0, -1.0]):
        
        if self.type==POINT_PLANNER:
            return self.point_planner(goalPoint)
        
        elif self.type==TRAJECTORY_PLANNER:
            return self.trajectory_planner()


    def point_planner(self, goalPoint):
        x = goalPoint[0]
        y = goalPoint[1]
        return x, y

    # TODO Part 6: Implement the trajectories here
    def trajectory_planner(self):
        out = []

        if TRAJECTORY_TYPE == "parabola":
            n = int(round(X_MAX_PARABOLA / STEP)) + 1
            for i in range(n):
                x = i * STEP
                out.append([x, x*x])

        if TRAJECTORY_TYPE == "sigmoid":
            n = int(round(X_MAX_SIGMOID / STEP)) + 1
            for i in range(n):
                x = i * STEP
                s = 1.0 / (1.0 + math.exp(-2.0*x))
                y = 2.0*s - 1.0
                out.append([x, y])
        return out

        # pass
        # the return should be a list of trajectory points: [ [x1,y1], ..., [xn,yn]]
        # return 

