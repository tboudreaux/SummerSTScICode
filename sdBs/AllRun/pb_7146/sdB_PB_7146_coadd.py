from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[340.708042,-2.732153],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PB_7146/sdB_PB_7146_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PB_7146/sdB_PB_7146_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
