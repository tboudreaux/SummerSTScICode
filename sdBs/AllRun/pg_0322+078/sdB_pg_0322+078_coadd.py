from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[51.392208,7.998003],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_0322+078/sdB_pg_0322+078_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_0322+078/sdB_pg_0322+078_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
