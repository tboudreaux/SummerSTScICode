from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[255.169458,33.630103],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1658+337/sdB_PG_1658+337_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1658+337/sdB_PG_1658+337_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
