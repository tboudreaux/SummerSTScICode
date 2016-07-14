from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[38.511375,-12.715803],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PHL_1359/sdB_PHL_1359_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PHL_1359/sdB_PHL_1359_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
