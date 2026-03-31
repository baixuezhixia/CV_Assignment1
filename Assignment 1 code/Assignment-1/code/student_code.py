import numpy as np

def my_imfilter(image, filter):
  """
  Apply a filter to an image. Return the filtered image.

  Args
  - image: numpy nd-array of dim (m, n, c)
  - filter: numpy nd-array of dim (k, k)
  Returns
  - filtered_image: numpy nd-array of dim (m, n, c)

  HINTS:
  - You may not use any libraries that do the work for you. Using numpy to work
   with matrices is fine and encouraged. Using opencv or similar to do the
   filtering for you is not allowed.
  - I encourage you to try implementing this naively first, just be aware that
   it may take an absurdly long time to run. You will need to get a function
   that takes a reasonable amount of time to run so that the TAs can verify
   your code works.
  - Remember these are RGB images, accounting for the final image dimension.
  """

  assert filter.shape[0] % 2 == 1
  assert filter.shape[1] % 2 == 1

  ############################
  ### TODO: YOUR CODE HERE ###

  # Handle both grayscale (2D) and color (3D) images uniformly
  squeeze = False
  if image.ndim == 2:
    image = image[:, :, np.newaxis]
    squeeze = True

  m, n, c = image.shape
  fh, fw = filter.shape
  ph, pw = fh // 2, fw // 2

  # Pad image with reflected content to preserve edge information
  padded = np.pad(image, ((ph, ph), (pw, pw), (0, 0)), mode='reflect')

  # Accumulate the weighted, shifted copies of the padded image
  filtered_image = np.zeros_like(image, dtype=np.float32)
  for i in range(fh):
    for j in range(fw):
      filtered_image += filter[i, j] * padded[i:i + m, j:j + n, :]

  if squeeze:
    filtered_image = filtered_image[:, :, 0]

  ### END OF STUDENT CODE ####
  ############################

  return filtered_image

def create_hybrid_image(image1, image2, filter):
  """
  Takes two images and creates a hybrid image. Returns the low
  frequency content of image1, the high frequency content of
  image 2, and the hybrid image.

  Args
  - image1: numpy nd-array of dim (m, n, c)
  - image2: numpy nd-array of dim (m, n, c)
  Returns
  - low_frequencies: numpy nd-array of dim (m, n, c)
  - high_frequencies: numpy nd-array of dim (m, n, c)
  - hybrid_image: numpy nd-array of dim (m, n, c)

  HINTS:
  - You will use your my_imfilter function in this function.
  - You can get just the high frequency content of an image by removing its low
    frequency content. Think about how to do this in mathematical terms.
  - Don't forget to make sure the pixel values are >= 0 and <= 1. This is known
    as 'clipping'.
  - If you want to use images with different dimensions, you should resize them
    in the notebook code.
  """

  assert image1.shape[0] == image2.shape[0]
  assert image1.shape[1] == image2.shape[1]
  assert image1.shape[2] == image2.shape[2]

  ############################
  ### TODO: YOUR CODE HERE ###

  # Low-pass filter image1 to keep only its low frequencies
  low_frequencies = my_imfilter(image1, filter)

  # High-pass filter image2: subtract its blurred version to keep edges/details
  high_frequencies = image2 - my_imfilter(image2, filter)

  # Combine and clip pixel values to valid [0, 1] range
  hybrid_image = np.clip(low_frequencies + high_frequencies, 0.0, 1.0)

  ### END OF STUDENT CODE ####
  ############################

  return low_frequencies, high_frequencies, hybrid_image
