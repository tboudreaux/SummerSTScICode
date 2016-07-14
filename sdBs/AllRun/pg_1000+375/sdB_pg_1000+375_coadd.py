from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[150.831792,37.276569],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1000+375/sdB_pg_1000+375_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1000+375/sdB_pg_1000+375_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
