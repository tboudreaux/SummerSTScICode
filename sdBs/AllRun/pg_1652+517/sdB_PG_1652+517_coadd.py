from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[253.552292,51.650081],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1652+517/sdB_PG_1652+517_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1652+517/sdB_PG_1652+517_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
