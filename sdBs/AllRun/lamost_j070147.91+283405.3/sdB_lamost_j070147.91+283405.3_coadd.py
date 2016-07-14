from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[105.449625,28.568139],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_lamost_j070147.91+283405.3/sdB_lamost_j070147.91+283405.3_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_lamost_j070147.91+283405.3/sdB_lamost_j070147.91+283405.3_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
