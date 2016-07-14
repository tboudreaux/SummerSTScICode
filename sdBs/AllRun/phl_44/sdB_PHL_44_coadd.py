from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[323.805542,-13.556272],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PHL_44/sdB_PHL_44_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PHL_44/sdB_PHL_44_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
