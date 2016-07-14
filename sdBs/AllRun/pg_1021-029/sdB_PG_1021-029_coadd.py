from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[156.075208,-3.177442],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1021-029/sdB_PG_1021-029_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1021-029/sdB_PG_1021-029_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
