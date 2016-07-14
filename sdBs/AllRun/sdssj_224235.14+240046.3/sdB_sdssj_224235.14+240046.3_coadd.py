from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[340.646417,24.012861],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_224235.14+240046.3/sdB_sdssj_224235.14+240046.3_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_224235.14+240046.3/sdB_sdssj_224235.14+240046.3_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
