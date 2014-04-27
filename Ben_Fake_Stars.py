import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pylab

nstars = 50 #How many fake stars do you want?
x,y = np.indices((1500,1500)) #What is your resolution?

img_noise = np.random.normal(scale=1., size=(1500,1500)) + 4.321 #Generating noise, play around with this to create gaussian noise similar to your camera


xpos = np.random.randint(30, len(x)-30, size=nstars) #Random X and Y positions
ypos = np.random.randint(30, len(y)-30, size=nstars)
mag = np.random.lognormal(mean=2.5, sigma=0.4, size=nstars) #Creating random magnitudes, again play around with this to suit your conditions. Increasing the mean increases the brightness of the star


sigma = 3.
make_star = lambda x0, y0, amp: amp * np.exp(-0.5/sigma**2*((x-x0)**2 + (y-y0)**2)) #just a Gaussian function. This is the PSF of a star, all stars have a gaussian function which varies with the quality of your observing instrument/conditions

img = img_noise.copy()
for i in xrange(nstars):
    print("Making star {} at ({:.2f},{:.2f}) with peak flux {:.2f}".format(i, xpos[i], ypos[i], mag[i]))
    img += make_star(xpos[i], ypos[i], mag[i])

fig, ax = pylab.subplots(figsize=(8,8))
final_image=plt.imshow(img, interpolation='nearest') #Change interpolation to 'nearest' for a pure pixel map. 'Bicubic' smooths it out (blurs). Read numpy manual for interpolation meanings
final_image.set_cmap('gray')
plt.show()
#plt.savefig('Ben_Test.jpeg')