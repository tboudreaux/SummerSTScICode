from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[222.783542,-18.932981],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_EC_14483-1843/sdB_EC_14483-1843_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_EC_14483-1843/sdB_EC_14483-1843_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
