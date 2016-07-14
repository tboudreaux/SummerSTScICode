from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[254.346667,65.524758],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1657+656/sdB_pg_1657+656_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1657+656/sdB_pg_1657+656_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()