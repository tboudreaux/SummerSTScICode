from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[153.839042,26.597417],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_101521.37+263550.7/sdB_SDSSJ_101521.37+263550.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_101521.37+263550.7/sdB_SDSSJ_101521.37+263550.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
