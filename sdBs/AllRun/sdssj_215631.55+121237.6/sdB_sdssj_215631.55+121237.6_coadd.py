from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[329.131458,12.210444],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_215631.55+121237.6/sdB_sdssj_215631.55+121237.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_215631.55+121237.6/sdB_sdssj_215631.55+121237.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
