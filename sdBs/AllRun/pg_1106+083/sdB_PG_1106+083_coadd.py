from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[167.1825,8.030292],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1106+083/sdB_PG_1106+083_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1106+083/sdB_PG_1106+083_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
