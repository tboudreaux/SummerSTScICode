from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[250.191417,12.687031],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1638+128/sdB_pg_1638+128_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1638+128/sdB_pg_1638+128_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
