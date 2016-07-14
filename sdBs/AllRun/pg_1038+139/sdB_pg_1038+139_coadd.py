from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[160.376542,13.6874],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1038+139/sdB_pg_1038+139_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1038+139/sdB_pg_1038+139_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()