from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[194.330667,-15.939667],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_EC_12546-1540/sdB_EC_12546-1540_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_EC_12546-1540/sdB_EC_12546-1540_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
