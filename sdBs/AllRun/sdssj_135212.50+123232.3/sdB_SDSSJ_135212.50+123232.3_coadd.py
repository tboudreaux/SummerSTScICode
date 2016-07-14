from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[208.052083,12.542306],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_135212.50+123232.3/sdB_SDSSJ_135212.50+123232.3_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_135212.50+123232.3/sdB_SDSSJ_135212.50+123232.3_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
