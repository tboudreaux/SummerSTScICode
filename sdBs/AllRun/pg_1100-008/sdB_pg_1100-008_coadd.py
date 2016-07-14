from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[165.759875,-1.06075],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1100-008/sdB_pg_1100-008_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1100-008/sdB_pg_1100-008_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
