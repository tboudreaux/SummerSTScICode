from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[208.507667,13.730667],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1351+139/sdB_PG_1351+139_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1351+139/sdB_PG_1351+139_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
