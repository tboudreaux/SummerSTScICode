from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[186.654792,57.99125],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1224+583/sdB_pg_1224+583_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1224+583/sdB_pg_1224+583_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
