from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[106.766083,-3.148492],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_JL_129/sdB_JL_129_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_JL_129/sdB_JL_129_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
