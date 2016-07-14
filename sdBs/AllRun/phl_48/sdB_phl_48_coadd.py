from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[323.85825,-6.961831],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_phl_48/sdB_phl_48_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_phl_48/sdB_phl_48_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
