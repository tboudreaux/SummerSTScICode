from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[241.460583,6.127222],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_160550.54+060738/sdB_sdssj_160550.54+060738_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_160550.54+060738/sdB_sdssj_160550.54+060738_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
