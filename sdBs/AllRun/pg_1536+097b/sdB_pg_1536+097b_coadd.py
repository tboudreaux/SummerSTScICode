from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[234.851917,9.557817],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1536+097b/sdB_pg_1536+097b_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1536+097b/sdB_pg_1536+097b_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
