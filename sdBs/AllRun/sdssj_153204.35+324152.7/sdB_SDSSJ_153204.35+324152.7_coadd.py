from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[233.018125,32.697972],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_153204.35+324152.7/sdB_SDSSJ_153204.35+324152.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_153204.35+324152.7/sdB_SDSSJ_153204.35+324152.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
