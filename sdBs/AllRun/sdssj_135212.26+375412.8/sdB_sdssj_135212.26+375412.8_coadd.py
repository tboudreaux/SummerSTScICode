from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[208.051083,37.903556],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_135212.26+375412.8/sdB_sdssj_135212.26+375412.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_135212.26+375412.8/sdB_sdssj_135212.26+375412.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
