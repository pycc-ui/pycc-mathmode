import numpy as np
import matplotlib.pyplot as plt
class TSP:
    def __init__(self,coordinates):
        self.coordinates = coordinates
        self.distance_matrix = self._distance()
    def _distance(self):
        distance_matrix = np.zeros([len(self.coordinates),
                                    len(self.coordinates)])
        for i in range(len(self.coordinates)):
            for j in range(len(self.coordinates)):
                distance_matrix[i][j] = np.linalg.norm(self.coordinates[i]-self.coordinates[j])
        return distance_matrix
    def plt(self):
        for i in self.coordinates:
            plt.plot(i[0],i[1],'o',color = 'red')
        plt.show()