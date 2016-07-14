from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[63.8205,-7.665192],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_lhs_24/sdB_lhs_24_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_lhs_24/sdB_lhs_24_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
