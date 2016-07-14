from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[339.069292,-31.703633],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PHL_334/sdB_PHL_334_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PHL_334/sdB_PHL_334_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
