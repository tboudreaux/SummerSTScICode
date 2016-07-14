from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[242.015417,7.074744],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1605+072/sdB_PG_1605+072_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1605+072/sdB_PG_1605+072_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
