from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[238.443667,-7.772514],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1551-076/sdB_pg_1551-076_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1551-076/sdB_pg_1551-076_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
