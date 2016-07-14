from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[10.396792,20.154856],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_0038+199/sdB_pg_0038+199_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_0038+199/sdB_pg_0038+199_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
