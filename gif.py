import imageio as iio 
filenames=['/home/hasitha/Documents/team-pic1.png','/home/hasitha/Documents/team-pic2.png']
images=[]





for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('team.gif',images,duration=500,loop=0)
    
