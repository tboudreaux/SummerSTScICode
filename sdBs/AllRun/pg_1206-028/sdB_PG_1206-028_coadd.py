from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[182.3665,-3.034919],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1206-028/sdB_PG_1206-028_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1206-028/sdB_PG_1206-028_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
