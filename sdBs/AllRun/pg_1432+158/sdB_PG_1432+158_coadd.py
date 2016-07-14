from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[218.828792,15.671003],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1432+158/sdB_PG_1432+158_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1432+158/sdB_PG_1432+158_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
