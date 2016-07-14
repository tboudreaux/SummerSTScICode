from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[254.569042,27.025628],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1656+271/sdB_PG_1656+271_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1656+271/sdB_PG_1656+271_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
