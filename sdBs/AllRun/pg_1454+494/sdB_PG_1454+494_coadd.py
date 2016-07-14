from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[224.028167,49.187917],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1454+494/sdB_PG_1454+494_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1454+494/sdB_PG_1454+494_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
