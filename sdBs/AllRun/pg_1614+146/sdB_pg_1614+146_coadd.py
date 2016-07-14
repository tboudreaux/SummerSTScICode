from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[244.127208,14.448858],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1614+146/sdB_pg_1614+146_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1614+146/sdB_pg_1614+146_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
