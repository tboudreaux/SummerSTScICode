from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[215.668042,-9.288942],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_UVO_1419-09/sdB_UVO_1419-09_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_UVO_1419-09/sdB_UVO_1419-09_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
