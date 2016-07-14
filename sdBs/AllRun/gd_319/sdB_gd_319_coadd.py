from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[192.518792,55.100889],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_gd_319/sdB_gd_319_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_gd_319/sdB_gd_319_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
