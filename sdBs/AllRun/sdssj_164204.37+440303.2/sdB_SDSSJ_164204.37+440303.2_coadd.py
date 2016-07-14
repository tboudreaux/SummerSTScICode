from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[250.518208,44.050889],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_164204.37+440303.2/sdB_SDSSJ_164204.37+440303.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_164204.37+440303.2/sdB_SDSSJ_164204.37+440303.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
