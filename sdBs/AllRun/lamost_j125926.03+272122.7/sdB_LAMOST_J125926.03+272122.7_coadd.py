from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[194.858458,27.356306],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_LAMOST_J125926.03+272122.7/sdB_LAMOST_J125926.03+272122.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_LAMOST_J125926.03+272122.7/sdB_LAMOST_J125926.03+272122.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
