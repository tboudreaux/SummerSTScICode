from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[249.549,27.839111],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_163811.76+275020.8/sdB_sdssj_163811.76+275020.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_163811.76+275020.8/sdB_sdssj_163811.76+275020.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
