import numpy as np
import matplotlib.pyplot as plt

def create_image(size, complexity):
    """
    Creates a random image with the specified size and complexity.

    Parameters
    ----------
    size : int
        The size of the image, in pixels.
    complexity : int
        The complexity of the image, as the number of random
        numbers used to generate it.

    Returns
    -------
    numpy.ndarray
        The generated image.
    """
    image = np.random.rand(size, size) * 255
    for _ in range(complexity):
        x = np.random.randint(0, size)
        y = np.random.randint(0, size)
        image[x, y] = np.random.rand() * 255
    return image

if __name__ == '__main__':
    size = 512
    complexity = 1000
    image = create_image(size, complexity)
    plt.imshow(image, cmap='gray')
    plt.show()