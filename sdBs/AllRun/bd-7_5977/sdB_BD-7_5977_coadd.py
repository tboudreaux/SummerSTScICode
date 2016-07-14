from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[349.444917,-6.475281],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_BD-7_5977/sdB_BD-7_5977_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_BD-7_5977/sdB_BD-7_5977_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
