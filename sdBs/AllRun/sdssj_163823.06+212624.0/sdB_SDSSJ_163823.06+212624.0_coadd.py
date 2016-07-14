from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[249.596083,21.44],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_163823.06+212624.0/sdB_SDSSJ_163823.06+212624.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_163823.06+212624.0/sdB_SDSSJ_163823.06+212624.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
