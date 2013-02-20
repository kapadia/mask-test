
import numpy
import Image


def createMask():
  
  # Open image and mask using PIL
  im = Image.open('CFHTLS_082_0389_gri.png')
  im_mask = Image.open('CFHTLS_082_0389_b_gri.png')
  
  # Convert to grayscale
  im_mask = im_mask.convert('L')
  
  # Get numpy array representation
  mask = numpy.asarray(im_mask)
  
  # Make array writable
  mask.flags.writeable = True
  
  # For SW purposes only need binary mask
  mask[numpy.where(mask > 0)] = 255
  mask[numpy.where(mask != 255)] = 254
  
  # Convert to Image object and save
  im_mask = Image.fromarray(mask)
  
  # Add mask to alpha of original image
  im.putalpha(im_mask)
  
  im.save('CFHTLS_082_0389.png')
  

if __name__ == '__main__':
  createMask()