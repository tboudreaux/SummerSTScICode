from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[313.884167,0.081533],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_2052-003/sdB_PG_2052-003_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_2052-003/sdB_PG_2052-003_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
