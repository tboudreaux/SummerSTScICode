from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[221.784042,23.360553],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1444+236/sdB_PG_1444+236_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1444+236/sdB_PG_1444+236_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
