from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[131.549792,24.419528],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_0843+246/sdB_pg_0843+246_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_0843+246/sdB_pg_0843+246_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
