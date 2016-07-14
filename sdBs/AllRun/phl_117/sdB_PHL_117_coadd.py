from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[325.995625,-23.486639],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PHL_117/sdB_PHL_117_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PHL_117/sdB_PHL_117_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
