from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[241.997042,38.629692],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1606+388/sdB_pg_1606+388_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1606+388/sdB_pg_1606+388_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
