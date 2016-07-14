from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[91.8155,64.502111],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_060715.72+643007.6/sdB_SDSSJ_060715.72+643007.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_060715.72+643007.6/sdB_SDSSJ_060715.72+643007.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
