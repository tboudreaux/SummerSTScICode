from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[137.980417,16.716244],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_0909+169/sdB_pg_0909+169_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_0909+169/sdB_pg_0909+169_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
