from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[209.836583,32.14625],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_135920.78+320846.5/sdB_SDSSJ_135920.78+320846.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_135920.78+320846.5/sdB_SDSSJ_135920.78+320846.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
