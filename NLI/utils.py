import numpy as np
from skimage import io
import matplotlib.pyplot as plt


def print_img_info(img: np.ndarray) -> None:
    """
    Print image information

    Args:
        img (np.ndarray): Image for which information is printed
    """
    print(
        f"img.shape: {img.shape}\n"
        f"img.dtype: {img.dtype}\n"
        f"Range of value: {img.min()}-{img.max()}\n"
    )


def iprint(
    img: np.ndarray,
    title: str = "",
    info: bool = False,
) -> None:
    """
    Image displaying, can print information and the title of the image.

    Args:
        img (np.ndarray): Image which is displayed
        title (str, optional): Title of the image. Defaults to ''.
        info (bool, optional): If information is displayed or not. Defaults to False.
    """
    if info:
        print(f"{ f' {title} ':-^50}\n")
        print_img_info(img)
    plt.figure()
    plt.axis("off")
    plt.title(title)
    io.imshow(img)


def mean_image(img: np.ndarray) -> np.ndarray:
    """
    Compute the mean of an image with an alpha channel without counting
    transparent pixels.

    Args:
        img (np.ndarray): Image for which the mean is computed

    Returns:
        np.ndarray: The mean of the input image based on non transparent
        pixel (alpha value equals 1).
    """
    return img[img[:, :, 3] == 1].mean(0)[:3]
