from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[174.727583,-16.970389],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_he_1136-1641/sdB_he_1136-1641_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_he_1136-1641/sdB_he_1136-1641_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
