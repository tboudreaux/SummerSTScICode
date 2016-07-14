from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[146.299042,-3.155392],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_0942-029/sdB_pg_0942-029_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_0942-029/sdB_pg_0942-029_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
