from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[227.120917,49.680806],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_CBS_302/sdB_CBS_302_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_CBS_302/sdB_CBS_302_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
