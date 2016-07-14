from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[250.858667,33.020433],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1641+331/sdB_PG_1641+331_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1641+331/sdB_PG_1641+331_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
