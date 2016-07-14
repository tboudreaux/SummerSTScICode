from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[122.292458,20.960111],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_080910.19+205736.4/sdB_SDSSJ_080910.19+205736.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_080910.19+205736.4/sdB_SDSSJ_080910.19+205736.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
