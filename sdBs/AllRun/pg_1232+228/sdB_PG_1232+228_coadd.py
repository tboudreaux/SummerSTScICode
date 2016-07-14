from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[188.809042,22.588892],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1232+228/sdB_PG_1232+228_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1232+228/sdB_PG_1232+228_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
