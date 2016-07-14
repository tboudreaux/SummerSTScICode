from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[236.703208,31.361778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_154648.77+312142.4/sdB_sdssj_154648.77+312142.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_154648.77+312142.4/sdB_sdssj_154648.77+312142.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
