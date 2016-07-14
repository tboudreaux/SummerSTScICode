from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[52.280792,-11.705708],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PHL_1548/sdB_PHL_1548_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PHL_1548/sdB_PHL_1548_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
