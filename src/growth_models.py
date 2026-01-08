import numpy as np
import matplotlib.pyplot as plt

class GompertzGrowth:
    """
    Implements the Gompertz growth model.
    """

    def __init__(self, a: float, b: float, c: float):
        """
        Initializes the Gompertz growth model with parameters.

        Parameters:
        a (float): The upper asymptote.
        b (float): The displacement along the x-axis.
        c (float): The growth rate.
        """
        self.a = a
        self.b = b
        self.c = c

    def evaluate(self, t: np.ndarray) -> np.ndarray:
        """
        Evaluates the Gompertz function at given time points.

        Parameters:
        t (np.ndarray): Array of time points.

        Returns:
        np.ndarray: Evaluated values of the Gompertz function.
        """
        return self.a * np.exp(-self.b * np.exp(-self.c * t))
    
    def plot(self, t: np.ndarray) -> None:
        values = self.evaluate(t)
        plt.plot(t, values)
        plt.title("Spheroid Growth vs. Time (Gompertz Model)")
        plt.xlabel("Time")
        plt.ylabel("Growth")
        plt.show()
    
if __name__ == "__main__":

    model = GompertzGrowth(a=1.0, b=2.0, c=0.5)
    time_points = np.linspace(0, 10, 100)

    # Evaluate and print growth values
    growth_values = model.evaluate(time_points)
    print(growth_values)

    # Plot the growth curve
    model.plot(time_points)