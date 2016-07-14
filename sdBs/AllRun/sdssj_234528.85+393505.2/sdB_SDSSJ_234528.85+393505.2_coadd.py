from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[356.370208,39.584778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_234528.85+393505.2/sdB_SDSSJ_234528.85+393505.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_234528.85+393505.2/sdB_SDSSJ_234528.85+393505.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
