from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[328.580542,-6.181842],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PHL_197/sdB_PHL_197_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PHL_197/sdB_PHL_197_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
