from matplotlib import pyplot as plt
def show_images(imgs, num_rows, num_cols, titles = None, scale = 1.5):
    figsize = (num_cols * sscale, num_rows * scale)
    _, axes = plt.subplot(num_rows, num_cols, figsize=figsize)
    axies = axes.flatten()
    for i, (ax, img) in enumerate(zip(axes, imgs)):
        if torch.is_tensor(img):
            ax.imshow(img.numpy())
            else:
                ax.imshow(img)
            ax.axes.get_xaxis().set_visible(False)
            ax.axes.get_yaxis().set_visible(False)
            if titles:
                ax.set_title(titles[i])
        return axes
