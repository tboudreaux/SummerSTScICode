from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[171.226542,51.475942],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1122+517/sdB_PG_1122+517_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1122+517/sdB_PG_1122+517_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
