from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[104.245583,28.749333],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_LAMOST_J065658.95+284457.6/sdB_LAMOST_J065658.95+284457.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_LAMOST_J065658.95+284457.6/sdB_LAMOST_J065658.95+284457.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
