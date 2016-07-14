from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[155.645458,46.016306],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_lamost_j102234.91+460058.7/sdB_lamost_j102234.91+460058.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_lamost_j102234.91+460058.7/sdB_lamost_j102234.91+460058.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
