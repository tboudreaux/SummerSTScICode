from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[259.939167,51.869489],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1718+519/sdB_pg_1718+519_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1718+519/sdB_pg_1718+519_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
