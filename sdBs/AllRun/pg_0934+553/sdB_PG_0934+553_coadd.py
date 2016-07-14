from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[144.58475,55.098117],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_0934+553/sdB_PG_0934+553_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_0934+553/sdB_PG_0934+553_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()