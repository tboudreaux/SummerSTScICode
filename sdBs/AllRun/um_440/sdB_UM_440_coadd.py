from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[174.354792,0.382706],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_UM_440/sdB_UM_440_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_UM_440/sdB_UM_440_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
