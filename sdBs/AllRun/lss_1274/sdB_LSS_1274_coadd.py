from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[139.733542,-57.073814],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_LSS_1274/sdB_LSS_1274_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_LSS_1274/sdB_LSS_1274_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
