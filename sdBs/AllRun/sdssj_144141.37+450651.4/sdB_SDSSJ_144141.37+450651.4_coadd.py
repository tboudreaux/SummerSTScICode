from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[220.422375,45.114278],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_144141.37+450651.4/sdB_SDSSJ_144141.37+450651.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_144141.37+450651.4/sdB_SDSSJ_144141.37+450651.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
