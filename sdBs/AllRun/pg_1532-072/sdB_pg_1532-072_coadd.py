from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[233.780042,-7.409414],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1532-072/sdB_pg_1532-072_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1532-072/sdB_pg_1532-072_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
