from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[126.324958,11.518417],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_LAMOST_J082517.99+113106.3/sdB_LAMOST_J082517.99+113106.3_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_LAMOST_J082517.99+113106.3/sdB_LAMOST_J082517.99+113106.3_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
