from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[225.224917,2.862],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_150053.98+025143.2/sdB_SDSSJ_150053.98+025143.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_150053.98+025143.2/sdB_SDSSJ_150053.98+025143.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
