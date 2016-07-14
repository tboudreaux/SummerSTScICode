from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[150.874833,35.939319],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_CBS_123/sdB_CBS_123_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_CBS_123/sdB_CBS_123_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
