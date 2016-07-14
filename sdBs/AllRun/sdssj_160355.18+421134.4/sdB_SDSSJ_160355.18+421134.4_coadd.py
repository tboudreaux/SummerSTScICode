from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[240.979917,42.192889],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_160355.18+421134.4/sdB_SDSSJ_160355.18+421134.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_160355.18+421134.4/sdB_SDSSJ_160355.18+421134.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
