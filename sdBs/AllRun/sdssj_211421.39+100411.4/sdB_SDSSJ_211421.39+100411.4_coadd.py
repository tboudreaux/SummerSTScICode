from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[318.589125,10.069833],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_211421.39+100411.4/sdB_SDSSJ_211421.39+100411.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_211421.39+100411.4/sdB_SDSSJ_211421.39+100411.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
