from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[122.5325,51.498922],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_0806+516/sdB_PG_0806+516_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_0806+516/sdB_PG_0806+516_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
